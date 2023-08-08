#!/usr/bin/python3
import os
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = f'{obj.to_dict()}'

    def save(self):
        with open(self.__file_path, "w") as fh:
            json.dump(self.__objects, fh)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as fh:
                self.__objects = json.load(fh)
