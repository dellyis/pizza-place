import pygame as pg

from constants import FONT


class Button:
    def __init__(self, text, pos, font_size, font_color, button_color, action=None):
        """
        Компонент кнопки, позволяющий легко взаимодействовать с ней

        :param text: отображаемый текст
        :param pos: позиция
        :param font_size: размер текста
        :param font_color: цвет текста
        :param button_color: цвет кнопки
        :param action: функция, выполняемая при нажатии
        """
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.button_color = button_color
        self.action = action
        self.font = pg.font.Font(FONT, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.rect.inflate_ip(30, 30)

    @property
    def width(self) -> int:
        """
        Ширина кнопки
        """
        return self.rect.width

    @property
    def height(self):
        """
        Высота кнопки
        """
        return self.rect.height

    def draw(self, surface):
        """
        Отрисовать кнопку

        :param surface: поверхность
        """
        pg.draw.rect(surface, self.button_color, self.rect, border_radius=15)
        text_rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, text_rect)

    def handle_event(self, event):
        """
        Обработчик событий

        :param event: событие
        """
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()

    def set_text(self, text):
        """
        Изменить текст на кнопке

        :param text: новый текст
        """
        self.text = text
        self.image = self.font.render(self.text, True, self.font_color)

    def set_pos(self, pos):
        """
        Изменить позицию кнопки

        :param pos: новая позиция
        """
        self.pos = pos
        self.rect.topleft = self.pos

    def set_font_size(self, font_size):
        """
        Изменить размер текста

        :param font_size: новый размер
        """
        self.font_size = font_size
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)

    def set_font_color(self, font_color):
        """
        Изменить цвет текста

        :param font_color: новый цвет
        """
        self.font_color = font_color
        self.image = self.font.render(self.text, True, self.font_color)

    def set_button_color(self, button_color):
        """
        Изменить цвет кнопки

        :param button_color: новый цвет
        """
        self.button_color = button_color


class Label:
    def __init__(self, text, pos, font_size, font_color):
        """
        Компонент надписи

        :param text: текст
        :param pos: позиция
        :param font_size: размер текста
        :param font_color: цвет текста
        """
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.font = pg.font.Font(FONT, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    @property
    def width(self):
        """
        Ширина надписи
        """
        return self.rect.width

    @property
    def height(self):
        """
        Высота надписи
        """
        return self.rect.height

    def draw(self, surface):
        """
        Отрисовать надпись

        :param surface: поверхность
        """
        surface.blit(self.image, self.rect)

    def set_text(self, text):
        """
        Изменить текст

        :param text: новый текст
        """
        self.text = text
        self.image = self.font.render(self.text, True, self.font_color)

    def set_pos(self, pos):
        """
        Изменить позицию надписи

        :param pos: новая позиция
        """
        self.pos = pos
        self.rect.topleft = self.pos

    def set_font_size(self, font_size):
        """
        Изменить размер текста

        :param font_size: новый размер
        """
        self.font_size = font_size
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)

    def set_font_color(self, font_color):
        """
        Изменить цвет текста

        :param font_color: новый цвет
        """
        self.font_color = font_color
        self.image = self.font.render(self.text, True, self.font_color)
