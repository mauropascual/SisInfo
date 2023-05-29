"""db departamento

Revision ID: 6b7c5c8afd5a
Revises: ad1073f8aea2
Create Date: 2023-05-27 23:48:56.884975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b7c5c8afd5a'
down_revision = 'ad1073f8aea2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departamento',
    sa.Column('id_departamento', sa.String(length=4), nullable=False),
    sa.Column('superficie', sa.String(length=50), nullable=False),
    sa.Column('ambientes', sa.String(length=10), nullable=False),
    sa.Column('torre', sa.String(length=20), nullable=False),
    sa.Column('direccion', sa.String(length=100), nullable=False),
    sa.Column('numero_depar', sa.String(length=10), nullable=False),
    sa.Column('garaje', sa.Boolean(), nullable=False),
    sa.Column('boulera', sa.Boolean(), nullable=False),
    sa.Column('id_administrator', sa.String(length=4), nullable=True),
    sa.ForeignKeyConstraint(['id_administrator'], ['administrator.id_user'], ),
    sa.PrimaryKeyConstraint('id_departamento')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('departamento')
    # ### end Alembic commands ###