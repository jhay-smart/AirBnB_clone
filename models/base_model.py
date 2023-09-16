#!/usr/bin/python3
"""
The BaseModel class has different attributes and methods reusable by other classes
"""
import uuid
from datetime import datetime as dt
import models
import json
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        Summary:Initailizing and defining the Base class other class can inherit
        Attributes:
            id -> Public instance attributes
            created_at -> Public instance attributes
            updated_at -> Public instance attributes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the object/instance attributes
            id: contains the object's identification
            created_at: the datetime in which the object was created
            updated_at: the datetime in which the object was modified
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = dt.strptime(value, timeformat)
                elif key == "__class__":
                    pass
                elif key != "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """ Writing the __str__ method """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Public instance methods:
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """ Public instance methods
            returns a dictionary containing all keys/values
            of __dict__ of the instance with self.__dict__
            we are making a copy.
            This method will be the first piece of the
            serialization/deserialization process: create a dictionary
            representation with “simple object type” of our BaseModel
        """
        dic_BaseClass = self.__dict__.copy()
        dic_BaseClass["__class__"] = self.__class__.__name__
        dic_BaseClass["created_at"] = self.created_at.isoformat()
        dic_BaseClass["updated_at"] = self.updated_at.isoformat()
        return dic_BaseClass
