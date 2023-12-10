#!/usr/bin/python3
"""A class User that inherits from BaseModel."""
from models.base_model import BaseModel

class User(Basemodel):
    """ A class User.

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
