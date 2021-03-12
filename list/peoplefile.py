from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import json


class FloatLayout(FloatLayout):
    Window.clearcolor = (255, 255, 255, 255)
    pass


class ListBuild(App):

    def build(self):
        Window.clearcolor = (255, 255, 255, 255)
        layout = FloatLayout()
        #osobalayout = FloatLayout()

        with open('list/people.json', 'r') as file:
            data = file.read()
            parse = json.loads(data)


        y = 1
        jump = 100

        if len(parse) <= 6: #Z duvodu velikosti obrazovky je pocet limitovan na 6 osob
            number = len(parse)
        elif len(parse) > 6:
            number = 6

        for x in range(number):
            osoba_jmeno = Label(text=parse[str(y)]['name'],
                                font_size='15sp',
                                color=(0,0,0),
                                pos=(-250, jump)
                                )
            osoba_zeme = Label(text=parse[str(y)]['country'],
                                font_size='15sp',
                                color=(0,0,0),
                                pos=(-150, jump)
                                )
            osoba_hodnost = Label(text=parse[str(y)]['rank'],
                               font_size='15sp',
                               color=(0, 0, 0),
                               pos=(-50, jump)
                               )
            osoba_role = Label(text=parse[str(y)]['role'],
                                  font_size='15sp',
                                  color=(0, 0, 0),
                                  pos=(50, jump)
                                  )
            y += 1
            jump -= 50

            layout.add_widget(osoba_jmeno)
            layout.add_widget(osoba_zeme)
            layout.add_widget(osoba_hodnost)
            layout.add_widget(osoba_role)
            layout.add_widget(FloatLayout())

        #layout.add_widget(intro)
        return layout

root = ListBuild()
root.run()