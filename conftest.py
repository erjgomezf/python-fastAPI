import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from app.main import app
from db import get_session


sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(
    sqlite_url, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    )

@pytest.fixture(name="session")
def session_fixture() -> Session: # type: ignore
    '''
    Crear todas las tablas en la base de datos.
    Parámetros:
    - app: La instancia de FastAPI.
    Retorna:
    - None
    '''
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session: Session) -> TestClient: # type: ignore
    '''
    
    '''
    def get_session_override() -> Session:
        '''
        Obtener una sesión de base de datos.
        Retorna:
        - Una sesión de base de datos.
        '''
        return session
    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()