from fastapi import FastAPI, HTTPException
from datetime import datetime
from zoneinfo import ZoneInfo

from db import SessionDep, create_all_tables

from models import Customer, Transaction, Invoice, CustomerCreate
from sqlmodel import select
    
# Crear la aplicación FastAPI
app = FastAPI(lifespan=create_all_tables)

@app.get("/")
async def root():
    return {"message": "Hola Luis!", "timestamp": datetime.now()}

country_timezones = {
    "US": "America/New_York",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "CL": "America/Santiago",
    "CO": "America/Bogota",
    "PE": "America/Lima",
}

# Mapeo de códigos ISO de países a zonas horarias
@app.get("/time/{iso_code}")
async def time(iso_code: str) -> str:
    '''
    Retorna la hora actual en la zona horaria del país especificado por su código ISO.
    Parámetros:
    - iso_code: Código ISO del país (por ejemplo, 'US' para Estados Unidos).
    Retorna:
    - Un diccionario con la hora actual en formato ISO.
    '''
    iso_code = iso_code.upper()
    timezone = country_timezones.get(iso_code)
    # Si el código ISO no es válido, retorna un error 404
    if timezone is None:
        raise HTTPException(status_code=404, detail=f"Unknown ISO code: {iso_code}")
    try:
        tz = ZoneInfo(timezone)
    # Para capturar el error de zona inválida
    except Exception:
        # ZoneInfo raises zoneinfo.ZoneInfoNotFoundError para zonas inválidas
        raise HTTPException(status_code=500, detail=f"Invalid timezone configured: {timezone}")
    # Retorna la hora actual en formato ISO
    return {"time": datetime.now(tz).isoformat()}

formats = {
    "12h": "%I:%M %p",
    "24h": "%H:%M",
    "iso": "%Y-%m-%dT%H:%M:%S%z",
}

# API para obtener la hora en un formato especifico (RETO PENDIENTE)
@app.get("/format/{time_format}")
async def time_format(time_format: str) -> dict:
    '''
    Retorna la hora actual en el formato especificado.
    Parámetros:
    - time_format: El formato deseado para la hora. Puede ser '12h', '24h' o 'iso'.
    Retorna:
    - Un diccionario con la hora formateada según el formato solicitado.
    '''
    time_format = time_format.lower()
    format_str = formats.get(time_format)
    # Si el formato no es válido, retorna un error 404
    if format_str is None:
        raise HTTPException(status_code=404, detail=f"formato desconocido: {time_format}")
    try:
    # Usar un datetime aware para que %z (offset) se rellene correctamente
        now = datetime.now().astimezone()
        formatted_time = now.strftime(format_str)
        return {"time": formatted_time}
    # Para capturar errores de formato
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al formatear la hora: {e}")
    
db_customers: list[Customer] = []

@app.post("/customers/", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump()) # Convertir CustomerCreate a Customer en formato dict
    session.add(customer) # Agregar el nuevo cliente a la sesión
    session.commit() # Guardar los cambios en la base de datos
    session.refresh(customer) # Refrescar el objeto cliente para obtener los datos actualizados
    #Asumieendo que el id no se genera automáticamente (SIN BASE DE DATOS)
    #customer.id = len(db_customers) +1
    #db_customers.append(customer)
    return customer

@app.get("/customers/", response_model=list[Customer])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all()

# retornar un cliente por su ID RETO PENDIENTE
@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    for customer in db_customers:
        if customer.id == customer_id:
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.post("/transactions/")
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post("/invoices/")
async def create_invoice(invoice_data: Invoice):
    return invoice_data