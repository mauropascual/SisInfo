from sqlalchemy.orm import Session

from schemas.departamento import DepartamentoBase
from data.models.departamento import Departamento
from .utils import generate_id

class DepartamentoService:
    def __init__(self, session : Session):
        self.session = session

    def get_departamento(self):
        query = self.session.query(Departamento).all()
        return query

    def register_departamento(self, id_administrator,departa: DepartamentoBase):
        id_departamento = generate_id()
        register = Departamento(id_departamento=id_departamento, id_administrator=id_administrator,
                                superficie=departa.superficie, ambientes=departa.ambientes, torre=departa.torre, 
                                direccion=departa.direccion, numero_depar=departa.numero_depar,garaje=departa.garaje, boulera=departa.boulera)
        
        self.session.add(register)
        self.session.commit()
        self.session.refresh(register)

        return register