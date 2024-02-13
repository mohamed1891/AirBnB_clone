#!/usr/bin/python3

# Import the modules
from models.base_model import BaseModel
from models import storage

# Define the class City that inherits from BaseModel
class City(BaseModel):
    # Public class attributes
    state_id: str = "" # It will be the State.id
    name: str = ""

    # Override the save method to update the FileStorage
    def save(self):
        # Call the superclass save method
        super().save()
        # Update the FileStorage with the City instance
        storage.new(self)
        # Save the changes to the JSON file
        storage.save()
