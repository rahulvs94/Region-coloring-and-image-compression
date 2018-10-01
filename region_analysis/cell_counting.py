import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randint

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        # 255 - white
        # 0 - black

        regions = dict()

        [rows, columns] = np.shape(image)
        new_region_image = np.pad(np.zeros((rows, columns), dtype=int), (1, 0), 'constant', constant_values=0)

        count = 0
        for i in range(rows):
            for j in range(columns):
                # print(regions)
                top = new_region_image[i, j+1]
                left = new_region_image[i+1, j]
                # new region
                if left == 0 and top == 0 and image[i, j] == 0:
                    count = count + 1
                    new_region_image[i+1, j+1] = count
                    regions[str(new_region_image[i+1, j+1])] = []
                    regions[str(new_region_image[i+1, j+1])].append((i, j))
                # assign same region as top
                elif left == 0 and top != 0 and image[i, j] == 0:
                    new_region_image[i+1, j+1] = top
                    regions[str(new_region_image[i + 1, j + 1])].append((i, j))
                # assign same region as left
                elif left != 0 and top == 0 and image[i, j] == 0:
                    new_region_image[i+1, j+1] = left
                    regions[str(new_region_image[i + 1, j + 1])].append((i, j))
                # if both are same
                elif left != 0 and top != 0 and left == top and image[i, j] == 0:
                    new_region_image[i+1, j+1] = left
                    regions[str(new_region_image[i + 1, j + 1])].append((i, j))
                # if top and left pixels belong to different regions, make them same
                elif left != 0 and top != 0 and left != top and image[i, j] == 0:
                    new_region_image[i+1, j+1] = top    # current
                    new_region_image[i+1, j] = top      # left
                    regions[str(new_region_image[i+1, j+1])].append((i, j))
                    regions[str(new_region_image[i+1, j+1])].extend(regions[str(left)])
                    regions[str(left)].clear()

        for i in range(1, len(regions)+1):
            if len(regions[str(i)]) == 0:
                regions.pop(str(i))

        # number of regions
        print("\nNumber of regions: ", len(regions))
        # remove first row
        new_region_image = np.delete(new_region_image, 0, axis=0)
        # remove first column
        new_region_image = np.delete(new_region_image, 0, axis=1)

        # creating blob color image
        rgb_image = np.zeros((rows, columns, 3), dtype=int)

        for key in regions:
            # print("\n\nRegion ", key, regions[key])
            color = [randint(50, 255), randint(20, 255), randint(50, 255)]
            for values in regions[key]:
                rgb_image[values[0], values[1]] = color

        cv2.imwrite('rgb_image.png', rgb_image)

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        """region = {'1': [(1, 1), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                        (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)],
                  '2': [(2, 1), (2, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                        (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)],
                  '3': [(2, 1), (2, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                        (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)],
                  '4': [(2, 1), (2, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                        (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)],
                  '5': [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                        (1, 2), (1, 2)]}"""

        for key, value in list(region.items()):
            if len(value) < 15:
                region.pop(key)
        print("Number of regions after checking 15 pixels limit: ", len(region))

        stats = region
        for key, value in list(region.items()):
            area = len(value)
            Xc, Yc = (1 / area) * np.sum(value, axis=0)
            centroid = (np.uint8(Xc), np.uint8(Yc))
            stats[key] = []
            stats[key].append(centroid)
            stats[key].append(area)
        # print(stats)

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        comp_image = np.uint8(255 - image)
        print("Type of negative image", type(comp_image))

        for key, value in list(stats.items()):
            centroid = value[0]
            area = value[1]
            cv2.putText(comp_image, '.' + str(key) + ',' + str(area), (centroid[1], centroid[0]), cv2.FONT_HERSHEY_DUPLEX, 0.3, 80)
            # print("Centroid: ", centroid)

        return comp_image
