#!/usr/bin/python3
""" Module containing BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel Class """

    def __init__(self, *args, **kwargs):
        from models import storage
        """ Initializes a BaseModel instance """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ Returns a string representation of the BaseModel instance """
        return "[{}] ({}) {}".format(type(self.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Saves the BaseModel instance """
        self.updated_at=datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the BaseModel instance """
        dictionary=self.__dict__.copy()
        dictionary['created_at']=self.created_at.isoformat()
        dictionary['updated_at']=self.updated_at.isoformat()
        dictionary['__class__']=type(self).__name__
        return dictionary
