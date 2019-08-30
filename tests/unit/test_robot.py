import pytest
from errors.robot_errors import (InvalidCommandError, InvalidCoordinateError,
                                 InvalidMovementError)
from src.robot import Robot


class TestRobot:
    def test__initialize_robot__given_some_orientation_as_string__it_should_have_given_orientation(
            self):
        target = Robot('3 3', 'N', [5, 5])
        assert target.coordinate == [3, 3]

    def test__initialize_robot__given_invalid_orientation_as_string__it_should_raise_invalid_coordinate_error(
            self):
        with pytest.raises(InvalidCoordinateError):
            Robot('foo', 'N', [5, 5])

    def test__initialize_robot__given_some_orientation_as_integer_list__it_should_have_given_orientation(
            self):
        target = Robot([3, 3], 'N', [5, 5])
        assert target.coordinate == [3, 3]

    def test__initialize_robot__given_some_orientation_outside_plateau__it_should_raise_invalid_coordinate_error(
            self):
        with pytest.raises(InvalidCoordinateError):
            target = Robot('6 6', 'N', [5, 5])

    def test__initialize_robot__given_plateau_dimensions__it_should_have_list_of_integers_with_dimensions(
            self):
        target = Robot('3 3', 'N', ['5', '5'])
        assert target.plateau_dimensions == [5, 5]

    def test__initialize_robot__given_some_orientation__it_should_have_given_orientation_as_numbers(
            self):
        target = Robot('3 3', 'N', [5, 5])
        assert target.orientation == [0, 1]

    @pytest.mark.parametrize('command', ['L', 'R', 'M'])
    def test__do__given_valid_command__it_should_run_without_errors(
            self, command):
        target = Robot([2, 2], 'N', [5, 5])
        target.run(command)

    def test__do__given_invalid_command__it_should_raise_invalid_command_error(
            self):
        target = Robot([2, 2], 'N', [5, 5])
        with pytest.raises(InvalidCommandError):
            target.run('foo')

    def test__move__to_an_invalid_orientation__it_should_raise_invalid_movement_error(
            self):
        target = Robot([0, 0], 'W', [5, 5])
        with pytest.raises(InvalidMovementError):
            target.move()

    def test__get_orientation_and_orientation_text__should_return_correct_text(
            self):
        target = Robot([1, 2], 'N', [5, 5])
        assert target.get_coordinate_and_orientation_text() == '1 2 N'
