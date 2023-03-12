#!/usr/bin/python3
"""
Module for Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the Amenity class that inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
