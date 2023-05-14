#!/usr/bin/python3
"""Testing City class from models.city"""
import unittest

# import sys module
import sys
#tell interpreter where to look
sys.path.insert(0,"..")
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
        """Unittest cases for City"""

        def setUp(self):
            self.city = City()

        def from_test_city_check_subclass(self):
            self.assertTrue(issubclass(type(self.city), BaseModel))

        def from_test_city_check_class_attr(self):
            self.assertTrue(hasattr(self.city, "name"))

        def from_test_amenity_check_attr_type(self):
            self.assertIs(type(self.amenity.name), str)
            self.assertFalse(bool(getattr(self.amenity, "name")))
