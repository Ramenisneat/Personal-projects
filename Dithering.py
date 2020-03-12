from PIL import Image
import numpy as np
from numba import jit

@jit
def Dither(img):
    for i in range(2):
        for x in range(len(img) - 1):
            for y in range(len(img[0]) - 1):
                prev = img[x][y][i]
                next = round(prev / 255) * 255
                img[x][y][i] = next
                quant = prev - next
                img[x + 1][y][i] += quant * 7 / 16
                img[x - 1][y + 1][i] += quant * 3 / 16
                img[x][y + 1][i] += quant * 5 / 16
                img[x + 1][y + 1][i] += quant * 1 / 16
    return img

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("f",type=str,default ="dogs.jpg",help="file name; image to be dithered")
    # parser.add_argument("c",type=str,default ="LA",help="color mode of output; RGB;LA for greyscale")
    # args = parser.parse_args()

    img = Image.open("dogs.jpg").convert("LA")  # args.f).convert(args.c)
    img = np.array(img)
    print("shape {}".format(img.shape))
    img = Dither(img)
    print("done")
    finished = Image.fromarray(img)
    finished.save("dithered1.png")


if __name__ == "__main__":
    main()
