from shape import Shape

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super(). __init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
            print(f"Is is a triangle with an area of {self.width * self.height / 2}")
            super().describe()
