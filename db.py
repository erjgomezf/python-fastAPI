from fastapi import FastAPI
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)


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
