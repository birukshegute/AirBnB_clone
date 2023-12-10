#!/usr/bin/python3
"""file containing class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review.
    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string"""
    place_id = ""
    user_id = ""
    text = ""
