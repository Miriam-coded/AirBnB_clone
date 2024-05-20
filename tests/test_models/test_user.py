"""
Module to test the User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
import os

class TestUser(unittest.TestCase):
    """
    Test cases for the User class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.user = User()
        self.user.email = "test@test.com"
        self.user.password = "testpass"
        self.user.first_name = "Test"
        self.user.last_name = "User"

    def tearDown(self):
        """
        Clean up test environment
        """
        del self.user
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_is_instance(self):
        """
        Test that User is an instance of BaseModel
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        Test attributes of the User class
        """
        self.assertEqual(self.user.email, "test@test.com")
        self.assertEqual(self.user.password, "testpass")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_save_user(self):
        """Test saving User instance to file storage."""
        self.user.save()
        key = f"User.{self.user.id}"
        self.assertIn(key, storage.all())
        saved_user = storage.all()[key]
        self.assertEqual(saved_user.email, "test@test.com")
        self.assertEqual(saved_user.password, "testpass")
        self.assertEqual(saved_user.first_name, "Test")
        self.assertEqual(saved_user.last_name, "User")

    def test_to_dict(self):
        """Test to_dict method of User class."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "test@test.com")
        self.assertEqual(user_dict["password"], "testpass")
        self.assertEqual(user_dict["first_name"], "Test")
        self.assertEqual(user_dict["last_name"], "User")
        self.assertEqual(user_dict["__class__"], "User")

    def test_recreation_from_dict(self):
        """Test creating User instance from dictionary."""
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(new_user.email, "test@test.com")
        self.assertEqual(new_user.password, "testpass")
        self.assertEqual(new_user.first_name, "Test")
        self.assertEqual(new_user.last_name, "User")
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)


if __name__ == "__main__":
    unittest.main()
