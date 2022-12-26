import os
import sys

import pygame as pg


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Pizza Place')
    screen = pg.display.set_mode((1280, 720))
    running = True
    sprites = pg.sprite.Group()
    cursor = pg.sprite.Sprite(sprites)
    cursor.image = load_image("cursor.png")
    cursor.rect = cursor.image.get_rect()
    while running:
        screen.fill("#A4784B")
        pg.mouse.set_visible(False)
        if pg.mouse.get_focused():
            cursor.rect.x, cursor.rect.y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        if pg.mouse.get_focused():
            sprites.draw(screen)
        pg.display.flip()
    pg.quit()
