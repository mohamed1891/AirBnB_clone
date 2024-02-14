#!usr/bin/python3

# Import the modules
from models.base_model import BaseModel
from models import storage

# Define the class User that inherits from BaseModel
class User(BaseModel):
    # Public class attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    # Override the save method to update the FileStorage
    def save(self):
        # Call the superclass save method
        super().save()
        # Update the FileStorage with the User instance
        storage.new(self)
        # Save the changes to the JSON file
        storage.save()
