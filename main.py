import os
import random
import mysql.connector

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file('screen_manager.kv')


class HomeWindow(Screen):
    def exit(self):
        App.get_running_app().stop()


class GameWindow(Screen):
    class TileButton(Button):
        foundPair = False
        image = StringProperty(None)
        background = ObjectProperty(None)
        background_hidden = ObjectProperty(None)
        background_normal = ObjectProperty(None)

        def on_image(self, instance, value):
            if self.background_normal is None:
                self.background_normal = value
                self.background = value
                self.background_hidden = self.background_down

        def on_press(self):
            if not self.foundPair:
                if self.parent.firstItem is None:
                    self.parent.firstItem = self
                    self.background_down, self.background_normal = self.background_normal, self.background_down
                else:
                    if self is self.parent.firstItem:
                        self.parent.firstItem = None
                    elif self.parent.firstItem.image == self.image:
                        #találtunk egy párt
                        self.parent.itemsLeft += 1

                        self.background_down, self.background_normal = self.background, self.background
                        self.parent.firstItem.background_down, self.parent.firstItem.background_normal = self.parent.firstItem.background, self.parent.firstItem.background
                        self.foundPair = True
                        self.parent.firstItem.foundPair = True
                        self.parent.firstItem = None

                        if self.parent.itemsLeft == len(self.parent.items) / 2:
                            #megtaláltuk az összes párt, azaz nyertünk
                            Clock.unschedule(self.parent.clock_callback)
                            self.parent.show_game_over_popup()

                    else:
                        self.parent.firstItem.background_down, self.parent.firstItem.background_normal = self.parent.firstItem.background_normal, self.parent.firstItem.background_down
                        self.parent.firstItem = None

    class TileGridLayout(GridLayout):

        def __init__(self, **kwargs):
            super().__init__()
            self.rows = kwargs["rows"]
            self.cols = kwargs["cols"]
            self.spacing = kwargs["spacing"]
            self.firstItem = None
            self.itemsLeft = 0
            self.elapsedSeconds = 0
            self.items = kwargs["items"]

        def toggle_buttons(self):
            for i in self.children:
                i.background_down, i.background_normal = i.background_normal, i.background_down

        def clock_callback(self, dt):
            self.elapsedSeconds += 1
            m, s = divmod(self.elapsedSeconds, 60)
            h, m = divmod(m, 60)
            time_text = "Eltelt idő: {:02d}:{:02d}:{:02d}".format(h, m, s)
            elapsed_time_label = self.parent.parent.parent.ids["elapsed_time_label"]
            elapsed_time_label.text = time_text

        def reset_clock(self):
            Clock.unschedule(self.clock_callback)

        def show_game_over_popup(self):
            m, s = divmod(self.elapsedSeconds, 60)
            h, m = divmod(m, 60)
            your_time_text = "Az időd: {:02d}:{:02d}:{:02d}".format(h, m, s)

            time_text = "{:02d}:{:02d}:{:02d}".format(h, m, s)

            box = BoxLayout()
            box.orientation = "vertical"
            box.padding = [80, 20, 80, 20]
            box.spacing = 20

            box.add_widget(Label(text=your_time_text, font_size=28))
            box.add_widget(Label(text="Gratulálok, nyertél, add meg a neved.", font_size=28))

            username_input = TextInput()
            username_input.size_hint = (1, 0.3)
            box.add_widget(username_input)

            validation_label = Label()
            validation_label.text = ""
            validation_label.font_size = 18
            validation_label.color = (0.78, 0.13, 0.21, 1)
            box.add_widget(validation_label)

            submit_button = Button()
            submit_button.text = "Mentés az adatbázisba"
            submit_button.size_hint = (1, 0.4)
            submit_button.background_normal = ""
            submit_button.background_color = (0.1, 0.5, 0.8, 1)

            #csúnya lambda függvény, talán egyszerűbben is meg lehet oldani?
            submit_button.on_press = lambda *args: self.validate_input_text(username_input.text, popup, validation_label, time_text, *args)

            box.add_widget(submit_button)
            popup = Popup(title="Vége a játéknak", content=box, auto_dismiss=False)
            popup.open()

        def show_db_insert_status_popup(self, text, color):
            box = BoxLayout()
            box.orientation = "vertical"
            box.padding = [30, 30, 30, 30]

            status_label = Label()
            status_label.text = text
            status_label.color = color
            status_label.font_size = 20

            box.add_widget(status_label)

            ok_button = Button()
            ok_button.text = "Ok"
            ok_button.background_normal = ""
            ok_button.background_color = (0.1, 0.5, 0.8, 1)
            ok_button.size_hint = (1, 0.4)
            ok_button.on_press = lambda *args: self.go_to_home_window(popup, *args)

            box.add_widget(ok_button)

            popup = Popup(title="Feltöltés az adatbázisba", content=box, auto_dismiss=False)
            popup.size_hint = (0.8, 0.8)
            popup.open()

        def go_to_home_window(self, popup: Popup):
            popup.dismiss()
            self.parent.parent.parent.parent.current = "homeWindow"

        def validate_input_text(self, input_text, popup: Popup, validation_label: Label, time_text):
            input_text = input_text.strip()
            if input_text:
                if len(input_text) > 20 or len(input_text) < 3:
                    validation_label.text = "A név legalább 3, maximum 20 karakter lehet!"
                else:
                    self.save_score_to_db(input_text, time_text, popup)
            else:
                validation_label.text = "A név nem lehet üres, illetve nem állhat pusztán szóközökből!"

        def save_score_to_db(self, name_text, time_text, popup: Popup):
            try:
                db = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="",
                    database="memorygamedb"
                )
                cursor = db.cursor()

                insert_statement = """
                    INSERT INTO highscore (name, time) 
                    VALUES (%s,%s)
                """

                cursor.execute(insert_statement, (name_text, time_text))
                db.commit()

                text = "Sikeres feltöltés!"
                color = (0.11, 0.56, 0, 1)
                popup.dismiss()
                self.show_db_insert_status_popup(text, color)

            except mysql.connector.Error as err:
                text = "Valami hiba történt a feltöltés során!"
                color = (0.78, 0.13, 0.21, 1)
                popup.dismiss()
                self.show_db_insert_status_popup(text, color)

    def get_images(self):
        tile_images = []
        for filename in os.listdir("images"):
            tile_images.append(os.path.join("images", filename))

        tile_images_copy = tile_images.copy()
        tile_images.extend(tile_images_copy)
        tile_images_copy.clear()

        return tile_images

    def start_game(self):
        tile_container = self.ids["tile_container"]
        images = self.get_images()
        grid_size = len(images)

        tile_grid_layout = self.TileGridLayout(rows=int(grid_size/2), cols=int(grid_size/2), spacing=10, items=images)
        tile_container.add_widget(tile_grid_layout)
        random.shuffle(images)
        for i in images:
            btn = self.TileButton(image=i)
            tile_grid_layout.add_widget(btn)
        tile_grid_layout.toggle_buttons()
        Clock.schedule_interval(tile_grid_layout.clock_callback, 1)

    def on_pre_enter(self, *args):
        self.start_game()

    def on_leave(self, *args):
        tile_container = self.ids["tile_container"]
        tile_container.children[0].reset_clock()
        tile_container.clear_widgets()

class HighscoreWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MemoryGameApp(App):
    def build(self):
        self.title = "Memóriajáték"
        self.icon = "icon.png"
        Window.minimum_width = 600
        Window.minimum_height = 550
        manager = WindowManager()
        return manager


MemoryGameApp().run()
