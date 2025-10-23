from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine, SQLModel

sqlite_name = "db.sqlite3" # SQLite database file
sqlite_url = f"sqlite:///{sqlite_name}" # URL for SQLite database


engine = create_engine(sqlite_url) # Crear el motor de la base de datos

def create_all_tables(app: FastAPI):
    '''
    Crear todas las tablas en la base de datos.
    Parámetros:
    - app: La instancia de FastAPI.
    Retorna:
    - None
    '''
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    '''
    Obtener una sesión de base de datos.
    Retorna:
    - Una sesión de base de datos.
    '''
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)] # Dependencia para obtener la sesión de base de datos
