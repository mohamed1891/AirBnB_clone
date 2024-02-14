#!/usr/bin/python3

# Import the modules
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage

# Define the TestReview class
class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_save_method(self):
        # Call the save method
        self.review.save()

        # Check if the superclass save method is called
        self.assertTrue(storage.save.called)

        # Check if the Review instance is added to storage
        self.assertIn(self.review.id, storage.all())

    def test_review_attributes(self):
        # Check if the Review instance has the expected attributes
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_update_attributes(self):
        # Check if updating attributes works as expected
        new_text = "Updated Review Text"
        self.review.text = new_text
        self.assertEqual(self.review.text, new_text)

    def test_review_str_representation(self):
        # Check if the string representation is formatted correctly
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)

    def test_review_to_dict_method(self):
        # Check if the to_dict method returns a valid dictionary
        review_dict = self.review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['text'], self.review.text)

if __name__ == '__main__':
    unittest.main()
