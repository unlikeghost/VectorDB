# Vector DB

This Python-based application is designed to save vectors using NumPy into a database. It uses SQLAlchemy to ensure compatibility with multiple database engines, although it is currently configured to work with SQLite. The application allows for easy storage and retrieval of vector data in a robust, database-agnostic manner.

This project is based on the code from [sqlite_vector](https://github.com/DaveOkpare/sqlite_vector/tree/main).

## Features

- **Efficient storage of vectors:** Save NumPy arrays in an SQLite database.
- **Fast nearest neighbor search:** Perform query vector searches based on Euclidean distance.
- **Easy-to-use and extendable:** Support for custom database tables and queries.

## Prerequisites

- Python 3.10
- Numpy
- SQLite (default) or any other SQLAlchemy-supported database engine
- Sqlalchemy

## Usage

**Example Code:**
```python
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
result = vectordb.query_array(session, query, 1)
print(result)

"""
# [[id, vector, distance], [...], ...]
[['9a8a88a4-8cec-4b03-9cea-01c37273df36', array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), np.float64(3.1622776601683795)]]
"""
```

## Contributing

Guidelines for contributing to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
