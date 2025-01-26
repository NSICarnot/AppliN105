import os

from PIL import Image
from customtkinter import CTkImage

def resize_image(img_path: str, width: int, height: int) -> Image:
    """
    Resize an image to the specified width and height
    :param img_path: Path to the image
    :param width: New width of the image
    :param height: New Height of the image
    :return: Resized image as a PIL Image object
    """
    try:
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"File {img_path} does not exist")
        img = Image.open(img_path)
        img.thumbnail((width, height))
        return img
    except Exception as e:
        print(f"Error while resizing image: {e}")
        return Image.new('RGB', (width, height))


def open_image(img_path: str) -> Image:
    """
    Open an image from the specified path
    :param img_path: Path to the image
    :return: Image as a PIL Image object
    """
    try:
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"File {img_path} does not exist")
        return Image.open(img_path)
    except Exception as e:
        print(f"Error while opening image: {e}")
        return Image.new('RGB', (50, 50))


def tk_CTkImage(img: Image, width: int, height: int, *, image_dark=None) -> CTkImage:
    """
    Create a CTkImage object from a PIL Image object
    :param img: Image to convert
    :param width: Desired width
    :param height: Desired height
    :param image_dark: Optional dark image for dark mode
    :return: CTkImage object
    """
    return CTkImage(img, size=(width, height)) if image_dark is None else CTkImage(light_image=img, size=(width, height), dark_image=image_dark)
