#!/usr/bin/python3
"""State unittests"""
import unittest

# import sys module
import sys
# tell interpreter where to look
sys.path.insert(1,"..")

# import State class 
from models.state import State
import datetime
import time


class TestState(unittest.TestCase):
    """class TestState"""

    def test_state_class_membership_and_attributes(self):
        """Checking State class attrs"""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertIsInstance(state, State)
        self.assertIsNotNone(state.name)

    def test_state_attr_type(self):
        """Checking State attributes value type"""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertEqual(len(state.id), 36)
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)
        self.assertIsInstance(state.name, str)

    def test_state_updated_at_matches_created_at_initialization(self):
        """Checking State updated_at is in sync with create_at"""
        state = State()
        self.assertEqual(state.updated_at, state.created_at)

    def test_state_str_method(self):
        """Testing String Methods in State"""
        state = State()
        state_str = state.__str__()
        self.assertIsInstance(state_str, str)
        self.assertEqual(state_str[:7], '[State]')
        self.assertEqual(state_str[8:46], '({})'.format(state.id))
        self.assertDictEqual(eval(state_str[47:]), state.__dict__)

    def test_state_save_method(self):
        """Checking if save method triggers update_at date"""
        state = State()
        time.sleep(0.0001)
        state.save()
        self.assertNotEqual(state.updated_at, state.created_at)

    def test_state_to_dict_method(self):
        """Checking State for dict key values"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['__class__'], type(state).__name__)
        self.assertEqual(
            state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(
            state_dict['updated_at'], state.updated_at.isoformat())
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)

    def test_state_dict_to_instance_with_kwargs(self):
        """Checking State can instantiate new object with dictionary"""
        state = State()
        state.name = "Betty"
        state.number = 972
        state_dict = state.to_dict()
        new_state = State(**state_dict)
        new_state_dict = new_state.to_dict()
        self.assertFalse(new_state is state)
        self.assertDictEqual(new_state_dict, state_dict)

    def test_state_dict_to_instance_with_empty_kwargs(self):
        """Checking State can instantiate new object with empty dict"""
        state_dict = {}
        new_state = State(**state_dict)
        new_state_dict = new_state.to_dict()
        self.assertIsInstance(new_state, State)
        self.assertIsNotNone(new_state.id)
        self.assertIsNotNone(new_state.created_at)
        self.assertIsNotNone(new_state.updated_at)

if __name__ == '__main__':
    unittest.main()
