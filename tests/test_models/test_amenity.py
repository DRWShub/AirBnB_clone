#!/usr/bin/python3
"""Testing Amenity class from models.amenity"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os
import sys


class TestAmenity(unittest.TestCase):
    """Unittest cases for Amenity"""
    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_check_subclass(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_amenity_check_class_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_check_attr_type(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))
