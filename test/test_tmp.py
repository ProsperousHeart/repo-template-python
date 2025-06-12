# import pytest
import unittest
from unittest.mock import patch
from io import StringIO
from src.tmp import print_hi, str_func


# def test_print_hi(capsys):
#     print_hi()
#     captured = capsys.readouterr()
#     assert captured.out == "Hi\n"


class TestTmp(unittest.TestCase):
    """Test cases for the tmp module."""

    def setUp(self):
        # return super().setUp()
        pass

    def tearDown(self):
        # return super().tearDown()
        pass

    def test_print_hi(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print_hi()
            self.assertEqual(fake_out.getvalue(), "Hi\n")

    def test_str_func_valid(self):
        resp = str_func("test")
        self.assertEqual(resp, "You sent:  test")

    def test_str_func_none(self):
        with self.assertRaises(TypeError):
            str_func(None)


if __name__ == "__main__":
    unittest.main()
