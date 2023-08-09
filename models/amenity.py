#!/usr/bin/python3
"""
module contains amenity information and its classes
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class with amenity information
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = ""
