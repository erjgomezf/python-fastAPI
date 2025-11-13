from typing import Annotated
from zoneinfo import ZoneInfo
import time
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import Transaction, Invoice
from db import create_all_tables
from .routers import customers, transactions, invoice, plans


app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router, tags=["customers"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(invoice.router, prefix="/invoices", tags=["invoices"])
app.include_router(plans.router, tags=["plans"])


@app.middleware("http")
async def log_request_time(request: Request, call_next) -> Request:
    '''
    Middleware para registrar el tiempo de procesamiento de una solicitud.
    Parámetros:
    - request: La solicitud entrante.
    '''
    star_time = time.time()
    response = await call_next(request)
    process_time = time.time() - star_time
    print(f"Request: {request.url}, completed in {process_time:.4f} seconds")
    return response

@app.middleware("http")
async def log_request_headers(request: Request, call_next) -> Request:
    '''
    Middleware para registrar los encabezados de la solicitud.
    Parámetros:
    - request: La solicitud entrante.
    '''
    print(f"Request headers: {request.headers}")
    response = await call_next(request)
    return response

security = HTTPBasic()

@app.get("/")
async def root(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    if credentials.username == "luis" and credentials.password == "luis":
        return {"message": "Hola Luis!"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas",
        headers={"WWW-Authenticate": "Basic"},
    )


    print(credentials)
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
async def get_time_by_iso_code(iso_code: str) -> str:
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