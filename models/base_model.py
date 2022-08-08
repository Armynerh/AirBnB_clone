#!/usr/bin/python3
"""This defines a class BaseModel"""

import uuid
from datetime import datetime

class BaseModel:
    """public instances of class BaseModel"""
    
    def __init__(self):
        """constructor for the class"""
        self.old_id = uuid.uuid4()
        self.id= str(self.old_id)
        self.created_at = datetime.now()
        self.updated_at= datetime.now()
    def __str__(self):
        """string repesentation """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'


    def save(self):
        """updates the instant attribute updated_at"""
        self.updated_at=datetime.now()
    def to_dict(self):
        """returns a dictionary that contains all instances of the class"""
        dict_rep =self.__dict__  
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()  
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
    