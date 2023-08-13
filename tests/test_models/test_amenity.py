#!/usr/bin/python3
"""
Tests base model class and its instances
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test all possible inputs on Amenity
    """
    def test_creation(self):
        """
        Test if class can be developed
        """

    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = BaseModel()
        self.assertEqual(str(test1), f"[Amenity] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
