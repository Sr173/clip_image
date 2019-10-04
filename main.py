import cv2
import os
import numpy as np

pic_list = [
    [2, 5, 8],
    [2, 3, 5, 8],
    [1, 2, 5, 8],
    [2, 5, 8],
    [2, 5, 6, 8],
    [2, 4, 5, 8],
    [2, 5, 8],
    [2, 5, 8, 9],
    [2, 5, 8, 7],
]

print(pic_list.__len__())
for fpath, dirname, fnames in os.walk("./pic/"):
    pic_name_list = fnames

for i in range(len(pic_name_list)):
    pic_name_list[i] = "./pic/" + pic_name_list[i]

print(pic_name_list)

count = 0

for i in range(len(pic_list)):
    blank_image = np.zeros((900, 900, 3), np.uint8)
    blank_image[::] = 255
    for j in pic_list[i]:
        j = j - 1
        img = cv2.imread(pic_name_list[count])
        count += 1
        height, width, _ = img.shape

        if height < width:
            start = int((width - height) / 2)
            img = img[:, start:start + height]
        else:
            start = int((height - width) / 2)
            img = img[start:start + width, :]
        img = cv2.resize(img, (300, 300), )

        print(height, width)
        x = j % 3
        y = int(j / 3)
        blank_image[y * 300: (y + 1) * 300, x * 300: (x + 1) * 300] = img
        cv2.imshow("Image", blank_image)
        cv2.waitKey(0)
        cv2.imwrite("image/" + str(i) + ".jpg", blank_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
