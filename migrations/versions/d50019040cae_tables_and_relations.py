"""tables and relations
Revision ID: d50019040cae
Revises: 
Create Date: 2021-12-05 16:56:39.038150
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd50019040cae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('rental',
    sa.Column('rental_id', sa.Integer(), nullable=False),
    sa.Column('rented', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('rental_id')
    )
    op.create_table('association',
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.author_id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], )
    )
    op.create_table('rent',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('rental_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['rental_id'], ['rental.rental_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rent')
    op.drop_table('association')
    op.drop_table('rental')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###