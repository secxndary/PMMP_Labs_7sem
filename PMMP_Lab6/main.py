import cv2


class MyOpenCv:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        self.mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')
        self.smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    def detect_face(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(150, 150))
        for (x, y, w, h) in faces:
            # face
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            # eyes
            eyes = self.eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=9, minSize=(30, 30))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(image, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
            # mouth
            mouths = self.mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=9,
                                                         minSize=(50, 50), maxSize=(90, 90))
            for (mx, my, mw, mh) in mouths:
                cv2.rectangle(image, (x + mx, y + my), (x + mx + mw, y + my + mh), (0, 0, 255), 2)
            # smile
            smiles = self.smile_cascade.detectMultiScale(roi_gray, minSize=(70, 70), scaleFactor=1.2)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(image, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (255, 255, 0), 2)

            if len(mouths) == 0:
                cv2.putText(image, "Mask on", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.putText(image, "Mask off", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            if len(eyes) == 0:
                cv2.putText(image, "Closed eyes", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            elif len(eyes) == 1:
                cv2.putText(image, "Pirate", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            else:
                cv2.putText(image, "Open eyes", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if len(smiles) == 0:
                cv2.putText(image, "Sad", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            else:
                cv2.putText(image, "Happy", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return image

    def show_video(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            _, frame = video_capture.read()
            processed_frame = self.detect_face(frame)
            # processed_frame = cv2.flip(processed_frame, 1)
            cv2.imshow('Face Detection', processed_frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    cv = MyOpenCv()
    cv.show_video()
