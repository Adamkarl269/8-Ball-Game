from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import random


lst = ["Yes", "No", "Without a doubt", "Certainly", "Can't predict now", "True", "False"]


class EightBallApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("8ball.kv")

    def response(self):
        self.root.ids.label_one.text = random.choice(lst)

        if self.root.ids.label_one.text == "Can't predict now":
            sound = SoundLoader.load("response.mp3")
            sound.play()
        elif self.root.ids.label_one.text == "False":
            sound = SoundLoader.load("response.mp3")
            sound.play()
        elif self.root.ids.label_one.text == "No":
            sound = SoundLoader.load("response.mp3")
            sound.play()
        elif self.root.ids.label_one.text == "Yes":
            sound = SoundLoader.load("response_positive_1.mp3")
            sound.play()
        elif self.root.ids.label_one.text == "Without a doubt":
            sound = SoundLoader.load("response_positive_1.mp3")
            sound.play()
        elif self.root.ids.label_one.text == "Certainly":
            sound = SoundLoader.load("response_positive_2.mp3")
            sound.play()
        elif self.root.ids.label_one.text == "True":
            sound = SoundLoader.load("response_positive_3.mp3")
            sound.play()

    def change_to_dark(self):
        self.theme_cls.theme_style = "Dark"

    def change_to_light(self):
        self.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    EightBallApp().run()
