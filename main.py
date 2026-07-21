from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window

from ui.main_screen import MainScreen


# ثبت فونت وزیر
LabelBase.register(
    name="Vazir",
    fn_regular="assets/fonts/Vazirmatn-Regular.ttf"
)


class SerajApp(MDApp):

    def build(self):
        self.title = "Seraj"

        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"

        Window.clearcolor = (248/255, 242/255, 231/255, 1)

        Builder.load_file("kv/main.kv")

        return MainScreen()


if __name__ == "__main__":
    SerajApp().run()