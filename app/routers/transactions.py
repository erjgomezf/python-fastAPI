from fastapi import APIRouter
from models import Transaction

# Para crear el router en APIRouter
router = APIRouter()

@router.post("/transactions")
async def create_transation(transaction_data: Transaction):
    return transaction_data