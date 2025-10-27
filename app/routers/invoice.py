from fastapi import APIRouter
from models import Invoice

# Para crear el router en APIRouter
router = APIRouter()


@router.post("/invoices/")
async def create_invoice(invoice_data: Invoice):
    return invoice_data