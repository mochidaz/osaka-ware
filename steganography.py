import stegano
from PIL import Image
import stepic

from constants import *

def to_image(encryption, output):
    image = stegano.lsb.hide(Image.open(ENCODED_IMAGE_ONE), encryption)
    image.save(output)


def from_image(image):
    file = stegano.lsb.reveal(image)

    return file


def hide_data(encryption, output_image_path):
    carrier_image = Image.open(ENCODED_IMAGE_ONE)

    stego_image = stepic.encode(carrier_image, encryption)

    stego_image.save(output_image_path, format="PNG")


def reveal_data(stego_image_path):
    stego_image = Image.open(stego_image_path)

    hidden_data = stepic.decode(stego_image)

    return hidden_data
