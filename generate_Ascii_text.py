#!/usr/bin/env python3
from PIL import Image

#ASCII_CHARS = "Ñ@#W$98765.3210?!abc;:+=-,._ "
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width and height
def resize_image(image, new_width=100, new_height=None):
    width, height = image.size
    if new_height is None:
        ratio = height / width
        new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=100, new_height=None):
    # give image path
    path = "./Untitled-5.jpg"
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return

    # convert image to ASCII
    image_data = pixels_to_ascii(
        grayify(resize_image(image, new_width, new_height)))

    # format
    pixel_count = len(image_data)
    ascii_text = "\n".join([image_data[index:(index+new_width)]
                           for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_text)

    # save result to "ascii_text.txt"
    with open("ascii_text.txt", "w") as f:
        f.write(ascii_text)


# run
main(new_width=150, new_height=100)
