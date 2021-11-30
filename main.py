from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file('screen_manager.kv')


class GameWindow(Screen):
    pass


class HighscoreWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MemoryGameApp(App):
    def build(self):
        self.title = "Memóriajáték"
        self.icon = "icon.png"
        manager = WindowManager()
        return manager


MemoryGameApp().run()
