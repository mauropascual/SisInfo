from sqlalchemy import Column, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from data import Base

class Departamento(Base):
    __tablename__ = 'departamento'
    id_departamento = Column(String(4), primary_key=True)
    superficie = Column(String(50), nullable=False)
    ambientes = Column(String(10), nullable=False)
    torre = Column(String(20), nullable=False)
    direccion = Column(String(100), nullable=False)
    numero_depar= Column(String(10), nullable=False)
    garaje = Column(Boolean, nullable=False, default=False)
    boulera = Column(Boolean, nullable=False, default=False)
    id_administrator = Column(String(4), ForeignKey('administrator.id_user'))

    administrator = relationship("Administrator", back_populates="departamentos")