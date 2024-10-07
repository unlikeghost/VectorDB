from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import DeclarativeBase
from typing import Dict, Any, List


class SQLModel(DeclarativeBase):

    @classmethod
    def get_schema(cls) -> str:

        _schema = cls.__mapper__.selectable.schema
        if _schema is None:
            raise ValueError("Cannot identify model")
        return _schema

    @classmethod
    def get_tablename(cls) -> str:
        return cls.__tablename__

    @classmethod
    def get_field_names(cls) -> List[str]:
        return cls.__table__.columns.keys()

    def to_dict(self) -> Dict[str, Any]:
        _dict: Dict[str, Any] = dict()

        for key in self.__mapper__.c.keys():
            _dict[key] = getattr(self, key)
        return _dict


# Base class for all models
Base = SQLModel()


def get_engine(database_url='sqlite:///test.db'):
    engine = create_engine(database_url)
    return engine


def create_tables(engine):
    """Creates all tables using the models defined."""
    Base.metadata.create_all(engine)


def get_session(engine):
    """Creates and returns a new session."""
    Session = sessionmaker(bind=engine)
    return Session()
