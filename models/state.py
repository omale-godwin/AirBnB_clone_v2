#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state', cascade='all, delete')

    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id = current State.id"""

            city_list = []
            for key, obj in models.storage.all('City').items():
                if obj.state_id == self.id:
                    city_list.append(obj)
            return city_list
