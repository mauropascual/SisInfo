from sqlalchemy import Column, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

from .user import User

class Conserje(User):
    __tablename__ = 'conserje'
    id_user = Column(String(4), ForeignKey('user.id_user'), primary_key=True)
    cargo = Column(String(20), nullable=False)
    carnet= Column(String(10), nullable=False)
    antecedentes = Column(String(50), nullable=False)
    foto = Column(LargeBinary((2**32)-1))
    
    __mapper_args__ = {
        'polymorphic_identity': 'conserje'
    }