from sqlalchemy import create_engine
from slqalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from os import getenv
import models

class DBStorage:
    """Class that manages storage of hbnb models using sqlalchemy and mysql"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the db connection"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """Queries all objects of a specific class"""


        objects = {}
        if cls:
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for cls in models.storage.classes:
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds object to current db"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of current db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the db and creates current db session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Closes the current session"""
        self.__session.remove()