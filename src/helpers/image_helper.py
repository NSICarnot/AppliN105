import os

from PIL import ImageTk, Image


def resize_image(img_path: str, width: int, height: int) -> Image:
    try:
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"File {img_path} does not exist")
        img = Image.open(img_path)
        img.thumbnail((width, height))
        return img
    except Exception as e:
        print(f"Error while resizing image: {e}")
        return Image.new('RGB', (width, height))


def to_ImageTk(img: Image) -> ImageTk.PhotoImage:
    return ImageTk.PhotoImage(img)
