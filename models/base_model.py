#!/usr/bin/python3
"""Define a class BaseModel."""
import models
from uuid import uuid4
from datetime import datetime

Class BaseModel:
    """Represents the Basemodel of the project"""
    def __init__(self, *args, **kwargs):
        """ Initializing BaseModel

        Args:
            *args: unused
            **kwargs(dictionary): Atrributes key/value pairing.
        """
        self.id = str(uuid())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Updating updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the BaseModel instance dictionary.

        The key/value pair __class__ represents the class name of the object.
        """
        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
