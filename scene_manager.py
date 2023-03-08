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
                             lambda: scene_manager.change_scene("ClickerScene"))
        self.button.set_pos(((1280 - self.button.width) // 2, 400))
        self.upgrades = Button("Бонусы", (640, 320), 32, Colors.light, Colors.primary,
                               lambda: scene_manager.change_scene("UpgradeScene"))
        self.upgrades.set_pos(((1280 - self.upgrades.width) // 2, 480))

    def draw(self):
        self.screen.fill(Colors.secondary)

        title = Label("Пиццерия", (1280 // 2, 200), 128, Colors.info)
        title.set_pos(((1280 - title.width) // 2, 200))
        title.draw(self.screen)

        Label(f"Монеты: {data.money}", (25, 650), 32, Colors.warning).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

        self.button.draw(self.screen)
        self.upgrades.draw(self.screen)

    def handle_events(self, event):
        self.button.handle_event(event)
        self.upgrades.handle_event(event)

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

        Label(f"Монеты: {data.money}", (25, 650), 32, Colors.warning).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

    def handle_events(self, event):
        self.click.handle_event(event)

    def money_inc(self):
        if not self.end_day:
            self.end_day = time() + 60
        dlt = (1 + 2 * data.data.upgrades.cheesy_crust + 3 * data.data.upgrades.pepperoni_power + 5 * data.data.upgrades.mega_meal) * \
              (1 + 0.1 * data.data.upgrades.extra_cheese) * (1 + 0.2 * data.data.upgrades.speedy_delivery) * \
              (1 + 0.3 * data.data.upgrades.mighty_meat) * (1 + 0.5 * data.data.upgrades.supreme_slice)
        self.money = round(self.money + dlt, 2)
        data.data.money = round(data.money + dlt, 2)


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

        Label(f"Монеты: {data.money}", (25, 650), 32, Colors.warning).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

        self.button.draw(self.screen)

    def handle_events(self, event):
        self.button.handle_event(event)

    def on_change(self, money):
        self.money = money


class UpgradeScene(BaseScene):
    def __init__(self, screen):
        super().__init__(screen)

        self.upgrades = (
            ("extra_cheese", "Дополнительный сыр (+10% монет за клик)", 200),
            ("speedy_delivery", "Быстрая доставка (+20% монет за клик)", 500),
            ("mighty_meat", "Могучее мясо (+30% монет за клик)", 1000),
            ("supreme_slice", "Высший ломтик (+50% монет за клик)", 1500),
            ("cheesy_crust", "Сырная корочка (+2 монеты за клик)", 2000),
            ("pepperoni_power", "Сила пепперони (+3 монеты за клик)", 3000),
            ("mega_meal", "Мега мясо (+5 монет за клик)", 5000),
        )

        self.back = Button(" < ", (25, 100), 32, Colors.light, Colors.primary,
                           lambda: scene_manager.change_scene("HomeScene"))

    def draw(self):
        self.screen.fill(Colors.secondary)

        for index, (name, display_name, price) in enumerate(self.upgrades):
            setattr(self, name,
                    Button(str(price + (price // 2) * getattr(data.data.upgrades, name)), (1000, 150 + 65 * index), 20,
                           Colors.light, Colors.success if price + (price // 2) * getattr(data.data.upgrades,
                                                                                          name) <= data.money
                           else Colors.danger, self.buy(name, price)))
            getattr(self, name).draw(self.screen)
            Label(display_name + f" ({getattr(data.data.upgrades, name)})", (350, 150 + 65 * index), 20, Colors.light).draw(
                self.screen)

        Label(f"Монеты: {data.money}", (25, 650), 32, Colors.warning).draw(self.screen)
        Label(f"День {data.day}", (25, 25), 32, Colors.warning).draw(self.screen)

        title = Label("Бонусы", (640, 100), 100, Colors.info)
        title.set_pos(((1280 - title.width) // 2, 2))
        title.draw(self.screen)

        self.back.draw(self.screen)

    def handle_events(self, event):
        for name, *_ in self.upgrades:
            getattr(self, name).handle_event(event)
        self.back.handle_event(event)

    def buy(self, name, price):
        def func():
            now_level = getattr(data.data.upgrades, name)
            if price + (price // 2) * now_level <= data.money:
                setattr(data.data.upgrades, name, now_level + 1)
                data.data.money -= price + (price // 2) * now_level
                data.save()

        return func


class SceneManager:
    def __init__(self):
        """
        Класс, отвечающий за сцены
        """
        self.scenes: Dict[str, BaseScene] = {}
        self.current_scene: Optional[BaseScene] = None

    def register(self, scene: BaseScene):
        """
        Регистрация новой сцены

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
