from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.button import Label


class FloatLayout(FloatLayout):
    Window.clearcolor = (255, 255, 255, 255)
    pass


class Start(App):

    def build(self):
        layout = FloatLayout()

        text = Label(text="Choose what application you want to start.",
                    font_size = '20sp',
                    color=(0,0,0),
                    pos=(0, 100)
                    )

        btn = Button(text="BMI calculator",
                     font_size='20',
                     color=(0, 0, 0),
                     size_hint=(.4, .1),
                     width=200,
                     height=100,
                     pos=(220, 200)
                     )

        btn2 = Button(text="JSON file",
                     font_size='20',
                     color=(0, 0, 0),
                     size_hint=(.4, .1),
                     width=200,
                     height=100,
                     pos=(220, 100)
                     )

        btn.bind(on_press=self.BmiPress)
        btn2.bind(on_press=self.JsonPress)

        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(text)

        return layout

    def BmiPress(self, event):
        App.get_running_app().stop()
        from calculator import kivybmi
        Window.close()

    def JsonPress(self, event):
        App.get_running_app().stop()
        from list import peoplefile
        Window.close()


root = Start()
root.run()