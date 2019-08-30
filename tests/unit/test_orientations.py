import pytest
from errors.orientation_errors import InvalidOrientationError
from src.orientations import Orientations


class TestOrientations:
    def test__from_text_to_list__invalid_orientation__should_raise_invalid_orientation_error(
            self):
        with pytest.raises(InvalidOrientationError):
            Orientations.from_list_to_text('foo')

    @pytest.mark.parametrize('orientation,expected_coordinates',
                             [('N', [0, 1]), ('S', [0, -1]), ('E', [1, 0]),
                              ('W', [-1, 0])])
    def test__from_text_to_list__valid_orientation__should_return_list_with_orientation(
            self, orientation, expected_coordinates):
        assert Orientations.from_text_to_list(
            orientation) == expected_coordinates

    def test__from_list_to_text__invalid_orientation__should_raise_invalid_orientation_error(
            self):
        with pytest.raises(InvalidOrientationError):
            assert Orientations.from_list_to_text([-2, -2])

    @pytest.mark.parametrize('coordinates,expected_orientation',
                             [([0, 1], 'N'), ([0, -1], 'S'), ([1, 0], 'E'),
                              ([-1, 0], 'W')])
    def test__from_list_to_text__valid_list__should_return_text_of_orientation(
            self, coordinates, expected_orientation):
        assert Orientations.from_list_to_text(
            coordinates) == expected_orientation

    def test__get_orientation_relative_to__invalid_orientation__should_raise_invalid_orientation_error(
            self):
        with pytest.raises(InvalidOrientationError):
            assert Orientations.get_orientation_relative_to('foo', 'bar')

    @pytest.mark.parametrize('orientation,next_orientation', [('N', [1, 0]),
                                                              ('W', [0, 1]),
                                                              ('S', [-1, 0]),
                                                              ('E', [0, -1])])
    def test__get_orientation_relative_to__valid_orientations_turn_right__should_return_valid_orientation(
            self, orientation, next_orientation):
        assert Orientations.get_orientation_relative_to(
            orientation, 'R') == next_orientation

    @pytest.mark.parametrize('orientation,next_orientation', [('N', [-1, 0]),
                                                              ('E', [0, 1]),
                                                              ('S', [1, 0]),
                                                              ('W', [0, -1])])
    def test__get_orientation_relative_to__valid_orientations_turn_left__should_return_valid_orientation(
            self, orientation, next_orientation):
        assert Orientations.get_orientation_relative_to(
            orientation, 'L') == next_orientation
