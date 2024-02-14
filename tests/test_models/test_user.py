#!/usr/bin/python3

# Import the modules
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage

# Define the TestUser class
class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_save_method(self):
        # Call the save method
        self.user.save()

        # Check if the superclass save method is called
        self.assertTrue(storage.save.called)

        # Check if the User instance is added to storage
        self.assertIn(self.user.id, storage.all())

    def test_user_attributes(self):
        # Check if the User instance has the expected attributes
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_update_attributes(self):
        # Check if updating attributes works as expected
        new_email = "updated@example.com"
        self.user.email = new_email
        self.assertEqual(self.user.email, new_email)

    def test_user_str_representation(self):
        # Check if the string representation is formatted correctly
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_user_to_dict_method(self):
        # Check if the to_dict method returns a valid dictionary
        user_dict = self.user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], self.user.email)

if __name__ == '__main__':
    unittest.main()
