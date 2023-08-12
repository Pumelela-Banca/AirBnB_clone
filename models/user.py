#!/usr/bin/python3
"""
module contains user and its instances
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    class controlling user details
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
