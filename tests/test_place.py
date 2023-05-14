#!/usr/bin/python3
"""Testing Place class from models.place"""
import unittest

# import sys module
import sys
#tell interpreter where to look
sys.path.insert(0,"..")

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
        """Unittest cases for Place"""

        def setUp(self):
            self.place = Place()
            self.attr_list = ["name", "user_id", "city_id", "description",
                    "number_bathrooms", "max_guest", "number_rooms",
                    "price_by_night", "latitude", "longitude", "amenity_ids"]

        def test_from_place_check_class_attr(self):
            for attr in self.attr_list:
                self.assertTrue(hasattr(Place, attr))

        def test_from_place_check_class_type(self):
            self.assertIs(type(self.place.name), str)
            self.assertIs(type(self.place.city_id), str)
            self.assertIs(type(self.place.user_id), str)
            self.assertIs(type(self.place.description), str)
            self.assertIs(type(self.place.number_bathrooms), int)
            self.assertIs(type(self.place.max_guest), int)
            self.assertIs(type(self.place.number_rooms), int)
            self.assertIs(type(self.place.price_by_night), int)
            self.assertIs(type(self.place.latitude), float)
            self.assertIs(type(self.place.longitude), float)
            self.assertIs(type(self.place.amenity_ids), lis)

            for attr in self.attr_list:
                self.assertFalse(bool(getattr(self.place, attr)))

        def test_from_place_check_class_methos_place(self):
            self.assertTrue(issubclass(type(self.place), BaseModel))
