from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
import math

class PasswordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "login"

        layout = BoxLayout(orientation='vertical', padding=40, spacing=15)
        layout.add_widget(Label(text="Enter Password", font_size=26))

        self.password_input = TextInput(password=True, font_size=22, multiline=False)
        layout.add_widget(self.password_input)

        login_button = Button(text="Login", font_size=24)
        login_button.bind(on_press=self.check_password)
        layout.add_widget(login_button)

        self.error_label = Label(text="", font_size=18, color=(1, 0, 0, 1))
        layout.add_widget(self.error_label)

        self.add_widget(layout)

    def check_password(self, instance):
        if self.password_input.text == "1000200":
            self.manager.current = "main"
        else:
            self.password_input.text = ""
            self.error_label.text = "Incorrect password!"

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "main"

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.mode_spinner = Spinner(text="Area/Perimeter", values=["Area/Perimeter", "Side Length"], font_size=20)
        layout.add_widget(self.mode_spinner)

        self.shape_spinner = Spinner(
            text="Square",
            values=["Square", "Triangle", "Rectangle", "circle", "rectangular parallelepiped", "manshour",
                    "Rhombus", "Parallelogram", "Cube", "Parallelepiped", "Quadrilateral Pyramid"],
            font_size=20
        )
        layout.add_widget(self.shape_spinner)

        self.op_spinner = Spinner(text="Area", values=["Area", "Perimeter", "Volume"], font_size=20)
        layout.add_widget(self.op_spinner)

        layout.add_widget(Label(text="Enter dimensions (comma separated):", font_size=18))

        self.dim_input = TextInput(multiline=False, font_size=18)
        layout.add_widget(self.dim_input)

        calc_button = Button(text="Calculate", font_size=22, background_color=(0, 0.6, 0, 1))
        calc_button.bind(on_press=self.calculate)
        layout.add_widget(calc_button)

        reset_button = Button(text="Reset", font_size=22, background_color=(1, 0, 0, 1))
        reset_button.bind(on_press=self.reset)
        layout.add_widget(reset_button)

        self.result_label = Label(text="", font_size=20, color=(0, 0, 1, 1))
        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def calculate(self, instance):
        shape = self.shape_spinner.text
        mode = self.mode_spinner.text
        op = self.op_spinner.text
        try:
            dims = [float(x.strip()) for x in self.dim_input.text.split(",") if x.strip()]
        except:
            self.result_label.text = "Invalid input. Please enter numeric values."
            return

        res = None

        if mode == "Area/Perimeter":
            if shape == "Square" and len(dims) >= 1:
                side = dims[0]
                res = side ** 2 if op == "Area" else 4 * side
            elif shape == "Triangle":
                if op == "Area" and len(dims) >= 2:
                    res = 0.5 * dims[0] * dims[1]
                elif op == "Perimeter" and len(dims) >= 3:
                    res = sum(dims[:3])
            elif shape == "Rectangle" and len(dims) >= 2:
                res = dims[0] * dims[1] if op == "Area" else 2 * (dims[0] + dims[1])
            elif shape == "Rhombus" and len(dims) >= 1:
                res = dims[0] ** 2 if op == "Area" else dims[0] * 4
            elif shape == "Parallelogram" and len(dims) >= 2:
                res = dims[0] * dims[1] if op == "Area" else 2 * (dims[0] + dims[1])
            elif shape == "Cube" and len(dims) >= 1:
                side = dims[0]
                if op == "Area":
                    res = 6 * side ** 2
                elif op == "Perimeter":
                    res = 12 * side
                elif op == "Volume":
                    res = side ** 3
            elif shape == "Parallelepiped" and len(dims) >= 3:
                l, w, h = dims[0], dims[1], dims[2]
                if op == "Area":
                    res = 2 * (l * w + l * h + w * h)
                elif op == "Volume":
                    res = l * w * h
            elif shape == "rectangular parallelepiped" and len(dims) >= 3:
                if op == "Volume":
                    res = dims[0] * dims[1] * dims[2]
                elif op == "Area":
                    res = 2 * (dims[0]*dims[1] + dims[0]*dims[2] + dims[1]*dims[2])
            elif shape == "Quadrilateral Pyramid" and len(dims) >= 3:
                if op == "Volume":
                    base_area = dims[0] * dims[1]
                    height = dims[2]
                    res = (1/3) * base_area * height
                elif op == "Area":
                    base = 0.5 * dims[0] * dims[1]
                    side = dims[2]
                    res = 4 * base + side**2
            elif shape == "circle" and len(dims) >= 1:
                r = dims[0]
                res = math.pi * r**2 if op == "Area" else 2 * math.pi * r
            elif shape == "manshour" and len(dims) >= 9:
                if op == "Area":
                    res = (dims[0]**2) + (0.5 * dims[1] * dims[2]) + (0.5 * dims[3] * dims[4]) + (dims[5] * dims[6]) + (dims[7] * dims[8])
            else:
                res = "Unsupported shape or insufficient data"

        elif mode == "Side Length":
            if shape == "Square" and len(dims) >= 1:
                res = math.sqrt(dims[0])
            elif shape == "Triangle" and len(dims) >= 2:
                base, area = dims[0], dims[1]
                res = (2 * area) / base
            elif shape == "Cube" and len(dims) >= 1:
                res = math.sqrt(dims[0] / 6) if op == "Area" else dims[0] ** (1/3)
            else:
                res = "Side length formula not available for this shape"

        self.result_label.text = f"Result: {res}"

    def reset(self, instance):
        self.dim_input.text = ""
        self.result_label.text = ""

class GeometryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PasswordScreen())
        sm.add_widget(MainScreen())
        return sm

if __name__ == '__main__':
    GeometryApp().run()
