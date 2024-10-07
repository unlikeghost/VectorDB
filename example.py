import numpy as np

from VectorDB import get_engine, create_tables, get_session
from VectorDB import ArrayCRUD


engine = get_engine()
create_tables(engine)
session = get_session(engine)

vectordb = ArrayCRUD()

array1 = np.arange(10)
array2 = np.arange(10, 20)
array3 = np.arange(20, 30)

vectordb.add_array(session, {'array_data': array1})
vectordb.add_array(session, {'array_data': array3})
vectordb.add_array(session, {'array_data': array2})

vectordb.add_array(session, {'array_data': np.arange(20, 28)})

query = np.arange(19, 29)
result = vectordb.query_array(session, query, 100)
print(result)
