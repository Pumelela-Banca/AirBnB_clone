#!/usr/bin/python3
"""
module contains state class and its methods
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    class that stores state
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = ""
