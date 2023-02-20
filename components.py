from typing import Optional, Dict

import pygame as pg

from constants import Colors, FONT


class Font:
    def __init__(self, size: int, font: str = FONT):
        self.font = pg.font.Font(FONT, size)

    def render(self, text: str):
        ...


class Button:
    def __init__(self, text, pos, font_size, font_color, button_color, button_hover_color, bg_color=None, action=None):
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.button_color = button_color
        self.button_hover_color = button_hover_color
        self.bg_color = bg_color
        self.action = action
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        if self.bg_color:
            self.background = pg.Surface(self.rect.size)
            self.background.fill(self.bg_color)
            self.image.blit(self.background, (0, 0))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()

    def set_text(self, text):
        self.text = text
        if self.bg_color:
            self.background = pg.Surface(self.rect.size)
            self.background.fill(self.bg_color)
            self.image.blit(self.background, (0, 0))
        self.image = self.font.render(self.text, True, self.font_color)

    def set_pos(self, pos):
        self.pos = pos
        self.rect.topleft = self.pos

    def set_font_size(self, font_size):
        self.font_size = font_size
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        if self.bg_color:
            self.background = pg.Surface(self.rect.size)
            self.background.fill(self.bg_color)
            self.image.blit(self.background, (0, 0))

    def set_font_color(self, font_color):
        self.font_color = font_color
        self.image = self.font.render(self.text, True, self.font_color)
        if self.bg_color:
            self.background = pg.Surface(self.rect.size)
            self.background.fill(self.bg_color)
            self.image.blit(self.background, (0, 0))

    def set_button_color(self, button_color):
        self.button_color = button_color

    def set_button_hover_color(self, button_hover_color):
        self.button_hover_color = button_hover_color

    def set_bg_color(self, bg_color):
        self.bg_color = bg_color
        self.background = pg.Surface(self.rect.size)
        self.background.fill(self.bg_color)
        self.image.blit(self.background, (0, 0))

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def get_text(self):
        return self.text