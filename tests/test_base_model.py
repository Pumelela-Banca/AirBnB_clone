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

    def test_documentation(self):
        """
        tests documentation requirements
        """
        import models.base_model as base
        model = BaseModel()
        self.assertIsNotNone(base.__doc__)
        self.assertTrue(base.__doc__ != "")
        self.assertIsNotNone(model.__str__)
        self.assertTrue(model.__str__ != "")
        self.assertIsNotNone(model.to_dict)
        self.assertTrue(model.to_dict.__doc__ != "")
        self.assertIsNotNone(model.save)
        self.assertTrue(model.save.__doc__ != "")

    def test_init(self):
        """
        test initialization of class
        """
        tes1 = BaseModel(name="Tom", number=89)
        self.assertEqual(tes1.__dict__['id'], f'{tes1.id}')
        self.assertEqual(tes1.__dict__['name'], f'{"Tom"}')
        self.assertEqual(tes1.__dict__['number'], 89)
        self.assertTrue(isinstance(tes1.id, str))
        self.assertTrue(type(tes1.updated_at), datetime)
        self.assertTrue(type(tes1.created_at), datetime)

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
        self.assertEqual(str(test1) , f"[BaseModel] ({test1.id}) {test1.__dict__}")

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
        storage.new(tes1)
        hold = storage.all()
        tes1_name = f'{tes1.__class__.__name__}.{tes1.id}'
        # test key
        self.assertIn(tes1_name, hold.keys())
        # test values
        # change str to dictionary
        self.assertIn("Tex", hold[tes1_name].place)
        self.assertIn("5", hold[tes1_name].sta)
        self.assertIn(f"{tes1.id}", hold[tes1_name].id)

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
        # self.assertAlmostEqual(f"{tes1.created_at.now()}",
        #                 new_dic["created_at"].replace("T", " "))
        self.assertIn("updated_at", new_dic.keys())
        self.assertEqual(f"{tes1.updated_at}",
                         new_dic["updated_at"].replace("T", " "))


if __name__ == '__main__':
    unittest.main()
