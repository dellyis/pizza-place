import inspect
from time import time
from typing import Dict, Optional

from components import Button, Label
from constants import Colors
from db import data


class BaseScene:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pass  # Переопределяется для каждой сцены отдельно

    def handle_events(self, event):
        pass  # Переопределяется для каждой сцены отдельно

    def on_change(self, *args, **kwargs):
        pass  # Переопределяется для каждой сцены отдельно


class HomeScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.button = Button("Начать", (640, 320), 32, Colors.light, Colors.primary,
                             lambda: scene_manager.change_scene("ClickerScene" if data.day % 5 else "EventDayScene"))
        self.button.set_pos(((1280 - self.button.width) // 2, 400))

    def draw(self):
        self.screen.fill(Colors.secondary)

        title = Label("Пиццерия", (1280 // 2, 200), 128, Colors.info)
        title.set_pos(((1280 - title.width) // 2, 200))
        title.draw(self.screen)

        Label(f"Монеты: {data.money}", (25, 600), 32, Colors.warning).draw(self.screen)
        Label(f"Кристаллы: {data.gems}", (25, 650), 32, Colors.info).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

        self.button.draw(self.screen)

    def handle_events(self, event):
        self.button.handle_event(event)

    def on_change(self, new_day=False):
        if new_day:
            data.data.day += 1
            data.save()


class ClickerScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)

        self.click = Button("Тык", (640, 360), 32, Colors.light, Colors.primary, self.money_inc)
        self.click.set_pos(((1280 - self.click.width) // 2, 390 - self.click.height))

        self.end_day = None
        self.money = 0

    def draw(self):
        if self.end_day and time() > self.end_day:
            data.save()
            scene_manager.change_scene("ResultScene", money=self.money)
            self.end_day = None
            self.money = 0

        self.screen.fill(Colors.secondary)

        title = Label(f"Нажимайте! (осталось {round(self.end_day - time(), 1)}с)" if self.end_day else "Нажимайте!",
                      (0, 0), 128 - 64 * bool(self.end_day), Colors.info)
        title.set_pos(((1280 - title.width) // 2, 150))
        title.draw(self.screen)

        self.click.draw(self.screen)

        Label(f"Монеты: {data.money}", (25, 600), 32, Colors.warning).draw(self.screen)
        Label(f"Кристаллы: {data.gems}", (25, 650), 32, Colors.info).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

    def handle_events(self, event):
        self.click.handle_event(event)

    def money_inc(self):
        if not self.end_day:
            self.end_day = time() + 6
        delta = round(
            (1 + 2 * data.upgrades.cheesy_crust + 3 * data.upgrades.pepperoni_power + 5 * data.upgrades.mega_meal) *
            (1 + 0.1 * data.upgrades.extra_cheese) * (1 + 0.2 * data.upgrades.speedy_delivery) *
            (1 + 0.3 * data.upgrades.mighty_meat) * (1 + 0.5 * data.upgrades.supreme_slice), 2)
        self.money += delta
        data.data.money += delta


class EventDayScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.button = Button("Тык", (640, 360), 32, Colors.light, Colors.primary, )

    def draw(self):
        pass

    def handle_events(self, event):
        self.button.handle_event(event)


class ResultScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.money = None
        self.button = Button("В меню", (640, 320), 32, Colors.light, Colors.primary,
                             lambda: scene_manager.change_scene("HomeScene", new_day=True))
        self.button.set_pos(((1280 - self.button.width) // 2, 400))

    def draw(self):
        self.screen.fill(Colors.secondary)

        title = Label(f"Получено {self.money} монет", (1280 // 2, 200), 64, Colors.info)
        title.set_pos(((1280 - title.width) // 2, 250))
        title.draw(self.screen)

        Label(f"Монеты: {data.money}", (25, 600), 32, Colors.warning).draw(self.screen)
        Label(f"Кристаллы: {data.gems}", (25, 650), 32, Colors.info).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

        self.button.draw(self.screen)

    def handle_events(self, event):
        self.button.handle_event(event)
    
    def on_change(self, money):
        self.money = money


class UpgradeScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)

        self.extra_cheese = Button("Дополнительный сыр", (640, 320), 32, Colors.light, Colors.primary, None)
        self.speedy_delivery = Button("Быстрая доставка", (640, 320), 32, Colors.light, Colors.primary, None)
        self.sizzling_sausage = Button("Шипящая колбаса", (640, 320), 32, Colors.light, Colors.primary, None)
        self.mighty_meat = Button("Могучее мясо", (640, 320), 32, Colors.light, Colors.primary, None)
        self.supreme_slice = Button("Высший ломтик", (640, 320), 32, Colors.light, Colors.primary, None)
        self.cheesy_crust = Button("Сырная корочка", (640, 320), 32, Colors.light, Colors.primary, None)
        self.pepperoni_power = Button("Сила пепперони", (640, 320), 32, Colors.light, Colors.primary, None)
        self.mega_meal = Button("Мега мясо", (640, 320), 32, Colors.light, Colors.primary, None)


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
        self.current_scene.on_change(*args, **kwargs)

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
