import streamlit as st
import tempfile
import imageio_ffmpeg
import subprocess
import os
from main import process_video 

# 1. Sayfa Tasarımı ve Başlık
st.set_page_config(page_title="Fußball Analyse KI", page_icon="⚽", layout="wide")
st.title("⚽ KI Fußball-Analyse Dashboard")
st.write("Bitte laden Sie das Fußballvideo hoch, das Sie analysieren möchten.")

# OTURUM HAFIZASI (Session State): Uygulamanın videoyu işlediğini unutmaması için
if 'video_processed' not in st.session_state:
    st.session_state.video_processed = False
if 'web_video_path' not in st.session_state:
    st.session_state.web_video_path = ""

# 2. Kullanıcıdan Video Alma Kutusu
yuklenen_video = st.file_uploader("Video hochladen (mp4, avi)", type=['mp4', 'avi'])

if yuklenen_video is not None:
    # EĞER VİDEO HENÜZ İŞLENMEDİYSE (İlk Aşama)
    if not st.session_state.video_processed:
        st.subheader("Hochgeladenes Originalvideo")
        st.video(yuklenen_video)
        
        if st.button("Analyse starten", type="primary"):
            with st.spinner("Die KI verfolgt die Spieler, bitte warten..."):
                tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') 
                tfile.write(yuklenen_video.read())
                
                ilk_sonuc_yolu = "output_videos/analizli_sonuc.mp4"
                web_uyumlu_yol = "output_videos/web_sonuc.mp4"
                
                # Videoyu İşle
                process_video(tfile.name, ilk_sonuc_yolu)
                
                st.info("Das Video wird in ein webbrowser-kompatibles Format konvertiert, bitte warten...")
                
                try:
                    ffmpeg_motoru = imageio_ffmpeg.get_ffmpeg_exe()
                    subprocess.run(
                        [ffmpeg_motoru, "-y", "-i", ilk_sonuc_yolu, "-vcodec", "libx264", web_uyumlu_yol],
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    st.success("Analyse und Konvertierung erfolgreich abgeschlossen!")
                    
                    # İşlemin bittiğini hafızaya kaydet ve sayfayı yenile
                    st.session_state.video_processed = True
                    st.session_state.web_video_path = web_uyumlu_yol
                    st.rerun() # Sayfayı otomatik yenileyip ikinci aşamaya geçer
                    
                except Exception as e:
                    st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
                    
    # EĞER VİDEO İŞLENDİYSE (İkinci Aşama: Video gösterimi ve Heatmap sorgusu)
    if st.session_state.video_processed:
        st.subheader("KI Analyse Ergebnisse")
        st.video(st.session_state.web_video_path)
        
        st.divider() # Araya şık bir ayırıcı çizgi
        
        # KULLANICIYA ID SORDUĞUMUZ KISIM
        st.markdown("### 🗺️ Spieler Heatmap Generator")
        st.write("Bitte geben Sie die ID des Spielers ein, für den Sie eine Heatmap erstellen möchten.")
        
        # Sayı girme kutucuğu (Form yapısı sayesinde butona basana kadar işlem yapmaz)
        with st.form("heatmap_form"):
            oyuncu_id = st.number_input("Spieler-ID eingeben:", min_value=0, step=1)
            heatmap_uret_butonu = st.form_submit_button("Heatmap generieren")
            
        # "Heatmap generieren" butonuna basılırsa
        if heatmap_uret_butonu:
            with st.spinner(f"Heatmap für Spieler {oyuncu_id} wird generiert..."):
                try:
                    # DİKKAT: Burada heatmap_generator.py dosyasına ID numarasını gönderiyoruz!
                    subprocess.run(["python3", "heatmap_generator.py", str(oyuncu_id)], check=True)
                    
                    # Oluşacak dosyanın adını belirliyoruz (Örn: player_14_heatmap.png)
                    heatmap_dosya_ismi = f"player_{oyuncu_id}_heatmap.png"
                    
                    if os.path.exists(heatmap_dosya_ismi):
                        st.success(f"Heatmap für Spieler {oyuncu_id} wurde erfolgreich erstellt!")
                        st.image(heatmap_dosya_ismi, width=600)
                    else:
                        st.error(f"Das Heatmap-Bild konnte nicht gefunden werden. Bitte stellen Sie sicher, dass der Spieler mit dieser ID existiert.")
                
                except subprocess.CalledProcessError:
                    st.error("Es gab einen Fehler bei der Erstellung der Heatmap!")
                    
        st.info("Sie können jederzeit eine neue ID eingeben, um eine andere Heatmap zu generieren.")