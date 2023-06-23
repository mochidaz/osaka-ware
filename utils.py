import ctypes
import zipfile

from PIL import Image

from constants import *


def change_wallpaper():
    SPI_SETDESKWALLPAPER = 0x0014

    image_data = Image.open(ENCODED_IMAGE_ONE)

    pwd = os.getcwd()

    image_data.save("wallpaper-osaker.jpg")

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(pwd, "wallpaper-osaker.jpg"), 3)


def compress_file(file_path, zip_path, file_name):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=file_name)


def extract_file(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()

        for file_name in file_list:
            file_data = zip_ref.read(file_name)

            with open(extract_to, 'wb') as output_file:
                output_file.write(file_data)
