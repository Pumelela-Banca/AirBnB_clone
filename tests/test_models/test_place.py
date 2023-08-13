#!/usr/bin/python3
"""
module to test place
"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    tests for place
    """
    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = BaseModel()
        self.assertEqual(str(test1) , f"[Place] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
