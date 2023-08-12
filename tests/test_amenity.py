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
        amen = Amenity()




if __name__ == '__main__':
    unittest.main()
