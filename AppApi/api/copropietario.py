from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .dependencies import get_db_session, get_current_user


from schemas.copropietario import Copropietario as Copro
from schemas.copropietario import UpdateCopropietario, CopropietarioBase
from data.models.copropietario import Copropietario
from services.copropietario import CopropietarioService


copropietario_router = APIRouter(prefix='/conpropietario')

@copropietario_router.get("/", response_model=list[UpdateCopropietario], tags=["Copropietario"])
def ger_copropietarios(session: Session=Depends(get_db_session)):
    service = CopropietarioService(session)

    return service.get_copropietarios()

@copropietario_router.post("/", response_model=Copro, tags=["Copropietario"])
def register_user(user: Copro = Depends(), foto: UploadFile = File(default=None), 
                  session: Session=Depends(get_db_session)):
    copropietario_service = CopropietarioService(session)
    if foto:
        foto = foto.file.read()

    return copropietario_service.register_copropietario(foto, user)

@copropietario_router.put("/{id}", response_model=Copro, tags=["Copropietario"])
def update_copropietario(id_copropietario, foto:UploadFile=File(default=None), user: UpdateCopropietario= Depends(),
                    session: Session=Depends(get_db_session)):
    copropietario_service = CopropietarioService(session)
    if foto:
        foto = foto.file.read()

    return copropietario_service.update_copropietario(id_copropietario, foto, user)

