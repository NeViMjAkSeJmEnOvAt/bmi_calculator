from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import json


class ListBuild(App):

    def build(self):
        Window.clearcolor = (255, 255, 255, 255)
        layout = FloatLayout()
        #osobalayout = FloatLayout()

        with open('list/people.json', 'r') as file:
            data = file.read()
            parse = json.loads(data)

        #####################################

        intro = Label(text="JSON extract, persons (max 6)",
                      font_size='35sp',
                      color=(0, 0, 0),
                      pos=(0, 250)
                      )
        jmeno = Label(text="Name: ",
                        font_size='20sp',
                        color=(0,0,0),
                        pos=(-250, 150)
                        )
        zeme = Label(text="Country:",
                      font_size='20sp',
                      color=(0, 0, 0),
                      pos=(-150, 150)
                      )
        hodnost = Label(text="Rank: ",
                      font_size='20sp',
                      color=(0, 0, 0),
                      pos=(-50, 150)
                      )
        role = Label(text="Role: ",
                      font_size='20sp',
                      color=(0, 0, 0),
                      pos=(50, 150)
                      )

        layout.add_widget(jmeno)
        layout.add_widget(zeme)
        layout.add_widget(hodnost)
        layout.add_widget(role)

        ######################################

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

        layout.add_widget(intro)
        return layout

root = ListBuild()
root.run()