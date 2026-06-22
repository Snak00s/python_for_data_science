from S1E9 import Character


class Baratheon(Character):
    """Representing Baratheon family."""
    def __init__(self, first_name: str, alive=True, eyes='brown',
                 hairs='dark'):
        """Init Baratheon class"""
        self.first_name = first_name
        self.is_alive = alive
        self.family_name = 'Baratheon'
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Str representation of Baratheon class"""
        return

    def __repr__(self):
        """Repr of Baratheon class"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """Representing Lannister family."""
    def __init__(self, first_name: str, alive=True, eyes='blue',
                 hairs='light'):
        """Init Lannister class"""
        self.first_name = first_name
        self.is_alive = alive
        self.family_name = 'Lannister'
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Str representation of Lannister class"""
        return

    def __repr__(self):
        """Repr of Lannister class"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def create_lannister(first_name: str, alive=True):
        """Create a new Lannister"""
        return Lannister(first_name=first_name, alive=alive)
