#!/usr/bin/python3

# Import the modules
import datetime
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test that the Amenity class has the correct attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_attribute_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
        self.assertTrue(amenity.name)
        self.assertAlmostEqual(amenity.price_by_night, 0)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_name_default_value(self):
        """Test that the name attribute has a default value of None"""
        amenity = Amenity()
        self.assertIsNone(amenity.name)

if __name__ == "__main__":
    unittest.main()
