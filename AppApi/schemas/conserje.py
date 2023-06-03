from pydantic import BaseModel

from .user import UserCreate, User

class ConserjeBase(BaseModel):
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class CreateConserje(UserCreate):
    cargo: str
    carnet: str
    antecedentes: str
    direccion: str
    telefono: str

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

class UpdateConserje(BaseModel):
    name: str
    last_name: str
    email: str
    cargo: str
    antecedentes: str
    direccion: str
    telefono: str

    class Config:
        orm_mode = True