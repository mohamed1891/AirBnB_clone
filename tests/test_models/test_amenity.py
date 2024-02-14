#!/usr/bin/python3

# Import the modules
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity

# Define the TestAmenity class
class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    @patch('models.storage.save')
    def test_save_method(self, mock_storage_save):
        # Assuming 'save' method is implemented in the Amenity class
        # You can add test cases to check if saving works as expected

        # Call the save method
        self.amenity.save()

        # Check if the superclass save method is called
        self.assertTrue(mock_storage_save.called)

        # Check if the Amenity instance is added to storage
        self.assertIn(self.amenity.id, storage.all())


if __name__ == '__main__':
    unittest.main()
