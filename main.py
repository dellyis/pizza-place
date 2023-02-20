import pygame as pg

from components import Button
from scene_manager import SceneManager, HomeScene

if __name__ == '__main__':
    pg.init()
    pg.font.init()

    pg.display.set_caption('Pizza Place')
    screen = pg.display.set_mode((1280, 720))

    running = True

    scene_manager = SceneManager()
    scene_manager.add(HomeScene(screen))
    scene_manager.change_scene("HomeScene")

    sprites = pg.sprite.Group()

    button = Button("Start!", (100, 100), 32, (255, 255, 255), (0, 0, 255), (0, 255, 0), None,
                    lambda: print("clicked"))

    while running:
        scene_manager.draw()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            button.handle_event(event)

        sprites.draw(screen)
        button.draw(screen)
        pg.display.flip()
    pg.quit()
