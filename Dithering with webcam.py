from PIL import Image
import numpy as np
from numba import jit
import cv2


@jit
def Dither_c(img):
    for i in range(3):
        for x in range(len(img)):
            for y in range(len(img[0])):
                prev = img[x][y][i]
                next = round(prev / 255) * 255
                img[x][y][i] = next
                quant = prev - next
                img[x + 1][y][i] += quant * 7 / 16
                img[x - 1][y + 1][i] += quant * 3 / 16
                img[x][y + 1][i] += quant * 5 / 16
                img[x + 1][y + 1][i] += quant * 1 / 16
    return img


@jit
def Dither_g(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            prev = img[x][y]
            next = round(prev / 255) * 255
            img[x][y] = next
            quant = prev - next
            img[x + 1][y] += quant * 7 / 16
            img[x - 1][y + 1] += quant * 3 / 16
            img[x][y + 1] += quant * 5 / 16
            img[x + 1][y + 1] += quant * 1 / 16
    return img


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("f",type=str,default ="dogs.jpg",help="file name; image to be dithered")
    # parser.add_argument("c",type=str,default ="LA",help="color mode of output; RGB;LA for greyscale")
    # args = parser.parse_args()

    video = cv2.VideoCapture(0)
    exited = False
    while not exited:
        ret, img = video.read()
        cv2.imshow("before", img)
        img = Dither_c(img)
        cv2.imshow("color", img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = Dither_g(img)
        cv2.imshow("grey", img)

        c = cv2.waitKey(1)
        if c == 27:
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
