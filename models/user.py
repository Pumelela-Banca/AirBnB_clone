#!/usr/bin/python3
"""
module contains user and its instances
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    class controlling user details
    """
    self.email = ''
    self.password = ''
    self.first_name = ''
    self.last_name = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
