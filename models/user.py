#!/usr/bin/python3
"""
class User that inherits from BaseModel
"""
import models.base_model


class User(models.base_model.BaseModel):
    """
        User  Class Declaration
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
