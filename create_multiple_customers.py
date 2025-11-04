from sqlmodel import Session
from faker import Faker

from db import engine
from models import Customer

session = Session(engine)
faker = Faker()

for x in range(100):
    # Usamos unique.email para garantizar que no se repitan en la misma ejecución
    customer = Customer(
        name=faker.name(),
        description=faker.sentence(),
        email=faker.unique.email(),
        age=faker.random_int(min=18, max=80)
    )
    session.add(customer)
    # Hacemos commit en cada iteración para que el validador de email funcione correctamente
    # contra la base de datos para el siguiente cliente.
    session.commit()