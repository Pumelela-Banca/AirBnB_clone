#!/usr/bin/python3
"""
module contains review information and properties
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    class for reviewing by users
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
