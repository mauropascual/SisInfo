from pydantic import BaseModel

from .user import UserCreate, User

class CopropietarioBase(BaseModel):
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class Copropietario(UserCreate):
    id_departamento: str
    carnet: str
    direccion: str
    telefono: str

    class Config:
        orm_mode = True

class UpdateCopropietario(CopropietarioBase):
    direccion: str
    telefono: str
    id_departamento: str