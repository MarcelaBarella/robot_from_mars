from errors.orientation_errors import InvalidOrientationError


class Orientations:
    """ Implements the orientation logic, where each string orientation is
    parsed and then converted to a dict.

    """
    __orientations = {
        'N': [0, 1],
        'E': [1, 0],
        'S': [0, -1],
        'W': [-1, 0]
    }

    @staticmethod
    def from_text_to_list(orientation_text):
        """ Given a orientation text parses to a value of orientations dict """
        try:
            return Orientations.__orientations[orientation_text]
        except KeyError:
            raise InvalidOrientationError(f'Cannot recognize {orientation_text} orientation')

    @staticmethod
    def get_orientation_relative_to(origin_orientation, left_or_right):
        """ Given the parsed value of inital orientation and a command return the update of orientation based on this inputs

            Args:
                origin_orientation (string or list): If its a list is parsed to a string, with the value of initial robot orientation.
                left_or_right (string): A string with the command to be matched
                in the orientations relative.

        """
        if type(origin_orientation) != str:
            origin_orientation = Orientations.from_list_to_text(origin_orientation)

        try:
            orientations_relative = {
                'NL': 'W',
                'NR': 'E',
                'WL': 'S',
                'WR': 'N',
                'SL': 'E',
                'SR': 'W',
                'EL': 'N',
                'ER': 'S'
            }

            new_orientation = orientations_relative[origin_orientation + left_or_right]
            return Orientations.__orientations[new_orientation]
        except KeyError:
            raise InvalidOrientationError(f'Cannot get relative to {origin_orientation} because direction or relative is invalid')



    @staticmethod
    def from_list_to_text(orientation_list):
        """ Parses a list with valid orientations values em parses to text
            format.

            orientation_list (list): An array with valid orientation values.

        """
        for key in Orientations.__orientations.keys():
            if Orientations.__orientations[key] == orientation_list:
                return key

        raise InvalidOrientationError(f'Cannot recognize direction from array {orientation_list}')
