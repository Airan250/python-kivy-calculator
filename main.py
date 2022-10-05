from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(background_color='black', foreground_color='white')
        self.last_was_operator = False
        main_layout.add_widget(self.solution)
        self.operator = ["/","-","*","+","."]
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","-"],
            ["1","2","3","*"],
            [".","0","c","+"]
        ]
        for row in buttons:
            L_layout = BoxLayout()
            for label in row:
                btn = Button(text=label)
                L_layout.add_widget(btn)
                btn.bind(on_press=self.on_btn_press)
            main_layout.add_widget(L_layout)
        equal = Button(text="=")
        equal.bind(on_press=self.on_solution)
        main_layout.add_widget(equal)
        return main_layout

    def on_btn_press(self, instance):
        current = self.solution.text
        pressed = instance.text
        if pressed == "c":
            self.solution.text = ""
        elif pressed in self.operator and self.last_was_operator:
            return
        elif pressed in self.operator and current == "":
            return
        else:
            self.solution.text += pressed
            if pressed in self.operator:
                self.last_was_operator = True
            else:
                self.last_was_operator = False
    def on_solution(self, instance):
        text = self.solution.text
        if self.last_was_operator:
            return
        elif text and text != "=":
            self.solution.text = str(eval(text))


if __name__=="__main__":
    app = MainApp()
    app.run()