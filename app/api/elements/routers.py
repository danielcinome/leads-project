from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Annotated
from app.db.postgres.connector import PostgresqlManager
from sqlalchemy.orm import Session
from .schemas import ElementsToProcessOut, ElementsToProcessCreate, ElementsToProcessUpdate
from .managers import search_elements, create_elements, delete_element, update_element
from app.api.users.schemas import UserSc
from app.api.users.routers import get_current_active_user

router = APIRouter()
validate_user = Annotated[UserSc, Depends(get_current_active_user)]

@router.get('/search/{status_}', response_model=List[ElementsToProcessOut])
async def search_elements_router(status_: str, db: Session = Depends(PostgresqlManager.get_db)):
    """
    Search for elements by their status.

    Args:
    * status_ (str): Status by which the search will be performed.

    Returns:
    * List of elements matching the provided status.
    """
    try:
        elements = await search_elements(status_, db)
    except Exception as error:
        raise error

    return elements

@router.post('/create', response_model=ElementsToProcessOut)
async def create_elements_router(element_create: ElementsToProcessCreate, current_user: validate_user, db: Session = Depends(PostgresqlManager.get_db)):
    """
    Create a new element.

    This endpoint allows you to create a new element.

    Returns:
    * Data of the created element.

    To use the EndPoint you must be an authenticated user.
    """
    try:
        element = await create_elements(element_create, db)
    except Exception as error:
        error

    return element

@router.patch("/update", response_model=ElementsToProcessOut)
async def update_element_router(updated_data: ElementsToProcessUpdate,  current_user: validate_user, db: Session = Depends(PostgresqlManager.get_db)):
    """
    Update an Existing Element (Partially).

    This endpoint allows you to partially update an existing element.

    Returns:
    * Updated element data.

    To use the EndPoint you must be an authenticated user.
    """
    try:
        element = await update_element(updated_data, db)
    except Exception as error:
        raise error

    return element


@router.delete("/delete/{element_id}")
async def delete_element_router(element_id: int, current_user: validate_user, db: Session = Depends(PostgresqlManager.get_db)):
    """
    Delete an Element by ID.

    This endpoint allows you to delete an element according to its ID.

    Returns:
    * Delete confirmation.

    To use the EndPoint you must be an authenticated user.
    """
    try:
        return await delete_element(element_id, db)
    except HTTPException as http_exception:
        raise http_exception
