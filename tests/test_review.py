#!/usr/bin/python3
"""Review unittests"""
import unittest

# import sys module
import sys
# tell interpreter where to look
sys.path.insert(1,"..")

# import review class
from models.review import Review
import datetime
import time


class TestReview(unittest.TestCase):
    """class TestReview"""

    def test_review_class_membership_and_attributes(self):
        """Checking Review attrs"""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.place_id)
        self.assertIsNotNone(review.user_id)
        self.assertIsNotNone(review.text)

    def test_review_attr_type(self):
        """Checking Review attributes value type"""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertEqual(len(review.id), 36)
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_updated_at_matches_created_at_initialization(self):
        """Checking Review updated_at is in sync with create_at"""
        review = Review()
        self.assertEqual(review.updated_at, review.created_at)

    def test_review_str_method(self):
        """Testing String Methods in Review"""
        review = Review()
        review_str = review.__str__()
        self.assertIsInstance(review_str, str)
        self.assertEqual(review_str[:8], '[Review]')
        self.assertEqual(review_str[9:47], '({})'.format(review.id))
        self.assertDictEqual(eval(review_str[48:]), review.__dict__)

    def test_review_save_method(self):
        """Checking if save method triggers update_at date"""
        review = Review()
        time.sleep(0.0001)
        review.save()
        self.assertNotEqual(review.updated_at, review.created_at)

    def test_review_to_dict_method(self):
        """Checking Review for dict key values"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['__class__'], type(review).__name__)
        self.assertEqual(
            review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(
            review_dict['updated_at'], review.updated_at.isoformat())
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)

    def test_review_dict_to_instance_with_kwargs(self):
        """Checking Review can instantiate new object with dictionary"""
        review = Review()
        review.name = "Betty"
        review.number = 972
        review_dict = review.to_dict()
        new_review = Review(**review_dict)
        new_review_dict = new_review.to_dict()
        self.assertFalse(new_review is review)
        self.assertDictEqual(new_review_dict, review_dict)

    def test_review_dict_to_instance_with_empty_kwargs(self):
        """Checking Review can instantiate new object with empty dict"""
        review_dict = {}
        new_review = Review(**review_dict)
        new_review_dict = new_review.to_dict()
        self.assertIsInstance(new_review, Review)
        self.assertIsNotNone(new_review.id)
        self.assertIsNotNone(new_review.created_at)
        self.assertIsNotNone(new_review.updated_at)

if __name__ == '__main__':
    unittest.main()
