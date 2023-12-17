
from typing import List
from sqlalchemy.orm import Session
from greenletio import async_
from fastapi import HTTPException, status


from .schemas import ElementsToProcessOut, ElementsToProcessCreate
from app.models.schemas import ElementsToProcess


async def search_elements(status_:str, db: Session) -> List[ElementsToProcessOut]:
    try:
        elements = await async_(db.query(ElementsToProcess).filter_by(status=status_).all)()
        if len(elements) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra registro del elememto con estado, {status_}')
    except HTTPException as http_execption:
        raise http_execption
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error al buscar elementos: {error}')

    return elements

async def create_elements(element_create: ElementsToProcessCreate, db: Session) -> ElementsToProcessOut:
    try:
        new_element = ElementsToProcess(**element_create.dict())
        db.add(new_element)
        db.commit()
        db.refresh(new_element)
    except HTTPException as http_execption:
        raise http_execption
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error al crear un nuevo elemento: {error}')

    return ElementsToProcessOut(**new_element.__dict__)