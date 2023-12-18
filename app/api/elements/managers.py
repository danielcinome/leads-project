
from typing import List
from sqlalchemy.orm import Session
from greenletio import async_
from fastapi import HTTPException, status


from .schemas import ElementsToProcessOut, ElementsToProcessCreate, ElementsToProcessUpdate
from app.models.schemas import ElementsToProcess


async def search_elements(status_:str, db: Session) -> List[ElementsToProcessOut]:
    """
    Search for elements by status.

    Args:
    - status_ (str): The status of the elements to search for.
    - db (Session): Database session.

    Returns:
    - List[ElementsToProcessOut]: A list of elements matching the specified status.

    Raises:
    - HTTPException: If the elements are not found or an internal server error occurs.
    """
    try:
        # Search all elements by status
        elements = await async_(db.query(ElementsToProcess).filter_by(status=status_).all)()
        if len(elements) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra registro del elememto con estado, {status_}')
    except HTTPException as http_execption:
        raise http_execption
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error al buscar elementos, intente nuevamente')

    return elements

async def create_elements(element_create: ElementsToProcessCreate, db: Session) -> ElementsToProcessOut:
    """
    Create a new element.

    Args:
        element_create (ElementsToProcessCreate): Data for creating a new element.
        db (Session): Database session.

    Returns:
        ElementsToProcessOut: Information about the newly created element.

    Raises:
        HTTPException: If there is an issue creating the element or an internal server error occurs.
    """
    try:
        new_element = ElementsToProcess(**element_create.dict())
        db.add(new_element)
        db.commit()
        db.refresh(new_element)
    except HTTPException as http_execption:
        raise http_execption
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error al crear un nuevo elemento, intente nuevamente')

    return ElementsToProcessOut(**new_element.__dict__)


async def update_element(updated_data:ElementsToProcessUpdate, db: Session) -> ElementsToProcessOut:
    """
    Update an existing element.

    Args:
        updated_data (ElementsToProcessUpdate): Data for updating an existing element.
        db (Session): Database session.

    Returns:
        ElementsToProcessOut: Information about the updated element.

    Raises:
        HTTPException: If the element to update is not found or an internal server error occurs.
    """
    try:
        existing_element = await async_(db.query(ElementsToProcess).filter_by(id=updated_data.id).first)()

        if existing_element is None:
            raise HTTPException(status_code=404,  detail=f"Elemento con id {element_id}, no encontrado")

        for field, value in updated_data.dict(exclude_unset=True).items():
            if value is not None:
                setattr(existing_element, field, value)

        db.commit()
        db.refresh(existing_element)
    except HTTPException as http_execption:
        raise http_execption
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error al actualizar el elemento, intente nuevamente')

    return existing_element

async def delete_element(element_id: str, db: Session):
    """
    Delete an element by ID.

    Args:
        element_id (str): The ID of the element to delete.
        db (Session): Database session.

    Returns:
        dict: A message indicating the successful deletion.

    Raises:
        HTTPException: If the element to delete is not found or an internal server error occurs.
    """

    try:
        element_to_delete = await async_(db.query(ElementsToProcess).filter_by(id=element_id).first)()

        if element_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Elemento con id {element_id}, no encontrado")

        db.delete(element_to_delete)
        db.commit()
    except HTTPException as http_execption:
        raise http_execption
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error al eliminar el elemento, intente nuevamente')

    return {
            'message': f'Se ha eliminado correctamente el elemento',
    }