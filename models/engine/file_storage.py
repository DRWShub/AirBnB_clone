#!/usr/bin/pyhton3

import json


class FileStorage():
    """serializes and deserializes instances to json file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects in class Filestorage"""
        return FileStorage.__objects

    def new(self, obj):
        """sets the __objects with obj key"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes __objects to JSON file path"""
        json_objects = {}
        for k, v in FileStorage.__objects.items():
            json_objects[k] = v.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes json file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}

        try:
            jsobj = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as rf:
                jsobj = json.load(rf)
            for key, val in jsobj.items():
                self.all()[key] = classes[val["__class__"]](**val)

        except FileNotFoundError:
            pass

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
