class Shape:

    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color

    def get_inner_color(self):
        return self._inner_color

    def get_border_color(self):
        return self._border_color

    def set_inner_color(self, inner_color):
        self._inner_color = inner_color

    def set_border_color(self, border_color):
        self._border_color = border_color


class Circle(Shape):

    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


class Rectangle(Shape):

    def __init__(self, width, length, inner_color, border_color):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length

    def set_rect_width(self, width):
        self._width = width

    def set_rect_length(self, length):
        self._length = length

    def get_rect_with(self):
        return self._width

    def get_rect_length(self):
        return self._length


class Square(Rectangle):

    def __init__(self, inner_color, border_color, width):
        super().__init__(inner_color, border_color, width, width)
        self._length = width
        self._width = width

    def set_sq_length(self, length):
        self._length = length
        self._width = length

    def set_sq_width(self, width):
        self._width = width
        self._length = width


shape = Shape("red", "green")
shape = {
    "Border Color": Shape.get_border_color(shape),
    "Inner Color": Shape.get_inner_color(shape),
}
print(shape)

circle = Circle("coral", "light green", 10)
circle = {
    "Circle border color": Circle.get_border_color(circle),
    "Circle inner color": Circle.get_inner_color(circle),
    "Circle radius": Circle.get_radius(circle)
}
print(circle)

rectangle = Rectangle(7, 9, "Black", "Blue")
rectangle = {
    "Rectangle border color": Rectangle.get_border_color(rectangle),
    "Rectangle inner color": Rectangle.get_inner_color(rectangle),
    "Rectangle length": Rectangle.get_rect_length(rectangle),
    "Rectangle width": Rectangle.get_rect_with(rectangle),
}
print(rectangle)

square = Square("black", "blue", 20)
square = {
    "Square border color": Square.get_border_color(square),
    "Square inner color": Square.get_inner_color(square),
    "Square width and length": Square.get_rect_length(square)
}
print(square)


