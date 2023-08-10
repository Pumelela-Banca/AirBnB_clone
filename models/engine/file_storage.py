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
        return FileStorage.__objects
    
    def new(self, obj):
        """
        adds new value to __objects
        """
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = f'{obj.to_dict()}'

    def save(self):
        """
        saves __objects to file
        """
        with open(FileStorage.__file_path, "w") as fh:
            json.dump(FileStorage.__objects, fh)

    def reload(self):
        """
        loads dictionary from object
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fh:
                FileStorage.__objects = json.load(fh)
