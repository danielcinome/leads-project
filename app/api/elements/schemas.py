from pydantic import BaseModel
from typing import Optional

class ElementsToProcessBase(BaseModel):
    id_bulk: int
    retries: Optional[int] = None
    status: int
    name: str

class ElementsToProcessCreate(ElementsToProcessBase):
    pass

class ElementsToProcessUpdate(BaseModel):
    id_bulk: Optional[int] = None
    retries: Optional[int] = None
    status: Optional[int] = None
    name: Optional[str] = None
    id: int

class ElementsToProcessOut(ElementsToProcessBase):
    id: int
