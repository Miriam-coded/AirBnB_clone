#!/usr/bin/python3
"""Defines unit tests for models/base_model.py

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import uuid
import os
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        self.model = BaseModel()

    def test_inst(self):
        """Test instance creation and atribute types"""
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        my_model_dict = self.model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], self.model.id)
        self.assertEqual(my_model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"],
                         self.model.updated_at.isoformat())

    def test_str(self):
        self.assertTrue(str(self.model).startswith('[BaseModel]'))
        self.assertIn(self.model.id, str(self.model))
        self.assertIn(str(self.model.__dict__), str(self.model))

    def test_save(self):
        initial_updated_at = self.model.updated_at
        sleep(1)
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


if __name__ == "__main__":
    unittest.main()
