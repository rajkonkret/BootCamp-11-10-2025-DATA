import cv2
import dlib
import matplotlib.pyplot as plt

# # https://github.com/eddiehe99/dlib-whl/releases/tag/v19.24.6
# # pip install .\dlib-19.24.6-cp312-cp312-win_amd64.whl

image_path = "obraz.jpg"
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Nie udało się wczytać obrazu")

gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

# wykryj twarze
detector = dlib.get_frontal_face_detector()

# faces = detector(gray)
faces = detector(gray, upsample_num_times=4)

for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(image, (x, y), (x + w, y + w), (255, 0, 0), 2)

cv2.imshow("Detekcja twarzy", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
