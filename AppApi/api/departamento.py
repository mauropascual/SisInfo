from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .dependencies import get_db_session, get_current_user


from schemas.departamento import DepartamentoBase
from data.models.administrator import Administrator
from services.departamento import DepartamentoService


departamento_router = APIRouter(prefix='/departamento')

@departamento_router.get("/", response_model=list[DepartamentoBase], tags=["Departamento"])
def get_departamento(session: Session=Depends(get_db_session)):
    departamento_service = DepartamentoService(session)

    return departamento_service.get_departamentos()

@departamento_router.post("/", response_model=DepartamentoBase, tags=["Departamento"])
def register_departamento(departamento: DepartamentoBase=Depends(), foto: UploadFile = File(default=None), 
                          session: Session=Depends(get_db_session),
                  user: Administrator=Depends(get_current_user)):
    departamento_service = DepartamentoService(session)
    if foto:
        foto = foto.file.read()

    return departamento_service.register_departamento(user.id_user, foto, departamento)


@departamento_router.put("/{id}", response_model=DepartamentoBase, tags=["Departamento"])
def register_departamento(id: str, departamento: DepartamentoBase=Depends(), foto: UploadFile = File(default=None),
                          session:Session=Depends(get_db_session)):
    departamento_service = DepartamentoService(session)
    data_departamento = departamento_service.get_departamento(id)
    
    if foto:
        foto = foto.file.read()

    return departamento_service.update_departamento(id, foto, departamento, data_departamento)