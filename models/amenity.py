#!/usr/bin/python3

# Import the modules
from models.base_model import BaseModel
from models import storage

# Define the class Amenity that inherits from BaseModel
class Amenity(BaseModel):
    # Public class attribute
    name: str = ""

    # Override the save method to update the FileStorage
    def save(self):
        # Call the superclass save method
        super().save()
        # Update the FileStorage with the Amenity instance
        storage.new(self)
        # Save the changes to the JSON file
        storage.save()
