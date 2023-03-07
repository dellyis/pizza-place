import pygame as pg

from scene_manager import HomeScene, ClickerScene, scene_manager, register_scenes

if __name__ == '__main__':
    pg.init()

    pg.display.set_caption('Pizza Place')
    screen = pg.display.set_mode((1280, 720))

    running = True

    register_scenes(screen)
    scene_manager.change_scene("HomeScene")

    sprites = pg.sprite.Group()

    while running:
        scene_manager.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            scene_manager.handle_events(event)

        sprites.draw(screen)
        pg.display.flip()
    pg.quit()
