#!/usr/bin/python3
"""contains BaseModel class"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Super-class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance

        Args:
            *args (any): Unused
            **kwargs (dict): key/value pairs of attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time
            self._import_storage().new(self)

    def __str__(self):
        """Return the str representation of the BaseModel Instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.utcnow()
        self._import_storage().save()

    def _import_storage(self):
        """Import storage method"""
        from models import storage
        return storage
