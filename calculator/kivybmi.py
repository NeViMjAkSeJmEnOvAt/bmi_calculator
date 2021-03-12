from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


DEFAULTH = 180 #default height
DEFAULTW = 70  #default weight
DEFAULTA = 20  #default age
DEFAULTBMI = 21 #defult bmi

class FloatLayout(FloatLayout):
    bmi = 20
    Window.clearcolor = (255, 255, 255, 255)
    pass


class BmiBuild(App):

    def build(self):
        self.height = DEFAULTH
        self.weight = DEFAULTW
        self.age = DEFAULTA
        self.bmi = DEFAULTBMI
        return FloatLayout()

    def result(self, finalbmi):
            if finalbmi < 16:
                self.root.ids.label_result_bmi.text = "Severe Thinnes"
            elif finalbmi > 16 and finalbmi <= 17:
                self.root.ids.label_result_bmi.text = "Moderate Thinnes"
            elif finalbmi > 17 and finalbmi <= 18.5:
                self.root.ids.label_result_bmi.text = "Mild Thinnes"
            elif finalbmi > 18.5 and finalbmi <= 25:
                self.root.ids.label_result_bmi.text = "Normal"
            elif finalbmi > 25 and finalbmi <= 30:
                self.root.ids.label_result_bmi.text = "Qwerweight"
            elif finalbmi > 30 and finalbmi <= 35:
                self.root.ids.label_result_bmi.text = "Slightly Obese"
            elif finalbmi > 35 and finalbmi <= 40:
                self.root.ids.label_result_bmi.text = "Obese"
            else:
                self.root.ids.label_result_bmi.text = "Morbidly Obese"



    def calculate(self, event):
        self.bmi = (self.weight / self.height / self.height)*10000
        bmifinal = round(self.bmi, 2)
        self.root.ids.label_final_bmi.text = str(bmifinal)
        BmiBuild.result(self, bmifinal)
        print(bmifinal)
        return bmifinal

    def enterHeight(self):
        height = self.root.ids.height.text
        print(height)
        if height != '':
            self.height = int(height)
        else:
            self.height = DEFAULTH

    def enterWeight(self):
        weight = self.root.ids.weight.text
        print(weight)
        if weight != '':
            self.weight = int(weight)
        else:
            self.weight = DEFAULTW

    def enterAge(self):
        age = self.root.ids.age.text
        print(age)
        if age != '':
            self.age = int(age)
        else:
            self.age = DEFAULTA


root = BmiBuild()
root.run()