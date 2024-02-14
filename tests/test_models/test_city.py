#!/usr/bin/python3

# Import the modules
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage

# Define the TestCity class
class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_save_method(self):
        # Call the save method
        self.city.save()

        # Check if the superclass save method is called
        self.assertTrue(storage.save.called)

        # Check if the City instance is added to storage
        self.assertIn(self.city.id, storage.all())

    def test_city_attributes(self):
        # Check if the City instance has the expected attributes
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_update_attributes(self):
        # Check if updating attributes works as expected
        new_name = "Updated City Name"
        self.city.name = new_name
        self.assertEqual(self.city.name, new_name)

    def test_city_str_representation(self):
        # Check if the string representation is formatted correctly
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)

    def test_city_to_dict_method(self):
        # Check if the to_dict method returns a valid dictionary
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], self.city.name)

if __name__ == '__main__':
    unittest.main()

