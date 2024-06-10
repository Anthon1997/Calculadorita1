from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from math import sin, cos, tan, log, sqrt

class CalculatorLayout(BoxLayout):
    def append_display(self, value):
        if self.ids.display.text == "Error":
            self.ids.display.text = ""
        self.ids.display.text += value

    def clear_display(self):
        self.ids.display.text = ""

    def backspace(self):
        self.ids.display.text = self.ids.display.text[:-1]

    def evaluate(self, expression):
        try:
            expression = expression.replace('^', '**')
            result = eval(expression, {"__builtins__": None}, {
                'sin': sin, 'cos': cos, 'tan': tan, 'log': log, 'sqrt': sqrt})
            if '**' in expression:
                # Mostrar el resultado con 2 decimales
                self.ids.display.text = "{:.2f}".format(result)
            else:
                self.ids.display.text = "{:.2f}".format(result)  # Mostrar el resultado con 2 decimales
        except Exception as e:
            self.ids.display.text = "Error"

class Calculadora(App):
    def build(self):
        return CalculatorLayout()
KV = '''
<CalculatorLayout>:
    orientation: 'vertical'
    display: display
    BoxLayout:
        size_hint_y: None
        height: 100
        TextInput:
            id: display
            font_size: 32
            readonly: True
            halign: "right"
            valign: "middle"
            text: ""
            multiline: False

    GridLayout:
        cols: 4
        rows: 6

        Button:
            text: "7"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "8"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "9"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "/"
            font_size: 37
            on_press: root.append_display(self.text)
            background_color: (0.86, 0.44, 0.58)
            color: (1, 1, 1, 1)

        Button:
            text: "4"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "5"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "6"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "*"
            font_size: 37
            on_press: root.append_display(self.text)
            background_color: (0.86, 0.44, 0.58)
            color: (1, 1, 1, 1)

        Button:
            text: "1"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "2"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "3"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "-"
            font_size: 37
            on_press: root.append_display(self.text)
            background_color: (0.86, 0.44, 0.58)
            color: (1, 1, 1, 1)

        Button:
            text: "0"
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "."
            on_press: root.append_display(self.text)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1
                Line:
                    width: 3.5
                    rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "+"
            font_size: 37
            on_press: root.append_display(self.text)
            background_color: (0.86, 0.44, 0.58)
            color: (1, 1, 1, 1)
        Button:
            text: "="
            font_size: 37
            on_press: root.evaluate(root.ids.display.text)
            background_color: (0.56, 0.93, 0.56)
            color: (1, 1, 1, 1)

        Button:
            text: "sin"
            on_press: root.append_display(self.text + "(")
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)
        Button:
            text: "cos"
            on_press: root.append_display(self.text + "(")
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)
        Button:
            text: "tan"
            on_press: root.append_display(self.text + "(")
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)
        Button:
            text: "log"
            on_press: root.append_display(self.text + "(")
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)

        Button:
            text: "("
            on_press: root.append_display(self.text)
            background_color: (0, 0.75, 0.75)
            color: (1, 1, 1, 1)
        Button:
            text: ")"
            on_press: root.append_display(self.text)
            background_color: (0, 0.75, 0.75)
            color: (1, 1, 1, 1)
        Button:
            text: "^"
            font_size: 37
            on_press: root.append_display(self.text)
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)
        Button:
            text: "sqrt"
            on_press: root.append_display(self.text + "(")
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)
        Button:
            text: "¡BORRAR!"
            on_press: root.clear_display()
            background_color: (0, 0, 1, 1)
            color: (1, 1, 1, 1)
        Widget:
        Widget:
'''
if __name__ == "__main__":
    Builder.load_string(KV)
    Calculadora().run()
