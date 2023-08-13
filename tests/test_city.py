#!/usr/bin/python3
"""
Tests base model class and its instances
"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test city class inputs
    """
    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = BaseModel()
        self.assertEqual(str(test1) , f"[City] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
