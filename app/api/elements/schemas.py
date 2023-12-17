from pydantic import BaseModel
from typing import Optional

class ElementsToProcessBase(BaseModel):
    id_bulk: int
    retries: Optional[int] = None
    status: int
    name: str

class ElementsToProcessCreate(ElementsToProcessBase):
    pass

class ElementsToProcessOut(ElementsToProcessBase):
    id: int
