from pydantic import BaseModel

from .user import UserCreate, User

class ConserjeBase(BaseModel):
    id_user: str
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class CreateConserje(UserCreate):
    cargo: str
    carnet: str
    antecedentes: str

    class Config:
        orm_mode = True

class Conserje(ConserjeBase):
    id_user: str

    class Config:
        orm_mode = True

class ShowConserje(User):
    cargo: str
    carnet: str
    antecedentes: str

    class Config:
        orm_mode = True
