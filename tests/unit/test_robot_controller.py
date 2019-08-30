import pytest

from src.robot_controller import RobotController


class TestRobotController:
    def test__get_robots_ouput__given_example_input__should_return_example_output(
            self):
        commands = ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']

        target = RobotController(commands)

        assert list(target.get_robots_output()) == ['1 3 N', '5 1 E']
