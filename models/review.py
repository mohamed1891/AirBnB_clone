#!/usr/bin/python3

# Import the modules
from models.base_model import BaseModel
from models import storage
from models.place import Place
from models.user import User

# Define the class Review that inherits from BaseModel
class Review(BaseModel):
    # Public class attributes
    place_id: str = "" # It will be the Place.id
    user_id: str = "" # It will be the User.id
    text: str = ""

    # Override the save method to update the FileStorage
    def save(self):
        # Call the superclass save method
        super().save()
        # Update the FileStorage with the Review instance
        storage.new(self)
        # Save the changes to the JSON file
        storage.save()
