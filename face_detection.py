import cv2
import sys

image_path = sys.argv[1]
casc_path = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(casc_path)

image = cv2.imread(image_path)
gray_color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detected_faces = face_cascade.detectMultiScale(
    gray_color,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30, 30)
)

print(f"Number of faces found: {len(detected_faces)}")

for (x, y, w, h) in detected_faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
