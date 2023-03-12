#!/usr/bin/python3
"""
Contains the City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class to represent a city
    """
    state_id = ""  # string - empty string: it will be the State.id
    name = ""  # string - empty string
