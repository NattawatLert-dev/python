from animal import Animal

class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing")