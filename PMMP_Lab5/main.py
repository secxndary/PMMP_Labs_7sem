import cv2
import numpy as np


class MyOpenCv:
    def __init__(self, file_path="image.jpg"):
        self.file_path = file_path
        self.image = cv2.imread(self.file_path)
        self.image_copy = self.image.copy()

    def get_image(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        image = cv2.imread(file_path)
        return image

    def show_image(self, image=None, width=600, height=600, window_name="Loaded image"):
        if image is None:
            image = self.image
        if image is None:
            print("[ERROR] No image loaded. Use load_image() to load an image.")
            return
        image_resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imshow(window_name, image_resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_harris_corners(self, block_size=2, k_size=3, k=0.04, param=0.01, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(np.float32)
        image_normalized = cv2.normalize(image_gray, None, 0.0, 1.0, cv2.NORM_MINMAX)
        corners = cv2.cornerHarris(image_normalized, blockSize=block_size, ksize=k_size, k=k)
        corners = cv2.dilate(corners, None)
        image[corners > param * corners.max()] = [0, 0, 255]
        return image

    def get_shi_tomasi_corners(self, max_corners=100, quality_level=0.01, min_distance=10, thickness=3, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(image_gray, maxCorners=max_corners, qualityLevel=quality_level,
                                          minDistance=min_distance)
        corners = np.int0(corners)
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(image, (x, y), thickness, [0, 255, 0], -1)
        return image

    def get_perspective_image(self, threshold1=75, threshold2=200, approx_epsilon=0.02, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_with_list_contour = image.copy()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(image_gray, threshold1, threshold2)
        contours = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
        screen_contour = None
        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, approx_epsilon * peri, True)
            if len(approx) == 4:
                screen_contour = approx
                break
        if screen_contour is not None:
            cv2.drawContours(image_with_list_contour, [screen_contour], -1, (0, 255, 0), 2)
            rect = np.array(screen_contour, dtype="float32")
            dst = np.array([[0, 0], [500, 0], [500, 500], [0, 500]], dtype="float32")
            M = cv2.getPerspectiveTransform(rect, dst)
            image_warped = cv2.warpPerspective(image, M, (500, 500))
            image_warped = cv2.cvtColor(image_warped, cv2.COLOR_BGR2GRAY)
            _, image_warped = cv2.threshold(image_warped, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            image_warped = cv2.flip(image_warped, 1)
            image_warped = cv2.rotate(image_warped, cv2.ROTATE_90_COUNTERCLOCKWISE)
            return image_warped


if __name__ == "__main__":
    perspective_file_path = "perspective.jpg"
    cv = MyOpenCv()

    harris_corners = cv.get_harris_corners(block_size=2, k_size=3, k=0.04, param=0.07, file_path="corners.jpg")
    shi_tomasi_corners = cv.get_shi_tomasi_corners(max_corners=300, quality_level=0.01, min_distance=10,
                                                      thickness=4, file_path="corners.jpg")
    perspective = cv.get_perspective_image(threshold1=75, threshold2=200, approx_epsilon=0.02, file_path=perspective_file_path)

    cv.show_image(harris_corners, window_name="Harris Corners")
    cv.show_image(shi_tomasi_corners, window_name="Shi-Tomasi Corners")
    cv.show_image(perspective, window_name="Perspective image")
