#!/usr/bin/python3
"""City module"""
import datetime
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name")
        self.state = kwargs.get("state")
        self.country = kwargs.get("country")
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
  
    def delete(self):
        """Delete a City instance"""
        del FileStorage.__objects[self.id]
