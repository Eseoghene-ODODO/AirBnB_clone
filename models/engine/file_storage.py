#!/usr/bin/env python3
import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_dict in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
