from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .dependencies import get_db_session, get_current_user


from schemas.conserje import CreateConserje, ConserjeBase, ShowConserje, UpdateConserje
from data.models.administrator import Administrator
from services.conserje import ConserjeService


conserje_router = APIRouter(prefix='/conserje')

@conserje_router.get("/", response_model=list[ShowConserje], tags=["Conserje"])
def get_conserjes(session: Session=Depends(get_db_session)):
    conserje_service = ConserjeService(session)
    return conserje_service.get_conserjes()

@conserje_router.get("/{id}", response_model=UpdateConserje, tags=["Conserje"])
def get_conserje(id:str, session:Session=Depends(get_db_session)):
    conserje_service = ConserjeService(session)
    return conserje_service.get_conserje(id)

@conserje_router.post("/", response_model=ConserjeBase, tags=["Conserje"])
def register_user(user: CreateConserje = Depends(), foto: UploadFile = File(default=None), 
                  session: Session=Depends(get_db_session), _:Administrator=Depends(get_current_user)):
    conserje_service = ConserjeService(session)
    if foto:
        foto = foto.file.read()

    return conserje_service.register_conserje(foto, user)

@conserje_router.put("/{id}", response_model=UpdateConserje, tags=["Conserje"])
def update_conserje(id, foto:UploadFile=File(default=None), user: UpdateConserje= Depends(),
                    session: Session=Depends(get_db_session)):
    conserje_service = ConserjeService(session)
    if foto:
        foto = foto.file.read()

    return conserje_service.update_conserje(id, foto, user)

@conserje_router.delete("/{id}", tags=["Conserje"])
def delete_conserje(id:str, session:Session=Depends(get_db_session)):
    conserje_service = ConserjeService(session)
    conserje_service.delete_conserje(id)

    return {"Mensaje": "Fue eliminado exitosamente"}