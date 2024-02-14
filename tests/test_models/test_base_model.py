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
        self.base_model = BaseModel()
        storage.reset()

    def tearDown(self):
        if os.path.exists(FileStorage.FILE_PATH):
            os.remove(FileStorage.FILE_PATH)

    def test_create_instance(self):
        self.assertIsInstance(self.base_model, BaseModel)

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
        # Save the instance to the file
        self.base_model.save()
        # Reload the storage
        storage.reload()
        # Check if the instance is loaded
        self.assertIn(self.base_model.id, storage.all())


if __name__ == '__main__':
    unittest.main()
