#!/usr/bin/python3
"""
Tests base model class and its instances
"""

import datetime
import time
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
        self.assertEqual(tes1.__dict__, {'created_at': datetime.datetime.now(),
                                         'id': f'{tes1.id}',
                                         'name': 'Tom', 'number': 89,
                                         'updated_at': datetime.datetime.now()})
        self.assertTrue(isinstance(tes1.id, str))

    def test_unique_id(self):
        """
        check if id are unique to each instance
        """
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_time(self):
        """
        test time values for created_at and updated_at with delay 0.02s
        """
        id1 = BaseModel()
        t_id1 = datetime.datetime.now()
        self.assertAlmostEqual(id1.created_at, t_id1)
        self.assertTrue(id1.created_at >= id1.updated_at)
        time.sleep(0.02)
        id2 = BaseModel()
        self.assertNotEqual(id2.created_at.timestamp(),
                            id1.created_at.timestamp())

    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = BaseModel()
        self.assertEqual(
            f"[{test1.__class__.__name__}] ({test1.id}) {test1.__dict__}",
            f"[BaseModel] ({test1.id}) {test1.__dict__}")

    def test_save(self):
        """
        tests save and if file is in file.json
        """
        pass


if __name__ == '__main__':
    unittest.main()
