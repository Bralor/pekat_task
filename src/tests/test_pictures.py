import os

import numpy
import pytest

from pictures.picture import PictureLoader
from pictures.picture import PictureResizer


VALID_ATTRS = [
    ("name"),
    ("path"),
    ("width"),
    ("height")
]
INVALID_ATTRS = [
    ("filename"),
    ("filepath"),
    ("x"),
    ("size_x")
]
CORRECT_DIMENSIONS = [
    ("height", 999),
    ("width", 1308)
]
INCORRECT_DIMENSIONS = [
    ("height", 9999),
    ("width", 13)
]


class TestPictureLoader:
    """
    An object that checks the valid or invalid outputs from the class
    'PictureLoader'.
    """

    def setup(self):
        filepath = "src/tests/arrow2.png"
        name = os.path.basename(filepath)
        self.testing = PictureLoader(filepath, name)

    @pytest.mark.parametrize("value", VALID_ATTRS)
    def test_if_instance_has_attr_path(self, value):
        assert hasattr(self.testing, value)

    @pytest.mark.parametrize("value", INVALID_ATTRS)
    def test_if_instance_has_incorrect_attrs(self, value):
        assert not hasattr(self.testing, value)

    def test_correct_value_of_instance_attr_path(self):
        assert self.testing.path == "src/tests/arrow2.png"

    def test_incorrect_value_of_instance_attr_path(self):
        assert self.testing.path != "src/foo/bar.png"

    def test_correct_value_of_instance_attr_name(self):
        assert self.testing.name == "resized_arrow2.png"

    def test_incorrect_value_of_instance_attr_name(self):
        assert self.testing.name != "resized_arrow3.png"

    def test_valid_data_type_instance_initiation(self):
        valid_dt = self.testing.initiate_image()
        assert isinstance(valid_dt, numpy.ndarray)

    def test_invalid_data_type_instance_initiation(self):
        valid_dt = self.testing.initiate_image()
        assert not isinstance(valid_dt, dict)

    @pytest.mark.parametrize("size, value", CORRECT_DIMENSIONS)
    def test_get_proper_dimensions(self, size, value):
        sample = self.testing.initiate_image()
        dimensions = self.testing.get_dimensions(sample)
        assert dimensions[size] == value

    @pytest.mark.parametrize("size, value", INCORRECT_DIMENSIONS)
    def test_get_incorrect_dimensions(self, size, value):
        sample = self.testing.initiate_image()
        dimensions = self.testing.get_dimensions(sample)
        assert dimensions[size] != value


class TestPictureResizer:

    def setup(self):
        filepath = "src/tests/arrow2.png"
        name = os.path.basename(filepath)
        self.resizer = PictureResizer(filepath, name)

    @pytest.mark.parametrize("value", VALID_ATTRS)
    def test_if_instance_has_attr_path(self, value):
        assert hasattr(self.resizer, value)

    @pytest.mark.parametrize("value", INVALID_ATTRS)
    def test_if_instance_has_incorrect_attrs(self, value):
        assert not hasattr(self.resizer, value)

    def test_if_is_resolution_checks_well(self):
        sample = self.resizer.initiate_image()
        dimensions = self.resizer.is_resolution_same(sample)
        assert not dimensions

    # def test_the_correct_resizing_of_the_picture(self):
        # sample = self.resizer.initiate_image()
        # output = self.resizer.resize_image(sample)
        # assert output
