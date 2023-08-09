#!/usr/bin/python3
"""
module contains city information and its classes
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    class with city attributes
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state_id = ""
        self.name = ""
