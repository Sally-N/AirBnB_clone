#!/usr/bin/python3
"""Defines unittests for FileStorage class"""


import models
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage_instantation(unittest.TestCase):
    """Unittests for FileStorage class instances"""

    def test_cls_dict_is_of_type_dict(self):
        self.assertEqual(dict, type(FileStorage().cls_dict))

    def test_file_path_is_file(self):
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test_objects_is_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_is_FileStorage_instance(self):
        self.assertTrue(isinstance(models.storage, FileStorage))

    def test_new_instance(self):
        new_obj = FileStorage()
        self.assertTrue(isinstance(new_obj, FileStorage))

    def test_new_instance_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage("file.json")


class TestFileStorage_behaviour(unittest.TestCase):
    """Unittests for FileStorage class behaviour"""

    def test_all_method_return_type(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        new_obj = BaseModel()
        models.storage.new(new_obj)
        self.assertIn("BaseModel." + new_obj.id, models.storage.all().keys())
        self.assertIn(new_obj, models.storage.all().values())

    def test_save_method(self):
        new_obj = BaseModel()
        models.storage.new(new_obj)
        models.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            json_dict = json.load(f)
            key = "BaseModel.{}".format(new_obj.id)
            self.assertIn(key, json_dict.keys())

    def test_save_method_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(BaseModel())

    def test_reload_method(self):
        new_obj = BaseModel()
        models.storage.new(new_obj)
        models.storage.save()
        models.storage.reload
        objs = FileStorage._FileStorage__objects
        key = "BaseModel.{}".format(new_obj.id)
        self.assertIn(key, objs)

    def test_reload_method_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload("BaseModel.360f1574-68e3-456c-a43e")


if __name__ == "__main__":
    unittest.main()
