#!/usr/bin/python3

# Import the modules
import uuid
from datetime import datetime
from models.__init__ import storage

# Define the class BaseModel
class BaseModel:
    # Class attribute that stores the file path
    FILE_PATH = "file.json"

    # Constructor
    def __init__(self, *args, **kwargs):
        # Initialize the instance attributes
        self.id = str(uuid.uuid4()) # assign a unique id
        self.created_at = datetime.now() # assign the current datetime
        self.updated_at = datetime.now() # assign the current datetime
        # If kwargs is not empty, update the instance attributes with the values from the dictionary
        if kwargs:
            for key, value in kwargs.items():
                # Convert the strings to datetime objects for created_at and updated_at
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                # Set the attribute with the key and value
                setattr(self, key, value)
        # Add the instance to the storage
        storage.new(self)

    # String representation
    def __str__(self):
        # Return a formatted string with the class name, id, and dictionary of the instance
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    # Method to update the updated_at attribute and save the instance to the file
    def save(self):
        # Update the updated_at attribute with the current datetime
        self.updated_at = datetime.now()
        # Save the instance to the file
        storage.save()

    # Method to return a dictionary representation of the instance
    def to_dict(self):
        # Create a copy of the instance dictionary
        dict_copy = self.__dict__.copy()
        # Add the class name to the dictionary
        dict_copy["__class__"] = self.__class__.__name__
        # Convert the datetime objects to strings in ISO format
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        # Return the dictionary
        return dict_copy
