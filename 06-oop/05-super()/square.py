from shape import Shape

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super(). __init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"Is is a square with an area of {self.width * self.width}")
        super().describe()