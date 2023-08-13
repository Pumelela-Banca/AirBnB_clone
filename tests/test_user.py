#!/usr/bin/python3
"""
module with tests for User
"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    test all cases for state
    """
    def setUp(self):
        pass

    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = User()
        self.assertEqual(str(test1), f"[User] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
