#!/usr/bin/python3

from datetime import datetime
from models import storage

def some_function():
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization method"""
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
            storage.new(self)
            
    def __str__(self):
        """String representation method"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

