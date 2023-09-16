#!/usr/bin/python3
"""
class Review that inherits from BaseModel
"""
import models.base_model


class Review(models.base_model.BaseModel):
    """
        Reviw Class Declaration
    """
    text = ""
    place_id = ""
    user_id = ""
