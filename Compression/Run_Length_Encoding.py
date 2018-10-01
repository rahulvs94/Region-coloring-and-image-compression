import numpy as np

class rle:

    def encode_image(self, binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        rle_list = []
        [rows, columns] = np.shape(binary_image)
        for i in range(rows):
            a = binary_image[i, 0]
            rle_list.append(str(binary_image[i, 0]))
            c = 0
            for j in range(columns):
                if binary_image[i, j] == a:
                    c = c + 1
                else:
                    rle_list.append(c)
                    c = 1
                    a = binary_image[i, j]
            rle_list.append(c)

        print("length of rle: ", len(rle_list))

        return rle_list

    def decode_image(self, rle_code, height, width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """

        temp = []
        for i in range(len(rle_code)):
            if rle_code[i] == '255':
                a = 1
            elif rle_code[i] == '0':
                a = 0
            else:
                if a == 1:
                    temp.append(255 * np.ones(rle_code[i]))
                    a = 0
                else:
                    temp.append(np.zeros(rle_code[i]))
                    a = 1

        decoded = [item for sublist in temp for item in sublist]
        print("length of decoded: ", len(decoded))

        return np.array(decoded).reshape(height, width)
