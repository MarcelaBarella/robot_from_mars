import argparse

from src.robot_controller import RobotController

parser = argparse.ArgumentParser(description='Robot controller')

parser.add_argument(
    '--file',
    type=argparse.FileType('r'),
    help=
    'File that contains plateau dimension and robot commads and coordinates',
    required=True)

argumets = parser.parse_args()

input_text_lines = argumets.file.readlines()
commands = [line.strip() for line in input_text_lines]

if __name__ == '__main__':
    robot_controller = RobotController(commands)
    [print(output) for output in robot_controller.get_robots_output()]
