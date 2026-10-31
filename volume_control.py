import cv2
import mediapipe as mp
import math       # Sanal cetvelimiz (hipotenüs) için
import numpy as np # Oran-orantı çevirmeni için
import os         # Mac'in terminaline komut göndermek için

kamera = cv2.VideoCapture(1)

mp_eller = mp.solutions.hands
eller = mp_eller.Hands(max_num_hands=1)
mp_cizim = mp.solutions.drawing_utils

while(True):
    ret, videoGoruntu = kamera.read()
    rgb_goruntu = cv2.cvtColor(videoGoruntu, cv2.COLOR_BGR2RGB)
    sonuc = eller.process(rgb_goruntu)

    if sonuc.multi_hand_landmarks:
            for el_koordinatlari in sonuc.multi_hand_landmarks:

                mp_cizim.draw_landmarks(videoGoruntu, el_koordinatlari, mp_eller.HAND_CONNECTIONS)
                
                h, w, c = videoGoruntu.shape

                basparmak_x = int(el_koordinatlari.landmark[4].x * w)
                basparmak_y = int(el_koordinatlari.landmark[4].y * h)
                
                isaret_x = int(el_koordinatlari.landmark[8].x * w)
                isaret_y = int(el_koordinatlari.landmark[8].y * h)
                
                cv2.circle(videoGoruntu, (basparmak_x, basparmak_y), 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(videoGoruntu, (isaret_x, isaret_y), 15, (255, 0, 0), cv2.FILLED)
                cv2.line(videoGoruntu, (basparmak_x, basparmak_y), (isaret_x, isaret_y), (255, 0, 0), 3)

                mesafe = math.hypot(isaret_x - basparmak_x, isaret_y - basparmak_y)
                
                ses_yuzdesi = np.interp(mesafe, [20, 200], [0, 100])
                
                os.system(f"osascript -e 'set volume output volume {int(ses_yuzdesi)}'")

                ses_bari = np.interp(mesafe, [20, 200], [50, 250])
                cv2.rectangle(videoGoruntu, (50, 100), (250, 150), (0, 0, 0), 3)
                cv2.rectangle(videoGoruntu, (50, 100), (int(ses_bari), 150), (0, 180, 100), cv2.FILLED)

                cv2.putText(videoGoruntu, f"Ses: %{int(ses_yuzdesi)}", (75, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    if ret == True:
        cv2.imshow('kamera',videoGoruntu)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()