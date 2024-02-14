#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass


# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
