import os
import sys
import tkinter
import customtkinter
from tkinter import filedialog, messagebox
from PIL import Image

DEFAULT_SAVE_DIR = os.path.join(os.path.expanduser('~'), 'Desktop')

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x600")
app.title("WEBP Converter")


def convert_images(file_paths, save_dir, file_format):
    for path in file_paths:
        with Image.open(path) as img:
            file_name, file_ext = os.path.splitext(os.path.basename(path))
            new_file_name = f"{file_name}.{file_format.lower()}"
            new_file_path = os.path.join(save_dir, new_file_name)
            img.save(new_file_path, file_format)


def select_files():
    file_paths = filedialog.askopenfilenames(
        filetypes=[('Image Files', (
            '*.jpg', '*.jpeg', '*.png', '*.bmp', '*.raw', '*.tiff', '*.gif', '*.NEF', '*.ARW', '*.CRW', '*.CR2',
            '*.CR3',
            '*.NRW', '*.RAF', '*.DNG', '*.RW2', '*.ORF', '*.DCR', '*.KDC'))],
        title="변환할 이미지들을 선택하세요")
    if file_paths:
        save_dir = filedialog.askdirectory(initialdir=DEFAULT_SAVE_DIR, title="저장위치를 지정하세요")
        if save_dir:
            convert_images(file_paths, save_dir, "WEBP")

            messagebox.showinfo("변환완료", "변환 완료되었습니다.")


select_btn = customtkinter.CTkButton(master=app, text="이미지 선택", command=select_files)
select_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

icon_file = os.path.join(bundle_dir, 'icon.ico')
if os.path.exists(icon_file):
    app.iconbitmap(icon_file)

app.mainloop()
