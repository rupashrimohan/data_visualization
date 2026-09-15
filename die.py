from random import randint


class Die:
    """A class to represent a single die."""

    def __init__(self, num_sides=6):
        """Initializing the class attributes."""
        self.num_sides = num_sides

    def roll(self):
        """Return the random value between 1 and the num of sides"""
        return randint(1, self.num_sides)
