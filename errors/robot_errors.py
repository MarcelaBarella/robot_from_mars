class InvalidCommandError(Exception):
    """ Invalid command received by robot """
    pass


class InvalidMovementError(Exception):
    """ Uses when robot receive a command to do a movement that is not valid"""
    pass


class InvalidCoordinateError(Exception):
    """ Indicates that a given value is not a valid coordinate """
    pass
