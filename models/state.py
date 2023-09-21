#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id = current State.id"""
            from models import storage
            from models.city import City

            city_dict = storage.all(City)
            city_list = []

            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
