from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import get_db_session


from schemas.user import UserBase, UserCreate
from data.models.user import User
from services.user import UserService


user_router = APIRouter(prefix='/user')

@user_router.post("/", response_model=UserBase, tags=["User"])
def register_user(user: UserCreate, session: Session=Depends(get_db_session)):
    user_service = UserService(session)

    return user_service.register_user(user)

@user_router.get("/", response_model=list[UserBase], tags=["User"])
def get_user(session: Session= Depends(get_db_session)):
    db = UserService(session)

    return db.get_user()


