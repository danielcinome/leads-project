from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.db.postgres.connector import PostgresqlManager
from sqlalchemy.orm import Session
from .schemas import ElementsToProcessOut, ElementsToProcessCreate
from .managers import search_elements, create_elements

router = APIRouter()

@router.get('/search/{status_}', response_model=List[ElementsToProcessOut])
async def search_elements_router(status_: str, db: Session = Depends(PostgresqlManager.get_db)):
    try:
        elements = await search_elements(status_, db)
    except Exception as error:
        raise error

    return elements

@router.post('/create', response_model=ElementsToProcessOut)
async def create_elements_router(element_create: ElementsToProcessCreate, db: Session = Depends(PostgresqlManager.get_db)):
    try:
        element = await create_elements(element_create, db)
    except Exception as error:
        error

    return element