# cnn - convuntional neural network - sieci konwulsyjne
# # https://github.com/eddiehe99/dlib-whl/releases/tag/v19.24.6
# # pip install .\dlib-19.24.6-cp312-cp312-win_amd64.whl
# # https://github.com/eddiehe99/dlib-whl/blob/main/dlib-20.0.0-cp313-cp313-win_amd64.whl
# # pip install .\dlib-20.0.0-cp313-cp313-win_amd64.whl
# # brew

import cv2
import dlib
import matplotlib.pyplot as plt

# siec cnn
# wytrenowany model sieci
cnn_model_path = "mmod_human_face_detector.dat"

image_path = 'obraz.jpg'
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Nie udało się wczytać obrazu")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cnn_detector = dlib.cnn_face_detection_model_v1(cnn_model_path)

detections = cnn_detector(rgb_image, upsample_num_times=1)

for d in detections:
    rect = d.rect
    x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
    cv2.rectangle(image, (x, y - 20), (x + w + 10, y + w + 10), (0, 0, 255), 2)

plt.figure(figsize=(10, 2))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title(f"Dokładniejszy model - wykrytu twarzy: {len(detections)}")
plt.axis('off')

plt.savefig("obrazy_rozpoznane.png")
plt.show()
