#!/usr/bin/python3
"""Test module for User class"""
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """TestUser class"""

    def test_instance_creation(self):
        """Test creating a User instance"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)


if __name__ == '__main__':
    unittest.main()
