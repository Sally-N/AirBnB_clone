#!/usr/bin/python3
"""Defines unittests for User class"""


import models
import unittest
from datetime import datetime
from models.user import User


class TestBaseModel_instantation(unittest.TestCase):
    """Unittests for User class instances"""

    def test_instance_with_no_args(self):
        cls_type = type(User())
        self.assertEqual(User, cls_type)

    def test_new_instance_storage(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_of_type_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime_obj(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime_obj(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_of_type_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_is_of_type_str(self):
        self.assertEqual(str, type(User().password))

    def test_first_name_is_of_type_str(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name_is_of_type_str(self):
        self.assertEqual(str, type(User().last_name))

    def test_new_instance_with_args(self):
        new_obj = User(None, "6")
        self.assertNotIn(None, new_obj.__dict__.values())
        self.assertNotIn("6", new_obj.__dict__.values())

    def test_new_instance_with_kwargs(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = User(id="68976", created_at=dt_iso_format,
                       updated_at=dt_iso_format)
        self.assertEqual(new_obj.id, "68976")
        self.assertEqual(new_obj.created_at, dt)
        self.assertEqual(new_obj.updated_at, dt)

    def test_new_instance_with_args_and_kwargs(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = User(None, id="68976", created_at=dt_iso_format,
                       updated_at=dt_iso_format)
        self.assertNotIn(None, new_obj.__dict__.values())
        self.assertEqual(new_obj.id, "68976")
        self.assertEqual(new_obj.created_at, dt)
        self.assertEqual(new_obj.updated_at, dt)

    def test_str_repr(self):
        new_obj = User()
        new_obj.id = "68976"
        new_obj_str = new_obj.__str__()
        self.assertIn("[User] (68976)", new_obj_str)
        self.assertIn("'id': '68976'", new_obj_str)


class TestBaseModel_save(unittest.TestCase):
    """ Unittests for save method in User class"""

    def test_save_with_arg(self):
        new_obj = User()
        with self.assertRaises(TypeError):
            new_obj.save("NaN")

    def test_saves_to_file(self):
        new_obj = User()
        new_obj.save()
        new_obj_id = new_obj.id
        new_obj_created = new_obj.created_at
        with open("file.json", "r") as f:
            json_str = f.read()
            self.assertIn(new_obj_id, json_str)
            self.assertIn(new_obj_created.isoformat(), json_str)


class TestBaseModel_to_dict(unittest.TestCase):
    """ Unittests for to_dict method in User class"""
    def test_to_dict_with_arg(self):
        new_obj = User()
        with self.assertRaises(TypeError):
            new_obj.to_dict(None)

    def test_to_dict_contains_kwargs(self):
        new_obj = User()
        new_obj.first_name = "Albert"
        new_obj.last_name = "Einstein"
        self.assertIn("Albert", new_obj.to_dict().values())
        self.assertIn("Einstein", new_obj.to_dict().values())

    def test_to_dict_type_is_dict(self):
        new_obj = User()
        self.assertTrue(dict, type(new_obj.to_dict()))

    def test_to_dict_correct_output(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = User(id="68976", created_at=dt_iso_format,
                       updated_at=dt_iso_format)
        expected = {
            "__class__": "User",
            "id": "68976",
            "created_at": dt_iso_format,
            "updated_at": dt_iso_format
        }
        self.assertEqual(expected, new_obj.to_dict())


if __name__ == "__main__":
    unittest.main()
