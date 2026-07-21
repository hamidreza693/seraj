from kivy.properties import NumericProperty
from kivymd.uix.screen import MDScreen

from utils.storage import load_count, save_count
from utils.persian import fa


class MainScreen(MDScreen):

    count = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = load_count()

    @property
    def title(self):
        return fa("سراج")

    @property
    def subtitle(self):
        return fa("ذکر صلوات")

    @property
    def reset_text(self):
        return fa("از صفر")

    def increment(self):
        self.count += 1
        save_count(self.count)

    def reset_counter(self):
        self.count = 0
        save_count(self.count)