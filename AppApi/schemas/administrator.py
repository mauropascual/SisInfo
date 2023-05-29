from pydantic import BaseModel

from .user import UserCreate

class AdministratoBase(BaseModel):
    id_user: str
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class CreateAdministrator(UserCreate):
    address: str

    class Config:
        orm_mode = True

class Administrator(AdministratoBase):
    id_user: str