from fastapi import APIRouter, HTTPException, status
from models import Plan, PlanCreate
from db import SessionDep
from sqlmodel import select


# Para crear el router en APIRouter

router = APIRouter()

@router.post("/plans/", response_model=Plan, status_code=status.HTTP_201_CREATED, tags=["plans"])
async def create_plan(plan_data: PlanCreate, session: SessionDep) -> Plan:
    '''
    Retorna una lista de todos los planes en la base de datos.
    * Parámetros:
        - session: La sesión de base de datos.
    * Retorna:
        - Una lista de planes
    '''
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db

@router.get("/plans/", response_model=list[Plan], status_code=status.HTTP_200_OK, tags=["plans"])
async def list_plans(session: SessionDep) -> list[Plan]:
    plans_db = session.exec(select(Plan)).all()
    if len(plans_db) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron planes")
    return plans_db