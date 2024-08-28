"""empty message

Revision ID: eb0b85608c0a
Revises: 00534dc350db
Create Date: 2024-08-28 15:10:04.219389

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from tidb_vector.sqlalchemy import VectorType
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "eb0b85608c0a"
down_revision = "00534dc350db"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "documents",
        "mime_type",
        existing_type=mysql.VARCHAR(length=64),
        type_=sa.String(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "uploads",
        "mime_type",
        existing_type=mysql.VARCHAR(length=64),
        type_=sa.String(length=128),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "uploads",
        "mime_type",
        existing_type=sa.String(length=128),
        type_=mysql.VARCHAR(length=64),
        existing_nullable=False,
    )
    op.alter_column(
        "documents",
        "mime_type",
        existing_type=sa.String(length=128),
        type_=mysql.VARCHAR(length=64),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
