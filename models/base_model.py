#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.key = datetime.datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.key = datetime.datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.key = kwargs[key]

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict1 = self.__dict__
        dict1['created_at'] = self.created_at.isoformat()
        dict1['updated_at'] = self.updated_at.isoformat()
        dict1['__class__'] = self.__class__.__name__
        return dict1
