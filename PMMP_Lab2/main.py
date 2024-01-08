import cv2
import numpy as np


class MyOpenCv:
    def __init__(self):
        self.file_path = "image.jpg"
        self.image = cv2.imread(self.file_path)

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

    def apply_linear_filter(self, kernel):
        result_image = cv2.filter2D(self.image, -1, kernel)
        return result_image

    def apply_blur(self, method="blur", kernel_size=5):
        if self.image is None:
            print("[ERROR] No image loaded. Use load_image() to load an image.")
            return None
        if method == "blur":
            result_image = cv2.blur(self.image, (kernel_size, kernel_size))
        elif method == "GaussianBlur":
            result_image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
        elif method == "medianBlur":
            result_image = cv2.medianBlur(self.image, kernel_size)
        else:
            print("[ERROR] Invalid blur method.")
            return None
        return result_image

    def apply_threshold(self, threshold=127, max_val=255, thresh_type=cv2.THRESH_BINARY):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, threshold, max_val, thresh_type)
        return binary_image

    def apply_erosion(self, kernel_size=5):
        binary_image = self.apply_threshold()
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.erode(binary_image, kernel, iterations=1)
        return result_image

    def apply_dilation(self, kernel_size=5):
        binary_image = self.apply_threshold()
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.dilate(binary_image, kernel, iterations=1)
        return result_image

    def apply_opening(self, kernel_size=5):
        binary_image = self.apply_threshold()
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
        return result_image

    def apply_closing(self, kernel_size=5):
        binary_image = self.apply_threshold()
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
        return result_image

    def apply_gradient(self, kernel_size=5):
        binary_image = self.apply_threshold()
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)
        return result_image

    def apply_adaptive_threshold(self, method="mean", block_size=11, c=2):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        if method == "mean":
            result_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                 cv2.THRESH_BINARY, block_size, c)
        elif method == "gaussian":
            result_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                 cv2.THRESH_BINARY, block_size, c)
        else:
            print("[ERROR] Invalid adaptive threshold method.")
            return None
        return result_image

    def apply_erosion_adaptive(self, method="mean", block_size=11, c=2, kernel_size=5):
        binary_image = self.apply_adaptive_threshold(method, block_size, c)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.erode(binary_image, kernel, iterations=1)
        return result_image

    def apply_dilation_adaptive(self, method="mean", block_size=11, c=2, kernel_size=5):
        binary_image = self.apply_adaptive_threshold(method, block_size, c)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result_image = cv2.dilate(binary_image, kernel, iterations=1)
        return result_image


if __name__ == "__main__":
    cv = MyOpenCv()
    cv.show_image(cv.image)

    kernel_sharpen = np.array([[-1.0, -1.0, -1.0],
                               [-1.0,  9.0, -1.0],
                               [-1.0, -1.0, -1.0]], dtype=np.float32)

    kernel_emboss = np.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [0, 1, 2]], dtype=np.float32)

    # Image generating
    image_linear_filter_sharpen = cv.apply_linear_filter(kernel_sharpen)
    image_linear_filter_emboss = cv.apply_linear_filter(kernel_emboss)

    image_blur = cv.apply_blur(method="blur", kernel_size=11)
    image_blur_gaussian = cv.apply_blur(method="GaussianBlur", kernel_size=11)
    image_blur_median = cv.apply_blur(method="medianBlur", kernel_size=11)

    image_binary = cv.apply_threshold(threshold=127, max_val=255, thresh_type=cv2.THRESH_BINARY)
    image_erosion = cv.apply_erosion(kernel_size=5)
    image_dilation = cv.apply_dilation(kernel_size=5)

    image_opening = cv.apply_opening(kernel_size=5)
    image_closing = cv.apply_closing(kernel_size=5)
    image_gradient = cv.apply_gradient(kernel_size=5)

    image_binary_adaptive = cv.apply_adaptive_threshold(method="gaussian", block_size=11, c=2)
    image_erosion_adaptive = cv.apply_erosion_adaptive(method="gaussian", block_size=11, c=2, kernel_size=5)
    image_dilation_adaptive = cv.apply_dilation_adaptive(method="gaussian", block_size=11, c=2, kernel_size=5)

    # Image showing
    cv.show_image(image_linear_filter_sharpen, window_name="Linear filter (sharpen)")
    cv.show_image(image_linear_filter_emboss, window_name="Linear filter (emboss)")

    cv.show_image(image_blur, window_name="Blur")
    cv.show_image(image_blur_gaussian, window_name="Gaussian Blur")
    cv.show_image(image_blur_median, window_name="Median Blur")

    cv.show_image(image_binary, window_name="Binary image (threshold)")
    cv.show_image(image_erosion, window_name="Erosion")
    cv.show_image(image_dilation, window_name="Dilation")

    cv.show_image(image_opening, window_name="Opening")
    cv.show_image(image_closing, window_name="Closing")
    cv.show_image(image_gradient, window_name="Gradient")

    cv.show_image(image_binary_adaptive, window_name="Binary image (adaptive)")
    cv.show_image(image_erosion_adaptive, window_name="Erosion (adaptive)")
    cv.show_image(image_dilation_adaptive, window_name="Dilation (adaptive)")

    # Image saving
    cv.save_image(image_linear_filter_sharpen, 'image_linear_filter_sharpen.jpg')
    cv.save_image(image_linear_filter_emboss, 'image_linear_filter_emboss.jpg')

    cv.save_image(image_blur, 'image_blur.jpg')
    cv.save_image(image_blur_gaussian, 'image_blur_gaussian.jpg')
    cv.save_image(image_blur_median, 'image_blur_median.jpg')

    cv.save_image(image_binary, 'image_binary.jpg')
    cv.save_image(image_erosion, 'image_erosion.jpg')
    cv.save_image(image_dilation, 'image_dilation.jpg')

    cv.save_image(image_opening, "image_opening.jpg")
    cv.save_image(image_closing, "image_closing.jpg")
    cv.save_image(image_gradient, "image_gradient.jpg")

    cv.save_image(image_binary_adaptive, 'image_binary_adaptive.jpg')
    cv.save_image(image_erosion_adaptive, 'image_erosion_adaptive.jpg')
    cv.save_image(image_dilation_adaptive, 'image_dilation_adaptive.jpg')
