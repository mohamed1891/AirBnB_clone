#!/usr/bin/python3

# Import the modules
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os

# Define the TestBaseModel class
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Sets up the test fixture for the BaseModel tests"""
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        """Tears down the test fixture for the BaseModel tests"""
        self.storage = None

    def test_create_instance(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model)
        self.assertEqual(self.base_model.id, self.base_model.id)

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        expected_dict = {
            "__class__": "BaseModel",
            "id": self.base_model.id,
            "created_at": self.base_model.created_at.isoformat(),
            "updated_at": self.base_model.updated_at.isoformat(),
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_save_method(self):
        self.base_model.save()
        self.storage.reload()
        self.assertIn(self.base_model.id,
                      self.storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
