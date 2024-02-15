#!/usr/bin/python3

# Import the modules
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
from models.engine.file_storage import FileStorage

# Define the TestPlace class
class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.place = Place()
        self.place.name = "Place"
        self.place.city_id = "city_id"
        self.place.user_id = "user_id"
        self.place.save()
        self.storage = FileStorage()
        self.storage.new(self.place)
        self.storage.save()

    def test_save_method(self):
        """Test Place.save method"""
        Place.save.assert_called_once()
        self.assertTrue(self.storage.save.called)
        
    def test_place_attributes(self):
        # Check if the Place instance has the expected attributes
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_update_attributes(self):
        # Check if updating attributes works as expected
        new_name = "Updated Place Name"
        new_description = "Updated Description"
        self.place.name = new_name
        self.place.description = new_description
        self.assertEqual(self.place.name, new_name)
        self.assertEqual(self.place.description, new_description)

    def test_place_str_representation(self):
        # Check if the string representation is formatted correctly
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_place_to_dict_method(self):
        # Check if the to_dict method returns a valid dictionary
        place_dict = self.place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], self.place.name)

if __name__ == '__main__':
    unittest.main()
