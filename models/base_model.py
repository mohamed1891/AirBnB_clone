#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Represents the base model of the AirBnB clone project.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        # assign with an uuid when an instance is created
        self.id = str(uuid4())
        # assign with the current datetime when an instance is created
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            # set attributes from the given dictionary
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            # add the instance to the storage
            models.storage.new(self)

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        # should print: [<class name>] (<self.id>) <self.__dict__>
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates updated_at with the current datetime,
        and save to storage.
        """
        # updates the public instance attribute updated_at with the current datetime
        self.updated_at = datetime.now()
        # save to storage
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance,
        makes the object ready for serialization.
        """
        # create a copy of the instance's dictionary
        dict = self.__dict__.copy()
        # convert created_at and updated_at to string object in ISO format
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        # add a key __class__ with the class name of the object
        dict["__class__"] = self.__class__.__name__
        return dict

    @classmethod
    def from_dict(cls, dict):
        """
        Creates an instance of the class from a dictionary.

        Args:
            dict (dict): A dictionary containing keys/values
            of attributes.

        Returns:
            An instance of the class.
        """
        # check if the dictionary has the correct class name
        if "__class__" in dict:
            class_name = dict.pop("__class__")
            if class_name == cls.__name__:
                # create an instance of the class with the given attributes
                return cls(**dict)
            else:
                # raise an error if the class name is incorrect
                raise ValueError("Incorrect class name in dictionary")
        else:
            # raise an error if the class name is not provided
            raise ValueError("No class name provided in dictionary")
