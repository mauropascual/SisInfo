from sqlalchemy.orm import Session

from schemas.departamento import DepartamentoBase
from data.models.departamento import Departamento
from .utils import generate_id

class DepartamentoService:
    def __init__(self, session : Session):
        self.session = session

    def get_departamentos(self):
        query = self.session.query(Departamento).all()
        return query

    def register_departamento(self, id_administrator, foto, departa: DepartamentoBase):
        id_departamento = generate_id()
        register = Departamento(id_departamento=id_departamento, id_administrator=id_administrator,
                                superficie=departa.superficie, ambientes=departa.ambientes, torre=departa.torre, 
                                direccion=departa.direccion, numero_depar=departa.numero_depar,garaje=departa.garaje, boulera=departa.boulera, foto=foto)
        
        self.session.add(register)
        self.session.commit()
        self.session.refresh(register)

        return register
    
    def get_departamento(self, id_departamento:str):
        query = self.session.query(Departamento).filter(Departamento.id_departamento==id_departamento).first()
        return query

    def update_departamento(self, id_departamento, foto, departamento: DepartamentoBase, get_departamento):
        self.session.query(Departamento).filter(Departamento.id_departamento==id_departamento).update(
            {"superficie": departamento.superficie, "ambientes": departamento.ambientes,
             "torre":departamento.torre, "direccion":departamento.direccion,
             "numero_depar": departamento.numero_depar, "garaje": departamento.garaje,
             "boulera": departamento.boulera, "foto": foto}
        )

        self.session.commit()
        self.session.refresh(get_departamento)

        return get_departamento
