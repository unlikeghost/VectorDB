import ast
from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import Session

from VectorDB._array_convertion import *
from VectorDB._array_model import ArrayModel
from VectorDB.metrics import get_nearest_neighbor


class ArrayCRUD:

    @staticmethod
    def add_array(session: Session, data: dict):

        _id: str = data.get("id", str(uuid4()))
        _array_data: np.ndarray = data.get("array_data", np.array([]))
        _shape: str = repr(_array_data.shape)
        _array_data: bytes = adapt_array(_array_data)

        array_model: ArrayModel = ArrayModel(id=_id, array_data=_array_data, shape=_shape)

        try:
            session.add(array_model)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

        return array_model

    @staticmethod
    def query_array(
            session: Session,
            vector_query: np.ndarray,
            close_k: int = 2):

        query_shape: tuple = vector_query.shape
        _data = session.execute(select(ArrayModel)).scalars().all()

        data: list = list(filter(lambda row: ast.literal_eval(row.shape) == query_shape, _data))

        if len(data) == 0:
            return []

        if close_k > len(data):
            close_k = len(data)

        _ids: list = list(map(lambda row: row.id, data))
        _vectors: list = list(map(lambda row: convert_to_array(row.array_data), data))

        _results: list = get_nearest_neighbor(_vectors, vector_query, close_k)

        for i in range(len(_results)):
            _results[i].insert(0, _ids[i])

        return _results
