from pydantic import BaseModel

class DepartamentoBase(BaseModel):
    superficie: str
    ambientes: str
    torre: str
    direccion: str
    numero_depar: str
    garaje: bool
    boulera: bool

    class Config:
        orm_mode = True

class Departamento(DepartamentoBase):
    id_user: str

    class Config:
        orm_mode = True

class DepartamentoWithAdmi(Departamento):
    id_administrator: str
    
    class Config:
        orm_mode = True