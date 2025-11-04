import math
from fastapi import APIRouter, HTTPException, Query, status
from sqlmodel import select

from db import SessionDep
from models import Customer, Transaction, TransactionCreate

router = APIRouter()


@router.post(
    "/transactions", status_code=status.HTTP_201_CREATED, tags=["transactions"]
)
async def create_transation(transaction_data: TransactionCreate, session: SessionDep):
    transaction_data_dict = transaction_data.model_dump()
    customer = session.get(Customer, transaction_data_dict.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist"
        )

    transaction_db = Transaction.model_validate(transaction_data_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)

    return transaction_db

@router.get("/transactions", tags=["transactions"])
async def list_transaction(
    session: SessionDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Número de registros"),
)-> list[Transaction]:
    query = select(Transaction).offset(skip).limit(limit)
    transactions = session.exec(query).all()
    return transactions

@router.get("/transactions/number", tags=["transactions"])
async def list_number_transactions(
    session: SessionDep,
    registros_por_pagina: int = Query(10, description="Número de registros por pagina"),
    numero_pagina: int = Query(1, description="Número de página"),
)-> list[Transaction]:
    '''
    Retorna una lista de todos los clientes en la base de datos.
    * Parámetros:
        - session: La sesión de base de datos.
    * Retorna:
        - Una lista de clientes
    '''
    transaction_db: int = session.exec(select(Transaction.id)).all()
    number_transaction : int = len(transaction_db)
    number_pages = math.ceil(number_transaction / registros_por_pagina)
    
    skip = ((numero_pagina - 1) * registros_por_pagina)
    query = select(Transaction).offset(skip).limit(registros_por_pagina)
    
    transactions = session.exec(query).all()
    count_pages: str = f"Cantidad de páginas: {number_pages}"
    return transactions, count_pages
    

    