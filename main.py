import os
from tkinter import Tk, Button, Label, filedialog
from PIL import Image


def convert_webp_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".webp"):
            webp_path = os.path.join(folder_path, filename)
            png_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.png")

            try:
                webp_image = Image.open(webp_path)
                png_image = webp_image.convert("RGBA")
                png_image.save(png_path)
                print(f"Converted {filename} to PNG.")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_webp_to_png(folder_path)
        label.config(text=f"Conversion completed for folder: {folder_path}")


root = Tk()
root.title("WebP to PNG Converter")

label = Label(root, text="Select a folder to convert WebP files to PNG")
label.pack(pady=10)

button = Button(root, text="Select Folder", command=select_folder)
button.pack(pady=10)

root.mainloop()
