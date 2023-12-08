#!/usr/bin/python3#
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

Class FileStorage:
    """ Class that seriaizes the  instances to a JSON file 
    and deserializes JSON file to instances

    Attributes:
        __file_path: string - path to the JSON file.
        __objects: dictionary - will store all objects by <class name>.id
    
    """
    self.__file_path = "file.json"
    self.__objects = ""
    
    def all(self):
        """ returns the dictionary __objects"""
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
    def reload(self):
        """deserializes the JSON file to __objects"""
