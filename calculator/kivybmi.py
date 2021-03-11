from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


DEFAULTH = 180 #default height
DEFAULTW = 70  #default weight
DEFAULTA = 20  #default age
DEFAULTBMI = 21 #defult bmi

class FloatLayout(FloatLayout):
    Window.clearcolor = (255, 255, 255, 255)
    pass


class BmiBuild(App):

    def build(self):
        self.height = DEFAULTH
        self.weight = DEFAULTW
        self.age = DEFAULTA
        self.bmi = DEFAULTBMI
        return FloatLayout()

    def calculate(self, event):
        self.bmi = (self.weight / self.height / self.height)*10000
        bmifinal = round(self.bmi, 2)
        print(bmifinal)
        return bmifinal

    def enterHeight(self):
        height = self.root.ids.height.text
        print(height)
        if int(height) > 0:
            self.height = float(height)
        else:
            self.height = int(DEFAULTH)

    def enterWeight(self):
        weight = self.root.ids.weight.text
        print(weight)
        if int(weight) > 0:
            self.weight = float(weight)
        else:
            self.weight = int(DEFAULTW)

    def enterAge(self):
        age = self.root.ids.age.text
        print(age)
        if int(age) > 0:
            self.age = float(age)
        else:
            self.age = int(DEFAULTA)



root = BmiBuild()
root.run()