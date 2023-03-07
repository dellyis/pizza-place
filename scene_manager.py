import inspect
from typing import Dict, Optional

import pygame as pg

from components import Button
from constants import Colors, FONT


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
        self.button = Button("Start!", (640, 320), 32, Colors.light, Colors.primary,
                             lambda: scene_manager.change_scene("ClickerScene"))
        self.button.set_pos(((1280 - self.button.width) // 2, (720 - self.button.height) // 2))

    def draw(self):
        title_font = pg.font.Font(FONT, 128)

        self.screen.fill(Colors.warning)
        self.screen.blit(title_font.render("Pizza Place", True, "#485696"),
                         ((1280 - title_font.size("Pizza Place")[0]) // 2, 100))

        self.button.draw(self.screen)

    def handle_events(self, event):
        self.button.handle_event(event)


class ClickerScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.button = Button("Click!", (640, 360), 32, (255, 255, 255), (0, 0, 255), lambda: print("click"))
        self.button.set_pos(((1280 - self.button.width) // 2, (720 - self.button.height) // 2))

        self.stop = Button("Stop", (0, 0), 32, (255, 255, 255), (0, 0, 255),
                           lambda: scene_manager.change_scene("ResultScene"))

    def draw(self):
        title_font = pg.font.Font(FONT, 128)

        self.screen.fill("#A4784B")
        self.screen.blit(title_font.render("Собери пиццу", True, "#485696"),
                         ((1280 - title_font.size("Собери пиццу")[0]) // 2, 100))

        self.button.draw(self.screen)

    def handle_events(self, event):
        self.button.handle_event(event)


class ResultScene(BaseScene):
    # TODO: fill the scene
    ...


class SceneManager:
    def __init__(self):
        """
        Класс, отвечающий за сцены
        """
        self.scenes: Dict[str, BaseScene] = {}
        self.current_scene: Optional[BaseScene] = None

    def register(self, scene: BaseScene):
        """
        Регистрация ново сцены

        :param scene: сцена
        """
        if not isinstance(scene, BaseScene):
            raise TypeError("Сцена должна наследоваться от класса BaseScene")
        if scene in self.scenes:
            raise ValueError("Сцена уже добавлена")
        self.scenes[scene.__class__.__name__] = scene

    def change_scene(self, name: str, *args, **kwargs):
        """
        Изменить текущую строку

        :param name: название сцены
        """
        if not self.scenes:
            raise Exception("Нет добавленных сцен")
        if name not in self.scenes:
            raise ValueError("Указанной сцены не существует")
        self.current_scene = self.scenes[name]

    def draw(self):
        """
        Отрисовать текущую сцену
        """
        if not self.current_scene:
            raise Exception("Не выбрана текущая сцена")
        self.current_scene.draw()

    def handle_events(self, event):
        """
        Обработать событие на сцене

        :param event: событие
        """
        if not self.current_scene:
            raise Exception("Не выбрана текущая сцена")
        self.current_scene.handle_events(event)


def register_scenes(screen):
    """
    Зарегистрировать все сцены

    :param screen: поверхность
    """
    for name, cls in inspect.getmembers(inspect.getmodule(inspect.currentframe()), inspect.isclass):
        if name != "BaseScene" and issubclass(cls, BaseScene):
            scene_manager.register(cls(screen))


scene_manager = SceneManager()
