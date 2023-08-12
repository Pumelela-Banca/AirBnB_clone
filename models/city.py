#!/usr/bin/python3
"""
module contains city information and its methods
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class with city attributes
    """
    state_id = ""
    name = ""
    def __init__(self, **kwargs):
        """constructor method"""
        super().__init__(**kwargs)
