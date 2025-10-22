from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field


from pydantic import BaseModel, EmailStr

class CustomerBase(SQLModel):
    name: str = Field(default=None, index=True)
    description: str | None = Field(default=None)
    email: EmailStr | None = Field(default=None)
    age: int | None = Field(default=None)

class  CustomerCreate(CustomerBase):    
    pass

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class Transaction(BaseModel):
    id: int | None 
    amount: int | None
    description: str

class Invoice(BaseModel):
    id: int | None 
    customer: Customer
    transaction: list[Transaction]
    total: int | None

    @property
    def total_amount(self) -> int:
        total = sum(transaction.amount for transaction in self.transaction)
        return total
