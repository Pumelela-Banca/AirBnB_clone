#!/usr/bin/python3

"""
file storage module that works with file.json to
store user, place, amenity, city, state and review
"""


import os
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns current dictionary object for all
        instances
        """
        return self.__objects
    
    def new(self, obj):
        """
        adds new value to __objects
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = f'{obj.to_dict()}'

    def save(self):
        """
        saves __objects to file
        """
        with open(self.__file_path, "w") as fh:
            json.dump(self.__objects, fh)

    def reload(self):
        """
        loads dictionary from object
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as fh:
                self.__objects = json.load(fh)
