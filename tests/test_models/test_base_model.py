#!/usr/bin/python3
"""test casses for the unittests"""

import unittest
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    """tests if object is part of BaseModel""" 
    def test_base_init(self):
      base_class= BaseModel()
      self.assertIsInstance(base_class, BaseModel)
