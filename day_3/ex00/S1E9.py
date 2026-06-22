from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class"""
    @abstractmethod
    def __init__(self, first_name: str, alive=True):
        self.first_name = first_name
        self.is_alive = alive
        return

    def die(self):
        """Make character die"""
        self.is_alive = False


class Stark(Character):
    """Stark character from abstract Character class"""
    def __init__(self, first_name: str, alive=True):
        """Init Stark class"""
        Character.__init__(self, first_name, alive)
