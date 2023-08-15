import math


def calculate_area(shape, **kwargs):
    try:
        if shape.lower() == "triangle":
            base = kwargs.get("base")
            height = kwargs.get("height")
            if base is None or height is None or base <= 0 or height <= 0:
                raise ValueError("Invalid base or height values for triangle.")
            return 0.5 * base * height
        elif shape.lower() == "rectangle":
            width = kwargs.get("width")
            height = kwargs.get("height")
            if width is None or height is None or width <= 0 or height <= 0:
                raise ValueError(
                    "Invalid width or height values for rectangle.")
            return width * height
        elif shape.lower() == "circle":
            radius = kwargs.get("radius")
            if radius is None or radius <= 0:
                raise ValueError("Invalid radius value for circle.")
            return math.pi * radius ** 2
        else:
            raise ValueError(
                "Invalid shape. Supported shapes: triangle, rectangle, circle.")
    except ValueError as e:
        return str(e)


# Example usages
triangle_area = calculate_area(shape="TRIANGLE", base=10, height=5)
rectangle_area = calculate_area(shape="rEctangle", width=8, height=5)
circle_area = calculate_area(shape="circlE", radius=3)

print(f"Triangle Area: {triangle_area}")
print(f"Rectangle Area: {rectangle_area}")
print(f"Circle Area: {circle_area}")
