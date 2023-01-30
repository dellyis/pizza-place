from typing import Optional, Dict

import pygame as pg

from constants import Colors, FONT


class Font:
    def __init__(self, size: int, font: str = FONT):
        self.font = pg.font.Font(FONT, size)

    def render(self, text: str):
        ...


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, fill: Optional[Dict[str, hex]] = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        if not fill:
            fill = {"normal": Colors.primary}

        self.fill = fill

        self.surface = pg.Surface((self.width, self.height))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def on_click(self):
        ...
