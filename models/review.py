from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""  # empty string: it will be the Place.id
    user_id = ""  # empty string: it will be the User.id
    text = ""  # empty string
