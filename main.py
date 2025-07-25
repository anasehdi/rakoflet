import flet as ft
import math


def main(page: ft.Page):
    page.title = "Geometry Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # UI Elements
    mode_dropdown = ft.Dropdown(
        label="Mode",
        options=[
            ft.dropdown.Option("Area/Perimeter"),
            ft.dropdown.Option("Side Length"),
        ],
        value="Area/Perimeter"
    )

    shape_dropdown = ft.Dropdown(
        label="Shape",
        options=[ft.dropdown.Option(s) for s in [
            "Square", "Triangle", "Rectangle", "circle", "rectangular parallelepiped", "manshour",
            "Rhombus", "Parallelogram", "Cube", "Parallelepiped", "Quadrilateral Pyramid"
        ]],
        value="Square"
    )

    op_dropdown = ft.Dropdown(
        label="Operation",
        options=[ft.dropdown.Option("Area"), ft.dropdown.Option("Perimeter"), ft.dropdown.Option("Volume")],
        value="Area"
    )

    dim_input = ft.TextField(label="Enter dimensions (comma separated)", width=300)
    result_text = ft.Text("", selectable=True)

    def calculate(e):
        try:
            dims = [float(x.strip()) for x in dim_input.value.split(",") if x.strip()]
        except:
            result_text.value = "Invalid input. Please enter numeric values."
            page.update()
            return

        shape = shape_dropdown.value
        mode = mode_dropdown.value
        op = op_dropdown.value
        res = None

        if mode == "Area/Perimeter":
            if shape == "Square" and len(dims) >= 1:
                res = dims[0] ** 2 if op == "Area" else 4 * dims[0]
            elif shape == "Triangle":
                if op == "Area" and len(dims) >= 2:
                    res = 0.5 * dims[0] * dims[1]
                elif op == "Perimeter" and len(dims) >= 3:
                    res = sum(dims[:3])
            elif shape == "Rectangle" and len(dims) >= 2:
                res = dims[0] * dims[1] if op == "Area" else 2 * (dims[0] + dims[1])
            elif shape == "circle" and len(dims) >= 1:
                r = dims[0]
                res = math.pi * r ** 2 if op == "Area" else 2 * math.pi * r
            elif shape == "Rhombus" and len(dims) >= 1:
                res = dims[0] ** 2 if op == "Area" else 4 * dims[0]
            elif shape == "Parallelogram" and len(dims) >= 2:
                res = dims[0] * dims[1] if op == "Area" else 2 * (dims[0] + dims[1])
            elif shape == "Cube" and len(dims) >= 1:
                s = dims[0]
                if op == "Area":
                    res = 6 * s ** 2
                elif op == "Perimeter":
                    res = 12 * s
                elif op == "Volume":
                    res = s ** 3
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
            elif shape == "manshour" and len(dims) >= 9:
                if op == "Area":
                    res = (dims[0]**2) + (0.5 * dims[1] * dims[2]) + \
                          (0.5 * dims[3] * dims[4]) + (dims[5] * dims[6]) + (dims[7] * dims[8])
            elif shape == "Quadrilateral Pyramid" and len(dims) >= 3:
                if op == "Volume":
                    base = dims[0] * dims[1]
                    height = dims[2]
                    res = (1 / 3) * base * height
                elif op == "Area":
                    base = 0.5 * dims[0] * dims[1]
                    side = dims[2]
                    res = 4 * base + side ** 2
        elif mode == "Side Length":
            if shape == "Square" and len(dims) >= 1:
                res = math.sqrt(dims[0])
            elif shape == "Cube" and len(dims) >= 1:
                if op == "Area":
                    res = math.sqrt(dims[0] / 6)
                elif op == "Volume":
                    res = dims[0] ** (1 / 3)

        result_text.value = f"Result: {res}"
        page.update()

    def reset(e):
        dim_input.value = ""
        result_text.value = ""
        page.update()

    # App Layout
    page.add(
        ft.Text("🧮 Geometry Calculator", size=24),
        mode_dropdown,
        shape_dropdown,
        op_dropdown,
        dim_input,
        ft.Row([
            ft.ElevatedButton("Calculate", on_click=calculate),
            ft.ElevatedButton("Reset", on_click=reset),
        ]),
        result_text
    )


ft.app(target=main)
