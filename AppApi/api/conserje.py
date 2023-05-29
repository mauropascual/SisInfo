from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .dependencies import get_db_session, get_current_user


from schemas.conserje import CreateConserje, ConserjeBase, ShowConserje
from data.models.administrator import Administrator
from services.conserje import ConserjeService


conserje_router = APIRouter(prefix='/conserje')

@conserje_router.get("/", response_model=list[ShowConserje], tags=["Conserje"])
def get_conserjes(session: Session=Depends(get_db_session)):
    conserje_service = ConserjeService(session)
    return conserje_service.get_conserjes()

@conserje_router.post("/", response_model=ConserjeBase, tags=["Conserje"])
def register_user(user: CreateConserje = Depends(), foto: UploadFile = File(default=None), 
                  session: Session=Depends(get_db_session), _:Administrator=Depends(get_current_user)):
    conserje_service = ConserjeService(session)
    if foto:
        foto = foto.file.read()

    return conserje_service.register_conserje(foto, user)
#a