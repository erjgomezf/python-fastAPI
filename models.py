from pydantic import BaseModel, EmailStr, field_validator
from sqlmodel import SQLModel, Field, Relationship, select, Session
from enum import Enum
from db import engine


class StatusEnum(str, Enum):
    ACTIVE = "activo"
    INACTIVE = "inactivo"

class CustomerPlan(SQLModel, table=True):
    '''
    Tabla de relaciones entre clientes y planes.
    Parámetros:
    - plan_id: Identificador del plan.
    - customer_id: Identificador del cliente.
    '''
    plan_id: int = Field(foreign_key="plan.id", primary_key=True)
    customer_id: int = Field(foreign_key="customer.id", primary_key=True)
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)
    

class PlanBase(SQLModel):
    '''
    Clase base para planes.
    Parámetros:
    - name: Nombre del plan.
    - price: Precio del plan.
    - description: Descripción del plan.
    '''
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str = Field(default=None)


class PlanCreate(PlanBase):
    pass


class Plan(PlanBase, table=True):
    '''
    Tabla de planes.
    '''
    id: int | None = Field(default=None, primary_key=True)
    customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)




class CustomerBase(SQLModel):
    '''
    Clase base para clientes.
    Parámetros:
    - name: Nombre del cliente.
    - description: Descripción del cliente.
    - email: Dirección de correo electrónico del cliente.
    - age: Edad del cliente.
    '''
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr | None = Field(default=None)
    age: int = Field(default=None)
    
    @field_validator("email")   #campo que se busca validar
    @classmethod    #convierte a class method para usar la funcion
    def validate_email(cls, value) -> str:
        '''
        Valida que no exista un cliente con la misma dirección de correo electrónico.
        Parámetros:
        - value: Dirección de correo electrónico a validar.
        Retorna:
        - La dirección de correo electrónico válida.
        Raises:
        - ValueError: Si ya existe un cliente con la misma dirección de correo electrónico.
        '''
        session = Session(engine) 
        query = select(Customer).where(Customer.email == value)
        result = session.exec(query).first()
        if result:
            raise ValueError("Ya existe un cliente con esta dirección de correo electrónico")
        return value


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class Customer(CustomerBase, table=True):
    '''
    Tabla de clientes.
    Parámetros:
    - id: Identificador único del cliente.
    - transaction: Transacciones asociadas al cliente.
    '''
    id: int | None = Field(default=None, primary_key=True)
    transaction: list["Transaction"] = Relationship(back_populates="customer")
    plans: list[Plan] = Relationship(back_populates="customers", link_model=CustomerPlan)
    



class TransactionBase(SQLModel):
    '''
    Clase base para transacciones.
    Parámetros:
    - ammount: Monto de la transacción.
    - description: Descripción de la transacción.
    - date: Fecha de la transacción.
    '''
    ammount: int = Field(default=None)
    description: str = Field(default=None)
    date: str = Field(default=None)
    
class Transaction(TransactionBase, table=True):
    '''
    Tabla de transacciones.
    Parámetros:
    - id: Identificador único de la transacción.
    - customer_id: Identificador del cliente asociado a la transacción.
    - customer: Cliente asociado a la transacción.
    '''
    id: int = Field(default=None, primary_key=True)
    customer_id: int = Field(default=None, foreign_key="customer.id") #acceder al id de customer
    customer: Customer = Relationship(back_populates="transaction")
    

class TransactionCreate(TransactionBase):
    customer_id: int = Field(default=None, foreign_key="customer.id")





class TransactionUpdate(TransactionBase):
    pass



class Invoice(BaseModel):
    '''
    Clase para facturas.
    Parámetros:
    - id: Identificador único de la factura.
    - customer: Cliente asociado a la factura.
    - transactions: Transacciones asociadas a la factura.
    - total: Total de la factura.
    '''
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        '''
        Calcula el total de la factura.
        Retorna:
        - El total de la factura.
        '''
        return sum(transaction.ammount for transaction in self.transactions)