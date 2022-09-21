from datacapture import CapureData
from unittest import TestCase
import pytest

class TryTest(TestCase):
    def setUp(self):
        self.d = CapureData()
        self.d.add(11)
        self.d.add(12)
        self.d.add(13)
        self.d.add(14)
        self.d.add(15)
        self.d.add(16)
        self.d.add(17)
        self.d.add(18)
        self.d.add(19)
        self.d.add(10)
        self.stat = self.d.build_stat()

    def test_add(self):
        self.d.add(12)
        self.assertEqual(12, self.d.get()[10])

    def test_add_more_fail(self):
        with pytest.raises(ValueError, match=r".* more .*"):
            self.d.add(12345667)

    def test_add_negative_fail(self):
        with pytest.raises(ValueError, match=r".* negative.*"):
            self.d.add(-1)

    def test_add_no_int_fail(self):
        with pytest.raises(TypeError, match=r".* valid.*"):
            self.d.add('aaaaaa')

    def test_get_less_val(self):
        c = self.stat.less(14)
        self.assertEqual(4, c)

    def test_get_less_error(self):
        with pytest.raises(ValueError, match=r".*values.*"):
            self.stat.less(9)

    def test_less_input_error(self):
        with pytest.raises(TypeError, match=r".* valid.*"):
            self.stat.less('a')

    def test_get_greater(self):
        self.assertEqual(5, self.stat.greater(14))

    def test_get_greater_error(self):
        with pytest.raises(ValueError, match=r".*values.*"):
            self.stat.greater(100)

    def test_greater_input_error(self):
        with pytest.raises(TypeError, match=r".* valid.*"):
            self.stat.greater('a')

    def test_get_between(self):
        self.assertEqual(5, self.stat.between(10, 16))

    def test_get_between_error(self):
        with pytest.raises(ValueError, match=r".*values.*"):
            self.stat.between(1, 2)

    def test_get_between_error_out(self):
        with pytest.raises(ValueError, match=r".*value.*"):
            self.stat.between(10, 9)

    def test_between_input_error(self):
        with pytest.raises(TypeError, match=r".* valid.*"):
            self.stat.between('a', 1)
