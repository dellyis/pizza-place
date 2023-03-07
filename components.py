import pygame as pg


class Button:
    def __init__(self, text, pos, font_size, font_color, button_color, action=None):
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.button_color = button_color
        self.action = action
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.rect.inflate_ip(30, 30)

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def draw(self, surface):
        pg.draw.rect(surface, self.button_color, self.rect, border_radius=15)
        text_rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, text_rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.font_color)

    def set_pos(self, pos):
        self.pos = pos
        self.rect.topleft = self.pos

    def set_font_size(self, font_size):
        self.font_size = font_size
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)

    def set_font_color(self, font_color):
        self.font_color = font_color
        self.image = self.font.render(self.text, True, self.font_color)

    def set_button_color(self, button_color):
        self.button_color = button_color


class Label:
    def __init__(self, text, pos, font_size, font_color):
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.font_color)

    def set_pos(self, pos):
        self.pos = pos
        self.rect.topleft = self.pos

    def set_font_size(self, font_size):
        self.font_size = font_size
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)

    def set_font_color(self, font_color):
        self.font_color = font_color
        self.image = self.font.render(self.text, True, self.font_color)
