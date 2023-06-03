from sqlalchemy.orm import Session

from .utils import generate_id, get_hashed_password
from schemas.copropietario import Copropietario as Copro
from schemas.copropietario import UpdateCopropietario
from data.models.copropietario import Copropietario
from .constants import ROLES_ID

ADMIN_TYPE = 'copropietario'

class CopropietarioService:
    def __init__(self, session : Session):
        self.session = session

    def register_copropietario(self, foto, user: Copro):
        id_user = generate_id()
        hashed_password = get_hashed_password(user.password)
        create_user = Copropietario(id_user = id_user, name = user.name, id_departamento = user.id_departamento,
                        last_name = user.last_name, email = user.email, password = hashed_password,
                        carnet = user.carnet, direccion = user.direccion, telefono = user.telefono,
                        foto = foto,
                        role=ROLES_ID.get(ADMIN_TYPE), user_type=ADMIN_TYPE)
        self.session.add(create_user)
        self.session.commit()
        self.session.refresh(create_user)

        return create_user
    
    def update_copropietario(self, id_copropietario: str, foto, user: UpdateCopropietario):
        copropietario = self.session.query(Copropietario).filter(Copropietario.id_user == id_copropietario).first()
        if copropietario:
            copropietario.name = user.name
            copropietario.last_name = user.last_name
            copropietario.email = user.email
            copropietario.direccion = user.direccion
            copropietario.telefono = user.telefono
            copropietario.foto = foto

            self.session.commit()
            self.session.refresh(copropietario)

        return copropietario
    


