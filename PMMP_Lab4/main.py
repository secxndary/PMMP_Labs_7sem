import cv2
import numpy as np


class MyOpenCv:
    def __init__(self):
        self.file_path = "image.jpg"
        self.image = cv2.imread(self.file_path)

    def get_image(self, file_path="image.jpg"):
        if file_path is None:
            file_path = self.file_path
        image = cv2.imread(file_path)
        return image

    def save_image(self, image, file_path):
        if image is None:
            image = self.image
        if self.image is None:
            print("[ERROR] No image to save. Use load_image() to load an image first.")
            return
        cv2.imwrite(file_path, image)
        print(f"[OK] Image saved as {file_path}")

    def show_image(self, image, width=600, height=600, window_name="Loaded image"):
        if image is None:
            image = self.image
        if self.image is None:
            print("[ERROR] No image loaded. Use load_image() to load an image.")
            return
        image_resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imshow(window_name, image_resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_external_contours(self, thresh1=127, thresh2=255, thickness=3, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)
        _, thresh = cv2.threshold(image_blur, thresh1, thresh2, 0)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (255, 0, 230), thickness)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness)
        print(f"Количество объектов: {len(contours)}")
        max_length_contour = max(contours, key=lambda x: len(x))
        max_area_contour = max(contours, key=lambda x: cv2.contourArea(x))
        # thickness + 6 because max_length_contour and max_area_contour is the same object (in this particular image)
        cv2.drawContours(image, [max_length_contour], -1, (50, 250, 255), thickness + 6)
        cv2.drawContours(image, [max_area_contour], -1, (0, 0, 255), thickness)
        return image

    def get_quadrilaterals(self, thresh1=127, thresh2=255, thickness=3, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)
        _, image_thresh = cv2.threshold(image_blur, thresh1, thresh2, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(image_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        quadrilaterals_count = 0
        for contour in contours:
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) == 4:
                cv2.drawContours(image, [contour], -1, (0, 0, 255), thickness)
                quadrilaterals_count += 1
        print(f"Количество прямоугольников: {quadrilaterals_count}")
        return image

    def get_hough_lines(self, thresh1=127, thresh2=255, thickness=3, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(image_gray, thresh1, thresh2, apertureSize=3)
        lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * -b)
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * -b)
            y2 = int(y0 - 1000 * a)
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness)
        return image

    def get_hough_circles(self, thresh1=127, thresh2=255, thickness=3, file_path="image.jpg"):
        image = self.get_image(file_path)
        image_with_circles = image.copy()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, image_thresh = cv2.threshold(image_gray, thresh1, thresh2, cv2.THRESH_BINARY)
        circles = cv2.HoughCircles(
            image_thresh, cv2.HOUGH_GRADIENT_ALT, dp=5, minDist=10, param1=1, param2=0.5, minRadius=0, maxRadius=0
        )
        circles_count = 0
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                center = (circle[0], circle[1])
                radius = circle[2]
                cv2.circle(image_with_circles, center, radius, (0, 255, 0), thickness)
                circles_count += 1
        print(f"Количество круглых объектов: {circles_count}")
        return image_with_circles


if __name__ == "__main__":
    cv = MyOpenCv()

    huawei_file_path = "huawei.jpg"
    quadrilaterals_file_path = "quadrilaterals.jpg"
    lines_file_path = "lines.jpg"
    circles_file_path = "circles.jpg"

    external_contours = cv.get_external_contours(thresh1=165, thresh2=255, thickness=2, file_path=huawei_file_path)
    quadrilaterals = cv.get_quadrilaterals(thresh1=127, thresh2=255, thickness=2, file_path=quadrilaterals_file_path)
    hough_lines = cv.get_hough_lines(thresh1=150, thresh2=255, thickness=1, file_path=lines_file_path)
    hough_circles = cv.get_hough_circles(thresh1=110, thresh2=255, thickness=3, file_path=circles_file_path)

    cv.show_image(external_contours, window_name="External contours")
    cv.show_image(quadrilaterals, width=600, height=281, window_name="Quadrilaterals")
    cv.show_image(hough_lines, window_name="Hough lines")
    cv.show_image(hough_circles, window_name="Hough circles")
