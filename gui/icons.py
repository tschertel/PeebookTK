# from pathlib import Path

# import ttkbootstrap as ttk

from PIL import Image, ImageTk

appicon_small = my_img = ImageTk.PhotoImage(Image.open("gui/icons/ebook_32.png"))

"""
Initial work on icons

"""
""" image_files = {
    "appicon_small": "ebook_32.png",
    "appicon_big": "ebook_64.png",
}

photoimages = []
imgpath = Path(__file__).parent / "icons"
for key, val in image_files.items():
    _path = imgpath / val
    photoimages.append(ttk.PhotoImage(name=key, file=_path))
 """
