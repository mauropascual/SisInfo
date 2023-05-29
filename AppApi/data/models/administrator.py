from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .user import User

class Administrator(User):
    __tablename__ = 'administrator'

    id_user = Column(String(4), ForeignKey('user.id_user'), primary_key=True)
    address = Column(String(70), nullable=False)
    user = relationship('User', backref='administrator', uselist=False)

    __mapper_args__ = {
        'polymorphic_identity': 'administrator'
    }
    departamentos = relationship("Departamento", back_populates="administrator")