#!/usr/bin/python3
"""Defines the file storage engine module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """File storage class

    serializes instances of BaseModel to a JSON file
    deserializes JSON file to BaseModel instances
    """

    __file_path = "file.json"
    __objects = {}
    cls_dict = {"BaseModel": BaseModel} 

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        obj_id = obj.id
        obj_key = "{}.{}".format(obj_cls_name, obj_id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = FileStorage.__objects
        output = {}
        path = FileStorage.__file_path
        for key, value in obj_dict.items():
            output[key] = value.to_dict()
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(output, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        path = FileStorage.__file_path
        try:
            with open(path, "r", encoding="utf-8") as json_file:
                json_dict = json.load(json_file)
                for value in json_dict.values():
                    cls_name = value["__class__"]
                    obj = FileStorage.cls_dict[cls_name](**value)
                    self.new(obj)
        except FileNotFoundError:
            return
