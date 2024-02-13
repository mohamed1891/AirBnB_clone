#!usr/bin/python3

# Import the modules
from models.base_model import BaseModel
from models import storage

# Define the class Place that inherits from BaseModel
class Place(BaseModel):
    # Public class attributes
    city_id: str = "" # It will be the City.id
    user_id: str = "" # It will be the User.id
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = [] # It will be the list of Amenity.id later

    # Override the save method to update the FileStorage
    def save(self):
        # Call the superclass save method
        super().save()
        # Update the FileStorage with the Place instance
        storage.new(self)
        # Save the changes to the JSON file
        storage.save()
