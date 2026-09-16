from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=500):
        """Initializing the class attributes"""

        self.num_points = num_points

        # Walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walks(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length

        while len(self.x_values) < self.num_points:
            # Decide which direction to go in both x and y direction
            x_step = self._get_steps()
            y_step = self._get_steps()

            # No moves can be made
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    # Helper methods to get the x and y steps
    def _get_steps(self):
        """Calculate the x and y steps"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5])
        step = direction * distance
        return step
