from sqlalchemy import Column, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

from .user import User

class Copropietario(User):
    __tablename__ = 'copropietario'
    id_user = Column(String(4), ForeignKey('user.id_user'), primary_key=True)
    carnet= Column(String(10), nullable=False)
    direccion = Column(String(60), nullable=True)
    telefono = Column(String(20), nullable=True)
    foto = Column(LargeBinary((2**32)-1))
    id_departamento = Column(String(4), ForeignKey('departamento.id_departamento'))

    
    __mapper_args__ = {
        'polymorphic_identity': 'copropietario'
    }