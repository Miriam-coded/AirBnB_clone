"""

"""

import models
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInst(unittest.TestCase):
    """

    """
    def test_file_inst_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_inst_args(self):
        with seld.assertRaises(TypeError):
            FileStorage(None)

    def test_stotage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """

    """

    def setUp
