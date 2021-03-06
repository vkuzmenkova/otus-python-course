"""alter default

Revision ID: 84bb02770633
Revises: f1498c4c6c6a
Create Date: 2021-09-13 12:33:18.142899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84bb02770633'
down_revision = 'f1498c4c6c6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blog_authors', 'bio',
               existing_server_default=sa.text("Hey, I'm using App!"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blog_authors', 'bio',
               existing_server_default=sa.text("'Draft'"))
    # ### end Alembic commands ###
