import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import Pitch
import pandas as pd
import sys

class HeatmapGenerator:
    def __init__(self, data_path):
        # Kaydettiğimiz CSV dosyasını okuyoruz
        self.df = pd.read_csv(data_path)

    def generate_player_heatmap(self, player_id):
        # Sadece istediğimiz oyuncunun verilerini filtreliyoruz
        player_df = self.df[self.df['Player_ID'] == player_id]

        if player_df.empty:
            print(f"Uyarı: {player_id} ID'li oyuncu bulunamadı.")
            return

        # mplsoccer ile nizami futbol sahası oluşturuyoruz
        pitch = Pitch(pitch_type='custom', pitch_length=105, pitch_width=68, 
                      pitch_color='#22312b', line_color='#c7d5cc')
        fig, ax = pitch.draw(figsize=(10, 7))

        # Seaborn ile ısı haritasını (KDE) saha üzerine çizdiriyoruz
        sns.kdeplot(
            x=player_df['X'], 
            y=player_df['Y'], 
            fill=True, 
            cmap='magma', # Renk paleti (ateş rengi)
            alpha=0.6,    # Saydamlık
            ax=ax,
            warn_singular=False
        )
        
        plt.title(f"Oyuncu {player_id} Isi Haritasi", color='white')
        dosya_adi = f"player_{player_id}_heatmap.png"
        plt.savefig(dosya_adi)
        print(f"Harika! Isı haritası başarıyla kaydedildi: {dosya_adi}")

# Bu dosya tek başına çalıştırıldığında test etmek için:
if __name__ == "__main__":
    try:
        hm = HeatmapGenerator("oyuncu_koordinatlari.csv")
        
        # Eğer terminalden (app.py'den) bir numara geldiyse onu kullan, gelmediyse varsayılan olarak 14'ü kullan
        if len(sys.argv) > 1:
            player_id = int(sys.argv[1])
        else:
            player_id = 14
            
        print(f"Çizim başlatılıyor... Analiz edilen oyuncu ID: {player_id}")
        hm.generate_player_heatmap(player_id)
        
    except FileNotFoundError:
        print("Hata: oyuncu_koordinatlari.csv dosyası bulunamadı. Önce main.py'yi çalıştırmalısın.")
    except ValueError:
        print("Hata: Girdiğiniz oyuncu ID'si geçerli bir sayı değil.")