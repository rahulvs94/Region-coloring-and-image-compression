import numpy as np
import cv2

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        # in-built function to calculate histogram
        print("size of image: ", np.shape(image))
        print("number of pixels: ", np.shape(image)[0] * np.shape(image)[1])
        # hist1 = np.ravel(cv2.calcHist([image], [0], None, [256], [0, 256]))
        # hist = np.ravel(cv2.calcHist([image], [0], None, [256], [0, 256]))

        # created function to calculate histogram
        hist = np.zeros(256)
        [rows, columns] = np.shape(image)
        for k in range(256):
            count = 0
            for i in range(rows):
                for j in range(columns):
                    if image[i, j] == k:
                        count = count + 1
                hist[k] = count

        # print("Check if histogram is same: ", np.array_equal(hist, hist1))

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        # print("number of pixels using sum: ", sum(hist))
        probability = np.array((1/sum(hist))*hist)
        expected_value = probability*np.array(range(256))
        # print("probability: \n", probability)
        # print("expected_value: \n", expected_value)

        threshold = len(hist)/2
        temp_threshold = 0

        while abs(threshold - temp_threshold) > 0.001:
            temp1 = []
            temp2 = []
            print("New threshold: ", threshold)
            for i in range(len(hist)):
                if i < threshold:
                    temp1.append(expected_value[i])
                else:
                    temp2.append(expected_value[i])
            mean1 = sum(temp1)
            print("mean1: \n", mean1)
            mean2 = sum(temp2)
            print("mean2: \n", mean2)
            temp_threshold = threshold
            threshold = (mean1+mean2)/2
            print("threshold: ", threshold)
            print("temp_threshold: ", temp_threshold)

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        [rows, columns] = np.shape(image)
        bin_img = np.zeros((rows, columns), dtype=int)
        print("############## Using to binarize an image ##############")
        hist = self.compute_histogram(image)
        threshold = self.find_optimal_threshold(hist)
        for i in range(rows):
            for j in range(columns):
                if image[i, j] < threshold:
                    bin_img[i, j] = 0
                else:
                    bin_img[i, j] = 255
        # print("binary image: \n", bin_img)

        return bin_img