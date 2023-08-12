#!/usr/bin/python3

"""
file storage module that works with file.json to
store user, place, amenity, city, state and review
"""


import os
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns current dictionary object for all
        instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        adds new value to __objects
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize and deseralize object to json file
        """
        dict1 = {}
        for key, value in FileStorage.__objects.items():
            dict1[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fh:
            json.dump(dict1, fh)

    def reload(self):
        """
        loads dictionary from object
        """
        try:
            with open(FileStorage.__file_path) as fh:
                dict2 = json.load(fh)
            for key, value in dict2.items():
                self.new(eval(key.split(".")[0])(**value))
        except Exception:
            return
