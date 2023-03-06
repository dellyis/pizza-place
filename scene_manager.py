from typing import Dict, Optional

import pygame as pg

from constants import FONT
from utils import load_image


class BaseScene:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        ...  # Переопределяется для каждой сцены отдельно

    def handle_events(self, event):
        ...  # Переопределяется для каждой сцены отдельно


class HomeScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.sprites = pg.sprite.Group()

    def draw(self):
        title_font = pg.font.Font(FONT, 128)

        self.screen.fill("#A4784B")
        self.screen.blit(title_font.render("Pizza Place", True, "#485696"),
                         ((1280 - title_font.size("Pizza Place")[0]) // 2, 100))


class SceneManager:
    def __init__(self):
        self.scenes: Dict[str, BaseScene] = {}
        self.current_scene: Optional[BaseScene] = None

    def add(self, scene: BaseScene):
        if not isinstance(scene, BaseScene):
            raise TypeError("Сцена должна наследоваться от класса BaseScene")
        if scene in self.scenes:
            raise ValueError("Сцена уже добавлена")
        self.scenes[scene.__class__.__name__] = scene

    def change_scene(self, name: str):
        if not self.scenes:
            raise Exception("Нет добавленных сцен")
        if name not in self.scenes:
            raise ValueError("Указанной сцены не существует")
        self.current_scene = self.scenes[name]

    def draw(self):
        if not self.current_scene:
            raise Exception("Не выбрана текущая сцена")
        self.current_scene.draw()

    def handle_events(self, event):
        if not self.current_scene:
            raise Exception("Не выбрана текущая сцена")
        self.current_scene.handle_events(event)
