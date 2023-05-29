from sqlalchemy import Column, String, ForeignKey

from sqlalchemy.orm import relationship
from data import Base

class User(Base):
    __tablename__ = 'user'
    id_user = Column(String(4), primary_key=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable=False)
    user_type = Column(String(20), nullable=False)
    role = Column(String(4), ForeignKey('role.id_role'))
    role_info = relationship('Role', back_populates='users')
    user_permissions = relationship(
        'Permission', secondary='user_permission', back_populates='users')
    
    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }