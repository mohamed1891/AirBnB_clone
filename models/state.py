#!/usr/bin/python3
# Import the modules
from models.base_model import BaseModel
from models import storage

# Define the class State that inherits from BaseModel
class State(BaseModel):
    # Public class attribute
    name: str = ""

    # Override the save method to update the FileStorage
    def save(self):
        # Call the superclass save method
        super().save()
        # Update the FileStorage with the State instance
        storage.new(self)
        # Save the changes to the JSON file
        storage.save()
