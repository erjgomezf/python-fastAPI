from fastapi import APIRouter, status, HTTPException
from sqlmodel import select


from models import Customer, CustomerCreate, CustomerUpdate
from db import SessionDep, create_all_tables

# Para crear el router en APIRouter
router = APIRouter()


# Crear un cliente
@router.post("/customers/", response_model=Customer, tags=["customers"])
async def create_customer(customer_data: CustomerCreate, session: SessionDep) -> Customer:
    '''
    Crea un nuevo cliente en la base de datos.
    * Parámetros:
        - customer_data: Los datos del cliente a crear.
    * Retorna:
        - El cliente creado.
    '''
    customer = Customer.model_validate(customer_data.model_dump()) # Convertir CustomerCreate a Customer en formato dict
    session.add(customer) # Agregar el nuevo cliente a la sesión
    session.commit() # Guardar los cambios en la base de datos
    session.refresh(customer) # Refrescar el objeto cliente para obtener los datos actualizados
    return customer

# Listar todos los clientes
@router.get("/customers/", response_model=list[Customer], tags=["customers"])
async def list_customers(session: SessionDep) -> list[Customer]:
    '''
    Retorna una lista de todos los clientes en la base de datos.
    * Parámetros:
        - session: La sesión de base de datos.
    * Retorna:
        - Una lista de clientes.
    '''
    customers_db = session.exec(select(Customer)).all()
    if len(customers_db) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron clientes")
    return customers_db

# retornar un cliente por su ID 
@router.get("/read_customers/{customer_id}", response_model=Customer, tags=["customers"])
async def get_customer(customer_id: int, session: SessionDep) -> Customer:
    '''
    Retorna un cliente por su ID.
    * Parámetros:
        - customer_id: El ID del cliente a retornar.
    * Retorna:
        - El cliente con el ID especificado.
    '''
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {customer_id} no encontrado")
    return customer_db

# eliminar un cliente por su ID
@router.delete("/delete_customers/{customer_id}", tags=["customers"])
async def delete_customer(customer_id: int, session: SessionDep) -> dict:
    '''
    Elimina un cliente por su ID.
    * Parámetros:
        - customer_id: El ID del cliente a eliminar.
    * Retorna:
        - Un mensaje de éxito.
    '''
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {customer_id} no encontrado")
    session.delete(customer_db)
    session.commit()
    return {"detail":"OK"}

# actualizar un cliente por su ID
@router.patch("/update_customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED, tags=["customers"])
async def update_customer(customer_id: int, customer_data: CustomerUpdate, session: SessionDep) -> Customer:
    '''
    Actualiza un cliente por su ID.
    * Parámetros:
        - customer_id: El ID del cliente a actualizar.
        - customer_data: Los datos actualizados del cliente.
    * Retorna:
        - El cliente actualizado.
    '''
    customer_db = session.get(Customer, customer_id, tags=["customers"])
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {customer_id} no encontrado")
    customer_data_dict = customer_data.model_dump(exclude_unset=True) # Convertir CustomerUpdate a dict
    customer_db.sqlmodel_update(customer_data_dict) # Actualizar el cliente en la base de datos
    session.add(customer_db) # Agregar el cliente actualizado a la sesión
    session.commit() # Guardar los cambios en la base de datos
    session.refresh(customer_db) # Refrescar el objeto cliente para obtener los datos actualizados
    return customer_db
