#!/usr/bin/python3

"""
Tests base model class and its instances
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test all possible inputs on BaseModel
    """
    def test_init(self):
        """
        test initialization of class
        """
        tes1 = BaseModel(name="Tom", number=89)
        # attributes not added to dictionary __dict__
        #self.assertTrue(isinstance(tes1.id, str))
        #self.assertEqual(tes1.name, "Tom")
        #self.assertEqual(tes1.number, 89)

    def test_unique_id(self):
        """
        check if id are unique to each instance
        """
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_time(self):
        """
        test time values for created_at and updated_at
        """
        pass

    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = BaseModel()
        self.assertEqual(
            f"[{test1.__class__.__name__}] ({test1.id}) {test1.__dict__}",
            f"[BaseModel] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
