import pygame
import sys
import os
IMG_ScalingRegulation=1.0
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_img(file_name):
    img=pygame.image.load(resource_path(file_name))
    img = pygame.transform.scale(img, (int(img.get_width() * IMG_ScalingRegulation), int(img.get_height() * IMG_ScalingRegulation)))
    return img

def open_file(file_name):
    return open(resource_path(file_name))


pygame.init()
