#!/usr/bin/python3
'''define class BaseModel'''
import uuid
import datetime
import models

class BaseModel:
    '''class BaseModel'''
    def __init__(self, *args, **kwargs):
        '''constructor method executed every
           time a new instance is created
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self,key, datetime.datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, kwargs[key])
        else:
            models.storage.new(self)

    def __str__(self):
        ''' return printable string represantation
            of an instance
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute updated_at
           with the current datetime
        '''
        self.updated_at = datetime.datetime.now()
        models.storage.save()


    def to_dict(self):
        '''returns a dictionary containing all keys/values
           of __dict__ of the instance:
           * by using self.__dict__, only instance attributes set will be returned
           * a key __class__ must be added to this dictionary with the
           class name of the object created_at and updated_at must be
           converted to string object in ISO format:
           format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
           you can use isoformat() of datetime object
        '''
        dict1 = self.__dict__.copy()
        dict1['created_at'] = self.created_at.isoformat()
        dict1['updated_at'] = self.updated_at.isoformat()
        dict1['__class__'] = self.__class__.__name__
        return dict1
