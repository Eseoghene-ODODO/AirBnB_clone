#!/usr/bin/python3
 import uuid
 from datetime import datetime


 class BaseModel:
     """Defines all common attributes/methods for other classes"""

     def _init_(self, *args, **kwargs):
         """Initialize the BaseModel instance"""
         if kwargs:
             """Set attributes from dictionary"""
             for key, value in kwargs.items():
                 if key == '_class_':
                     continue
                 if key in ['created_at', 'updated_at']:
                     value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                 setattr(self, key, value)
         else:
             """Create new instance with id and created_at """
             self.id = str(uuid.uuid4())
             self.created_at = self.updated_at = datetime.now()

     def _str_(self):
         """Return string representation of the BaseModel instance"""

         return f"[{self._class.name}] ({self.id}) {self.dict_}"

     def save(self):
         """Update the public instance attribute updated_at with the current datetime"""

         self.updated_at = datetime.datetime.now()

     def to_dict(self):
         """Return a dictionary containing all keys/values of dict of the instance"""

         # create a copy of the instance's dict attribute
         obj_dict = self._dict_.copy()

         # add the 'class' key to the dictionary
         obj_dict['_class'] = self.class.name_

         # convert the datetime attributes to string objects in ISO format
         obj_dict['created_at'] = self.created_at.isoformat()
         obj_dict['updated_at'] = self.updated_at.isoformat()
