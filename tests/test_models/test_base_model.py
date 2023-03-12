#!/usr/bin/python3
"""Defines unittests for BaseModel class"""


import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantation(unittest.TestCase):
    """Unittests for BaseModel class instances"""

    def test_new_instance_with_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_of_type_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime_obj(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime_obj(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_new_instance_with_args(self):
        new_obj = BaseModel(None)
        self.assertNotIn(None, new_obj.__dict__.values())

    def test_new_instance_with_kwargs(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = BaseModel(id="68976", created_at=dt_iso_format, updated_at=dt_iso_format)
        self.assertEqual(new_obj.id, "68976")
        self.assertEqual(new_obj.created_at, dt)
        self.assertEqual(new_obj.updated_at, dt)

if __name__ == "__main__":
    unittest.main()
