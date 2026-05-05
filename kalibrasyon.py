import cv2

# Videonun ilk karesini açalım
video_yolu = 'input_videos/08fd33_4.mp4'
cap = cv2.VideoCapture(video_yolu)
basarili, img = cap.read()

print("LÜTFEN SIRAYLA ŞU 4 NOKTAYA TIKLAYIN:")
print("1. Sol Üst, 2. Sağ Üst, 3. Sağ Alt, 4. Sol Alt")

def tiklama_olayi(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"[{x}, {y}],")
        # Setzen Sie einen roten Punkt an die angeklickte Stelle.
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('Kalibrasyon Ekrani', img)

cv2.imshow('Kalibrasyon Ekrani', img)
cv2.setMouseCallback('Kalibrasyon Ekrani', tiklama_olayi)
cv2.waitKey(0)
cv2.destroyAllWindows()