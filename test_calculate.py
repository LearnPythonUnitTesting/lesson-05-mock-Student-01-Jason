import unittest
import calculate
from unittest import mock


class TestMethod(unittest.TestCase):
    def test_get_int(self):
        # TODO
        calculate.get_random = mock.Mock(return_value=0.8)
        self.assertEqual(calculate.get_int(), 1)

        calculate.get_random = mock.Mock(return_value=0.2)
        self.assertEqual(calculate.get_int(), 0) 
