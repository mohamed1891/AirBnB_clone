#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key,
                                datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """String representation method"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Dictionary representation method"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
