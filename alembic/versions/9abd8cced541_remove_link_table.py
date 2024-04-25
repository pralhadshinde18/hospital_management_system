"""remove link table

Revision ID: 9abd8cced541
Revises: a53492c235cc
Create Date: 2024-04-24 14:13:45.707877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9abd8cced541'
down_revision: Union[str, None] = 'a53492c235cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient_hospital_link')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient_hospital_link',
    sa.Column('hospital_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('patient_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], name='patient_hospital_link_hospital_id_fkey'),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], name='patient_hospital_link_patient_id_fkey')
    )
    # ### end Alembic commands ###