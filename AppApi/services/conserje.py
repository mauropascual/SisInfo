from sqlalchemy.orm import Session

from .utils import generate_id, get_hashed_password
from schemas.conserje import CreateConserje, UpdateConserje
from data.models.conserje import Conserje
from .constants import ROLES_ID

ADMIN_TYPE = 'conserje'

class ConserjeService:
    def __init__(self, session : Session):
        self.session = session

    def get_conserjes(self):
        db_conserjes = self.session.query(Conserje).all()
        return db_conserjes

    def get_conserje(self, id_conserje: str):
        query_conserje = self.session.query(Conserje).filter(
            Conserje.id_user==id_conserje).first()
        
        return query_conserje

    def register_conserje(self, foto, user: CreateConserje):
        id_user = generate_id()
        hashed_password = get_hashed_password(user.password)
        create_user = Conserje(id_user = id_user, name = user.name, 
                        last_name = user.last_name, email = user.email, password = hashed_password,
                        cargo = user.cargo, carnet = user.carnet, antecedentes = user.antecedentes, 
                        direccion = user.direccion, telefono = user.telefono,
                        foto = foto,
                        role=ROLES_ID.get(ADMIN_TYPE), user_type=ADMIN_TYPE)
        self.session.add(create_user)
        self.session.commit()
        self.session.refresh(create_user)

        return create_user
    
    def update_conserje(self, id_conserje: str, foto, user: UpdateConserje):
        conserje = self.session.query(Conserje).filter(Conserje.id_user == id_conserje).first()
        if conserje:
            conserje.name = user.name
            conserje.last_name = user.last_name
            conserje.email = user.email
            conserje.cargo = user.cargo
            conserje.antecedentes = user.antecedentes
            conserje.direccion = user.direccion
            conserje.telefono = user.telefono
            conserje.foto = foto

            self.session.commit()
            self.session.refresh(conserje)

        return conserje


    # def update_conserje(self, id_conserje:str, foto, user:UpdateConserje, get_conserje):
    #     self.session.query(Conserje).filter(Conserje.id_user==id_conserje).update(
    #         {'name': user.name, 'last_name': user.last_name, 'email': user.email,
    #          'cargo':user.cargo, 'antecedentes':user.antecedentes, 'direccion': user.direccion,
    #          'telefono': user.telefono, 'foto': foto}
    #     )
    #     self.session.commit()
    #     self.session.refresh(get_conserje)

    #     return get_conserje