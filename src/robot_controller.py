from src.robot import Robot


class RobotController:
    """ Parses commands and run a robot inside a plateau.

        Attributes:
            commands (list): A list with commands in string format to be
            dealed by Robot class.
            plateau_dimensions (list): A list of ints with the plateau
            dimensions.

    """
    def __init__(self, commands):
        self.commands = commands
        self.plateau_dimensions = [int(dimension) for dimension in self.commands.pop(0).split(' ')]


    def get_robots_output(self):
        """ Given a set of commands and plateau dimensions parses this values
            run robot commands, and yield the current coordinates and
            orientations.

        """
        while self.commands:
            coordinates_and_orientation = self.commands.pop(0)
            coordinates = list(map(int, coordinates_and_orientation.split(' ')[:2]))
            orientation = coordinates_and_orientation.split(' ')[-1]
            robot_commands = self.commands.pop(0)

            robot = Robot(coordinates, orientation, self.plateau_dimensions)
            [robot.run(command) for command in robot_commands]
            yield robot.get_coordinate_and_orientation_text()
