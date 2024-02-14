#!/usr/bin/python3

# Import the modules
import os
import json
import datetime

# Placeholder for the BaseModel class definition
class BaseModel:
    pass

# Placeholder for the User class definition
class User:
    pass

# Placeholder for the Place class definition
class Place:
    pass

# Placeholder for the State class definition
class State:
    pass

# Placeholder for the City class definition
class City:
    pass

# Placeholder for the Amenity class definition
class Amenity:
    pass

# Placeholder for the Review class definition
class Review:
    pass

# Define the class FileStorage
class FileStorage:
    # Class attributes
    __file_path = "file.json"
    __objects = {}

    # Define a dictionary of valid classes
    def classes(self):
        return {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

    # Methods
    def all(self):
        # Return the dictionary of objects
        return self.__objects

    def new(self, obj):
        # Add the object to the dictionary of objects
        # The key is the class name and id, and the value is the object
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        # Save the objects to the JSON file
        # Create an empty dictionary to store the serialized objects
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        # Deserializes the JSON file to __objects
        # (only if the JSON file (__file_path) exists; otherwise,
        # do nothing. If the file doesn’t exist, no exception should be raised)
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            self.__objects = obj_dict

    def attributes(self):
        # Returns the valid attributes and their types for classname.
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
