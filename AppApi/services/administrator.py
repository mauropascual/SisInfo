from sqlalchemy.orm import Session

from .utils import generate_id, get_hashed_password
from schemas.administrator import CreateAdministrator
from data.models.administrator import Administrator
from .constants import ROLES_ID

ADMIN_TYPE = 'administrator'

class AdministratorService:
    def __init__(self, session : Session):
        self.session = session

    # def get_user(self):
    #     db_users = self.session.query(User).all()

    #     return db_user

    def register_administrator(self, user: CreateAdministrator):
        id_user = generate_id()
        hashed_password = get_hashed_password(user.password)
        create_user = Administrator(id_user = id_user, name = user.name, 
                       last_name = user.last_name, email = user.email, password = hashed_password, address = user.address, role=ROLES_ID.get(ADMIN_TYPE), user_type=ADMIN_TYPE)
        self.session.add(create_user)
        self.session.commit()
        self.session.refresh(create_user)

        return create_user
    