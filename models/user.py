#!/usr/bin/python3
"""
module contains user and its instances
"""


from base_model import BaseModel


class User(BaseModel):
    """
    class controlling user details
    """
    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
