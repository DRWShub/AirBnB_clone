#!/usr/bin/python3
"""BaseModel for all other classes"""
import uuid
from datetime import datetime
from models import storage

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():

    """base model"""
    def __init__(self, *args, **kwargs):
        """initialization with args and kwargs"""
        if kwargs:
            del(kwargs['__class__'])
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict.update({'__class__': type(self).__name__})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
