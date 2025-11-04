import random
from datetime import datetime
from faker import Faker
from sqlmodel import Session, select

from db import engine
from models import Transaction, Customer

faker = Faker()

session = Session(engine)

# 1. Obtener una lista de todos los IDs de clientes existentes para evitar errores de clave foránea.
existing_customer_ids = session.exec(select(Customer.id)).all()

if not existing_customer_ids:
    print("Error: No hay clientes en la base de datos. Ejecuta primero 'create_multiple_customers.py'.")
    exit()

# 2. Crear 100 transacciones en memoria.
for x in range(100):
    transaction = Transaction(
        # Elegir un ID de cliente aleatorio de la lista de IDs que realmente existen.
        customer_id=random.choice(existing_customer_ids),
        description=faker.sentence(),
        ammount=faker.random_int(min=100, max=1000),
        date=faker.datetime_between(
            start_date=datetime(2022, 1, 1), end_date=datetime.now()
        ).isoformat(),
    )
    session.add(transaction)

# 3. Realizar un único commit al final para mejorar el rendimiento.
session.commit()

print("Se han creado 100 transacciones para clientes existentes.")