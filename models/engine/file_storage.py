#!/usr/bin/python3

import json
import os
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.objects = {}

    def all(self, class_name):
        """Returns all stored objects"""
        if class_name in self.objects:
            return self.objects[class_name]
        else:
            return []
    
    def new(self, obj):
        """Saves a new object"""
        class_name = obj.__class__.__name__
        if class_name not in self.objects:
            self.objects[class_name] = []
        self.objects[class_name].append(obj)

    def save(self):
        """Saves all objects to the JSON file"""
        new_dict = {}
        for class_name in self.classes():
            new_dict[class_name] = {}
            for obj in self.all(class_name):
                new_dict[class_name][obj.id] = obj.to_dict()
        with open(self.file_path, 'w') as f:
            json.dump(new_dict, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        try:
            with open(self._FileStorage__file_path, 'r') as f:
                data = f.read()
                print(f"File Path: {self._FileStorage__file_path}")
                print(f"File Content: {data}")
                if data:
                    self._FileStorage__objects = json.loads(data)
                else:
                    self._FileStorage__objects = {}
        except FileNotFoundError:
            pass
