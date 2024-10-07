from uuid import uuid4
from sqlalchemy import Column, String, LargeBinary

from .db_settings import SQLModel


class ArrayModel(SQLModel):
    __tablename__ = 'embeddings'

    id = Column(
        String,
        primary_key=True,
        default=str(uuid4())
    )

    shape = Column(
        String,
        nullable=False
    )

    array_data = Column(
        LargeBinary,
        nullable=False
    )

    def __repr__(self):
        return f"<ArrayModel(name={self.id})>"
