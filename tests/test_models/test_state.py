#!/usr/bin/python3
"""
module with tests for state
"""


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    test all cases for state
    """
    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = State()
        self.assertEqual(str(test1) , f"[State] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
