from S1E9 import Character


class Baratheon(Character):
    """Representing Baratheon family."""
    def __init__(self, first_name: str, alive=True, eyes='brown',
                 hairs='dark'):
        self.first_name = first_name
        self.is_alive = alive
        self.family_name = 'Baratheon'
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return

    def __repr__(self):
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """Representing Lannister family."""
    def __init__(self, first_name: str, alive=True, eyes='blue',
                 hairs='light'):
        self.first_name = first_name
        self.is_alive = alive
        self.family_name = 'Lannister'
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return

    def __repr__(self):
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def create_lannister(first_name: str, alive=True):
        return Lannister(first_name=first_name, alive=alive)
