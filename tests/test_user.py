#!/usr/bin/python3
"""User unittests"""
import unittest

# import sys module
import sys
#tell interpreter where to look
sys.path.insert(1,"..")

#import User class
from models.user import User
import datetime
import time


class TestUser(unittest.TestCase):
    """class TestUser"""

    def test_user_class_membership_and_attributes(self):
        """Checking User attrs"""
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

    def test_user_attr_type(self):
        """Checking User attributes value type"""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertEqual(len(user.id), 36)
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_updated_at_matches_created_at_initialization(self):
        """Checking User updated_at is in sync with create_at"""
        user = User()
        self.assertEqual(user.updated_at, user.created_at)

    def test_user_str_method(self):
        """Testing String Methods in User"""
        user = User()
        user_str = user.__str__()
        self.assertIsInstance(user_str, str)
        self.assertEqual(user_str[:6], '[User]')
        self.assertEqual(user_str[7:45], '({})'.format(user.id))
        self.assertDictEqual(eval(user_str[46:]), user.__dict__)

    def test_user_save_method(self):
        """Checking if save method triggers update_at date"""
        user = User()
        time.sleep(0.0001)
        user.save()
        self.assertNotEqual(user.updated_at, user.created_at)

    def test_user_to_dict_method(self):
        """Checking User for dict key values"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['__class__'], type(user).__name__)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)

    def test_user_dict_to_instance_with_kwargs(self):
        """Checking User can instantiate new object with dictionary"""
        user = User()
        user.name = "Betty"
        user.number = 972
        user_dict = user.to_dict()
        new_user = User(**user_dict)
        new_user_dict = new_user.to_dict()
        self.assertFalse(new_user is user)
        self.assertDictEqual(new_user_dict, user_dict)

    def test_user_dict_to_instance_with_empty_kwargs(self):
        """Checking User can instantiate new object with empty dict"""
        user_dict = {}
        new_user = User(**user_dict)
        new_user_dict = new_user.to_dict()
        self.assertIsInstance(new_user, User)
        self.assertIsNotNone(new_user.id)
        self.assertIsNotNone(new_user.created_at)
        self.assertIsNotNone(new_user.updated_at)

if __name__ == '__main__':
    unittest.main()
