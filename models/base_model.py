#!/usr/bin/python3

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initializes instance attributes"""
        self.storage = storage()
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.storage.new(self)

    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        self.storage.save()

    def __str__(self):
        """String representation method"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Dictionary representation method"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
