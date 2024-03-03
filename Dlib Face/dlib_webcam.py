import dlib
import cv2

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while cv2.waitKey(1) & 0xFF != ord('q'):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("FaceCaptureFromWebcamFeed", frame)

cap.release()
cv2.destroyAllWindows()