from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import get_db_session, get_current_user


from schemas.departamento import DepartamentoBase
from data.models.administrator import Administrator
from services.departamento import DepartamentoService


departamento_router = APIRouter(prefix='/departamento')

@departamento_router.get("/", response_model=list[DepartamentoBase], tags=["Departamento"])
def register_user(session: Session=Depends(get_db_session),
                  _: Administrator=Depends(get_current_user)):
    departamento_service = DepartamentoService(session)

    return departamento_service.get_departamento()

@departamento_router.post("/", response_model=DepartamentoBase, tags=["Departamento"])
def register_user(departamento: DepartamentoBase, session: Session=Depends(get_db_session),
                  user: Administrator=Depends(get_current_user)):
    departamento_service = DepartamentoService(session)

    return departamento_service.register_departamento(user.id_user, departamento)
