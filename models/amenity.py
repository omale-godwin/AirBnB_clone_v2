#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class to store amenity info"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    def get_place_amenities(self):
        """Retrieves related place PlaceAmenity objects"""
        from models.place import PlaceAmenity
        return PlaceAmenity.query.filter_by(amenity_id=self.id).all()


