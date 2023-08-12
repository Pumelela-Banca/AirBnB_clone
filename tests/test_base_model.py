#!/usr/bin/python3
"""
Tests base model class and its instances
"""

import datetime
import time
import unittest
from models.base_model import BaseModel
from models import storage


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
        tes1 = BaseModel(place="Tex", sta="5")
        # test updated at
        save_time = tes1.updated_at.timestamp()
        time.sleep(0.02)
        tes1.save()
        self.assertTrue(tes1.updated_at.timestamp() > save_time)
        hold = storage.all()
        tes1_name = f'{tes1.__class__.__name__}.{tes1.id}'
        # test key
        self.assertIn(tes1_name, hold.keys())
        # test values
        # change str to dictionary
        self.assertIn("place", hold[tes1_name].values())
        self.assertIn("Tex", hold[tes1_name]["place"])
        self.assertIn("sta", hold[tes1_name].values())
        self.assertIn("5", hold[tes1_name]["sta"])
        self.assertIn("id", hold[tes1_name].values())
        self.assertIn(f"{tes1.id}", hold[tes1_name]["id"])
        self.assertIn("created_at", hold[tes1_name].values())
        self.assertIn(f"{tes1.created_at}", hold[tes1_name]["created_at"])
        self.assertIn("updated_at", hold[tes1_name].values())
        self.assertIn(f"{tes1.updated_at}", hold[tes1_name]["updated_at"])
        self.assertIn("__class__", hold[tes1_name].values())
        self.assertIn(f"{tes1.__class__}", hold[tes1_name]["__class__"])

    def test_to_dict(self):
        """
        tests to see if to dict works
        """
        tes1 = BaseModel(place="ken", name="Ele")
        new_dic = tes1.to_dict()
        self.assertIn("name", new_dic.keys())
        self.assertEqual("Ele", new_dic["name"])
        self.assertIn("place", new_dic.keys())
        self.assertEqual("ken", new_dic["place"])
        self.assertIn("id", new_dic.keys())
        self.assertEqual(f"{tes1.id}", new_dic["id"])
        self.assertIn("created_at", new_dic.keys())
        self.assertEqual(f"{tes1.created_at.now()}",
                         new_dic["created_at"].replace("T", " "))
        self.assertIn("updated_at", new_dic.keys())
        self.assertEqual(f"{tes1.updated_at}", new_dic["updated_at"].replace("T", " "))


if __name__ == '__main__':
    unittest.main()
