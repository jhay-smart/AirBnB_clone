#!/usr/bin/python3
"""
class City that inherits from BaseModel
"""
import models.base_model


class City(models.base_model.BaseModel)):
    """
       City Class declration
            name string - empty string
            state_id - empty string (it will be the State.id)
    """
    name = ""
    state_id = ""
