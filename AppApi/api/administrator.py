from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import get_db_session


from schemas.administrator import CreateAdministrator, AdministratoBase
from data.models.user import User
from services.administrator import AdministratorService


administrator_router = APIRouter(prefix='/administrator')

@administrator_router.post("/", response_model=AdministratoBase, tags=["Administrator"])
def register_user(user: CreateAdministrator, session: Session=Depends(get_db_session)):
    administrator_service = AdministratorService(session)

    return administrator_service.register_administrator(user)
