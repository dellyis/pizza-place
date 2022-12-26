import os
import sys

import pygame as pg

FONT = "./data/ProstoOne.ttf"

current_layout = "home"


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


if __name__ == '__main__':
    pg.init()
    pg.font.init()

    pg.display.set_caption('Pizza Place')
    screen = pg.display.set_mode((1280, 720))

    running = True

    cursor_sprite = pg.sprite.Group()

    cursor = pg.sprite.Sprite(cursor_sprite)
    cursor.image = load_image("cursor.png")
    cursor.rect = cursor.image.get_rect()

    sprites = pg.sprite.Group()

    menu_img = load_image("menu.png")

    while running:
        pg.mouse.set_visible(False)

        if current_layout == "home":
            title_font = pg.font.Font(FONT, 128)

            screen.fill("#A4784B")
            screen.blit(title_font.render("Pizza Place", True, "#485696"),
                        ((1280 - title_font.size("Pizza Place")[0]) // 2, 100))

            pg.draw.rect(screen, "#766771", (1100, 0, 100, 100))
            pg.draw.rect(screen, "#A3F7CB", (1105, 5, 90, 90))
            menu = pg.sprite.Sprite(sprites)
            menu.image = menu_img
            menu.rect = cursor.image.get_rect()
            menu.rect.x, menu.rect.y = 1118, 18

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if pg.mouse.get_focused():
            cursor.rect.x, cursor.rect.y = pg.mouse.get_pos()
            cursor_sprite.draw(screen)

        sprites.draw(screen)
        pg.display.flip()
    pg.quit()
