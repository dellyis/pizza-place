import os
import sys

import pygame as pg


def load_image(name):
    """
    Загрузка изображения

    :param name: название изображения
    """
    fullname = os.path.join("data", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    return pg.image.load(fullname)
