#!/usr/bin/python3

# Import the modules
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Define the TestFileStorage class
class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage
        self.file_storage = FileStorage()

    def tearDown(self):
        # Remove the file.json after each test
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        # Test if all method returns the __objects dictionary
        result = self.file_storage.all()
        self.assertEqual(result, self.file_storage._FileStorage__objects)

    def test_new_method(self):
        # Test if new method adds an object to __objects
        obj = BaseModel()
        self.file_storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.file_storage._FileStorage__objects)

    def test_save_and_reload_methods(self):
        # Test if save and reload methods work correctly
        obj1 = BaseModel()
        obj2 = User()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Save the objects to the JSON file
        self.file_storage.save()

        # Reload the objects from the JSON file
        new_file_storage = FileStorage()
        new_file_storage.reload()

        # Check if the reloaded objects match the original objects
        self.assertEqual(new_file_storage.all(), self.file_storage.all())

    def test_attributes_method(self):
        # Test if attributes method returns valid attributes for each class
        result = self.file_storage.attributes()
        expected_result = {
            "BaseModel": {"id": str, "created_at": str, "updated_at": str},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str, "user_id": str, "name": str, "description": str,
                      "number_rooms": int, "number_bathrooms": int, "max_guest": int,
                      "price_by_night": int, "latitude": float, "longitude": float,
                      "amenity_ids": list},
            "Review": {"place_id": str, "user_id": str, "text": str}
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
