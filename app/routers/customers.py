from fastapi import APIRouter, Query, status, HTTPException
from sqlmodel import select


from models import Customer, CustomerCreate, CustomerUpdate, Plan, CustomerPlan, StatusEnum
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

@router.post("/customers/{customer_id}/plans/{plan_id}/", status_code=status.HTTP_201_CREATED, tags=["customers"])
async def subscribe_customer_to_plan(customer_id: int, plan_id: int, session: SessionDep, plan_status: StatusEnum = Query()) -> CustomerPlan:
    '''
    Suscribe un cliente a un plan.
    * Parámetros:
        - `customer_id`: El ID del cliente.
        - `plan_id`: El ID del plan.
    * Retorna:
        - El objeto `CustomerPlan` que representa la nueva suscripción.
    '''
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)
    
    if not customer_db or not plan_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente o plan no encontrado")
    
    # Añadir el plan a la lista de planes del cliente
    customer_plan_db = CustomerPlan(plan_id=plan_db.id, customer_id=customer_db.id, status=plan_status)
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)

    return customer_plan_db

@router.get("/customers/plans/", response_model=list[CustomerPlan], status_code=status.HTTP_200_OK, tags=["customers"])
async def list_customer_plans(session: SessionDep) -> list[CustomerPlan]:
    '''
    Retorna una lista de todos los planes en la base de datos.
    * Parámetros:
        - customer_plan_db; La sesión de base de datos.
    * Retorna:
        - Una lista de planes
    '''
    customer_plan_db = session.exec(select(CustomerPlan)).all()
    if len(customer_plan_db) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron planes")
    return customer_plan_db

@router.get("/customers/{customer_id}/plans/", response_model=list[CustomerPlan], status_code=status.HTTP_200_OK, tags=["customers"])
async def list_customer_plans(customer_id: int, session: SessionDep, plan_status: StatusEnum = Query()) -> list[CustomerPlan]:
    query = (
        select(CustomerPlan)
        .where(CustomerPlan.customer_id == customer_id)
        .where(CustomerPlan.status == plan_status)
    )
    
    customer_plan_db = session.exec(query).all()
    if not customer_plan_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encuentran planes activos asociados al cliente con el id {customer_id}")
    return customer_plan_db


    