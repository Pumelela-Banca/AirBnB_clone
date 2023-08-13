#!/usr/bin/python3

"""
Tests file storage class and its instances
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    tests for storage methods
    """
    def setUp(self) -> None:
        """
        set up store
        """
        self.store = FileStorage()

    def test_all(self):
        """
        test cases for all method
        """
        # empty dictionary
        self.assertTrue(type(self.store.all()) is dict)

    def test_new(self):
        """
        test if new works
        """
        tes1 = BaseModel()
        self.store.new(tes1)
        self.assertIn("BaseModel." + tes1.id, self.store.all().keys())
        vals = self.store.all().values()
        for x in vals:
            for y in x.to_dict():
                if y == x:
                    self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
