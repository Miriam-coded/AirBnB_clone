"""

"""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInst(unittest.TestCase):
    """

    """

    def test_file_inst_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_inst_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """

    """

    __file_path = "file.json"

    @classmethod
    def setUpClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("tmp.json")
        except FileNotFoundError:
            pass


    @classmethod
    def tearDownClass(cls):
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
          pass

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.name = "TestModel"
        self.model.save()
        models.storage.reload()

    def tearDown(self):
        try:
            os.remove(self.__file_path)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_file_path_exists(self):
        self.assertIsInstance(os.path.exists(self.__file_path))

    def test_all(self):
        all_objects = models.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(f"BaseModel.{self.model.id}", all_objects)

    def test_new(self):
        new_model = BaseModel()
        new_model.name = "NewModel"
        models.storage.new(new_model)
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, models.storage.all())

    def test_save(self):
        models.storage.save()
        key = f"BaseModel.{self.model.id}"
        with open(self.__file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(key, data)

    def test_save_with_empty_objs(self):
        FileStorage._FileStorage__objects = {}
        models.storage.save()
        with open(self.__file_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, {})

    def test_reload(self):
        key = f"BaseModel.{self.model.id}"
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        self.assertIn(key, models.storage.all())

    def test_reload_no_file(self):
        try:
            os.remove(self.__file_path)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        self.assertEqual(models.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
