#!/usr/bin/python3

# Import the modules
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage

# Define the TestState class
class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_save_method(self):
        # Call the save method
        self.state.save()

        # Check if the superclass save method is called
        self.assertTrue(storage.save.called)

        # Check if the State instance is added to storage
        self.assertIn(self.state.id, storage.all())

    def test_state_attributes(self):
        # Check if the State instance has the expected attributes
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_state_update_attributes(self):
        # Check if updating attributes works as expected
        new_name = "Updated State Name"
        self.state.name = new_name
        self.assertEqual(self.state.name, new_name)

    def test_state_str_representation(self):
        # Check if the string representation is formatted correctly
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)

    def test_state_to_dict_method(self):
        # Check if the to_dict method returns a valid dictionary
        state_dict = self.state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], self.state.name)

if __name__ == '__main__':
    unittest.main()
