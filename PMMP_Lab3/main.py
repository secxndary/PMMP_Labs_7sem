import cv2


class MyOpenCv:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def __del__(self):
        self.capture.release()

    def process_video(self, blur_k_size=5, sobel_k_size=5, canny_threshold1=45, canny_threshold2=80):
        while True:
            ret, frame = self.capture.read()
            frame = cv2.flip(frame, 1)

            if not ret:
                print("[ERROR] Unable to capture frame.")
                break

            blurred_frame = cv2.GaussianBlur(frame, (blur_k_size, blur_k_size), 0)

            sobel_x = cv2.Sobel(blurred_frame, cv2.CV_64F, 1, 0, ksize=sobel_k_size)
            sobel_y = cv2.Sobel(blurred_frame, cv2.CV_64F, 0, 1, ksize=sobel_k_size)
            sobel_result = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

            laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
            laplacian_result = cv2.convertScaleAbs(laplacian)

            canny_edges = cv2.Canny(blurred_frame, canny_threshold1, canny_threshold2)

            cv2.imshow('Original', frame)
            cv2.imshow('Sobel', sobel_result)
            cv2.imshow('Laplacian', laplacian_result)
            cv2.imshow('Canny Edges', canny_edges)

            if cv2.waitKey(1) == 27:    # press the escape button
                break


if __name__ == "__main__":
    cv = MyOpenCv()
    cv.process_video(blur_k_size=5, sobel_k_size=5, canny_threshold1=45, canny_threshold2=80)
