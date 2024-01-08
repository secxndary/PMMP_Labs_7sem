import cv2
from matplotlib import pyplot as plt


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

    def get_gray_image(self, file_path="image.jpg"):
        if file_path is None:
            file_path = self.file_path
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        return image

    def show_cvt_color(self):
        image_cvt = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.show_image(image_cvt, window_name="Gray image")
        return image_cvt

    def show_threshold(self, file_path="image.jpg"):
        image_gray = self.get_gray_image(file_path)
        ret, image_threshold = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
        self.show_image(image_threshold, window_name="Threshold image")
        return image_threshold

    def show_adaptive_threshold_gaussian(self, file_path="image.jpg"):
        image_gray = self.get_gray_image(file_path)
        image_adaptive_threshold = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                         cv2.THRESH_BINARY, 5, 2)
        self.show_image(image_adaptive_threshold, window_name="Adaptive threshold gaussian image")
        return image_adaptive_threshold

    def show_adaptive_threshold_mean(self, file_path="image.jpg"):
        image_gray = self.get_gray_image(file_path)
        image_adaptive_threshold = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                         cv2.THRESH_BINARY, 5, 2)
        self.show_image(image_adaptive_threshold, window_name="Adaptive threshold mean image")
        return image_adaptive_threshold

    def show_equalize_hist(self, file_path="image.jpg"):
        image_gray = self.get_gray_image(file_path)
        image_equalize_hist = cv2.equalizeHist(image_gray)
        self.show_image(image_equalize_hist, window_name="Equalize histogram image")
        return image_equalize_hist

    def show_histogram(self, image, title="Histogram"):
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        plt.plot(hist, color='b')
        plt.title(title)
        plt.show()


if __name__ == "__main__":
    cv = MyOpenCv()
    chel_file_path = "chel.jpg"
    sudoku_file_path = "sudoku.jpg"

    cv.show_image(cv.image)
    chel = cv.get_image(chel_file_path)

    image_cvt = cv.show_cvt_color()
    sudoku_threshold = cv.show_threshold(sudoku_file_path)
    sudoku_adaptive_threshold_mean = cv.show_adaptive_threshold_mean(sudoku_file_path)
    sudoku_adaptive_threshold_gaussian = cv.show_adaptive_threshold_gaussian(sudoku_file_path)

    cv.show_image(chel, window_name="Original chel")
    cv.show_histogram(chel, "Original histogram")
    chel_equalized_hist = cv.show_equalize_hist(chel_file_path)
    cv.show_histogram(chel_equalized_hist, "Histogram after equalization")

    cv.save_image(image_cvt, 'image_cvt.jpg')
    cv.save_image(sudoku_threshold, 'sudoku_threshold.jpg')
    cv.save_image(sudoku_adaptive_threshold_mean, 'sudoku_adaptive_threshold_mean.jpg')
    cv.save_image(sudoku_adaptive_threshold_gaussian, 'sudoku_adaptive_threshold_gaussian.jpg')
    cv.save_image(chel_equalized_hist, 'chel_equalize_hist.jpg')
