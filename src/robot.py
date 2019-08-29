from enum import Enum

from errors.robot_errors import (InvalidCommandError, InvalidCoordinateError,
                                 InvalidMovementError)
from src.orientations import Orientations


class Robot:
    """ Implements robot move, spin movements and run method to run given commands.

            Attirbutes:
                initial_coordinate (string): String containing two numbers to be parsed as integer .
                initial_orientaiton (string): String containg a valid value for orientation.
                plateau_dimension (list): List containing two integers relative to length and heigth of a plateau

    """
    def __init__(self, initial_coordinate, initial_orientation, plateau_dimensions):
        self.plateau_dimensions = list(map(int, plateau_dimensions))
        self.orientation = Orientations.from_text_to_list(initial_orientation)

        try:
            if type(initial_coordinate) == str:
                self.coordinate = [int(value) for value in initial_coordinate.split(' ')]
            else:
                self.coordinate = [int(value) for value in initial_coordinate]

            initial_coordinate_is_outside_plateau = \
                [point for point in zip(self.coordinate, self.plateau_dimensions) if point[0] < 0 or point[0] > point[1]]

            if initial_coordinate_is_outside_plateau:
                raise InvalidCoordinateError(f'''Cannot accept {initial_coordinate} because it is outside the plateau''')

        except ValueError:
            raise InvalidCoordinateError(f'''Cannot accept {initial_coordinate} as initial coordinate because it does not
            have valid values for x and y''')


    def run(self, command):
        """ Runner of robot commands.

            Given a command takes the decision to move or spin the robot.

            Args:
                command(string): A string with a valid command to be passed to robot spin or move.

        """
        if command == 'R' or command == 'L':
            self.spin(command)
        elif command == 'M':
            self.move()
        else:
            raise InvalidCommandError(f'The command {command} is not valid. Please send only R, L or M')

    def spin(self, command):
        """ Implements the logic to spin the robot.

            Given a command spin uses the class orientation to search the next orientation relative of this command.

            Args:
                command (string): A string with a valid command to be passed to orientation.

        """
        self.orientation = Orientations.get_orientation_relative_to(self.orientation, command)

    def move(self):
        """ Implements the logic to move a robot.

            Given the current coordinate and orientation of the robot, sum this values that are already parsed in the instanciation of the class and validates if the robot remains inside the plateau.

        """
        PLATEAU_ORIGIN = [0, 0]

        next_coordinate = [sum(coordinate) for coordinate in zip(self.coordinate, self.orientation)]
        next_coordinate_is_inside_plateau = next_coordinate >= PLATEAU_ORIGIN and next_coordinate <= self.plateau_dimensions

        if not next_coordinate_is_inside_plateau:
            raise InvalidMovementError(f'Cannot move to {next_coordinate} because is outside plateau')

        self.coordinate = next_coordinate

    def get_coordinate_and_orientation_text(self):
        """ Parses coordinate and orientation in a atring to show the current
            values.

        """
        return f'{self.coordinate[0]} {self.coordinate[1]} {Orientations.from_list_to_text(self.orientation)}'
