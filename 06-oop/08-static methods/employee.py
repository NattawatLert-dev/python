class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_into(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions