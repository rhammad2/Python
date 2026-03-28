from functools import reduce
from image_lib import Image

def blur(image):
    """Builds and returns a new image which is a blurred copy of the argument image."""

    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)

    new = image.clone()

    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)

            sums = reduce(tripleSum, [oldP, left, right, top, bottom])
            averages = tuple(map(lambda value: value // 5, sums))

            new.setPixel(x, y, averages)

    return new


def main():
    my_image = Image("smokey.gif")
    blurred_image = blur(my_image)
    blurred_image.save("smokey_blurred.png")
    blurred_image.draw()

if __name__ == "__main__":
    main()