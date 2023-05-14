#!/usr/bin/python3
"""Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherits all the attributes of class BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
