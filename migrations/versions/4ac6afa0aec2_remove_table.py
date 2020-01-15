"""remove_table

Revision ID: 4ac6afa0aec2
Revises: 07e35f39f114
Create Date: 2020-01-12 09:18:33.714118

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ac6afa0aec2'
down_revision = '07e35f39f114'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_bgm_timeline_time', table_name='bgm_timeline')
    op.drop_index('ix_bgm_timeline_user_id', table_name='bgm_timeline')
    op.drop_index('ix_bgm_timeline_user_name', table_name='bgm_timeline')
    op.drop_table('bgm_timeline')
    op.drop_table('subjectjson')
    op.drop_table('map')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'map',
        sa.Column(
            'id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_table(
        'subjectjson',
        sa.Column(
            'id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False
        ),
        sa.Column('info', mysql.LONGTEXT(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_table(
        'bgm_timeline',
        sa.Column(
            'id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False
        ),
        sa.Column('user_name', mysql.VARCHAR(length=255), nullable=False),
        sa.Column(
            'user_id',
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=False
        ),
        sa.Column(
            'time',
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_index(
        'ix_bgm_timeline_user_name', 'bgm_timeline', ['user_name'], unique=False
    )
    op.create_index(
        'ix_bgm_timeline_user_id', 'bgm_timeline', ['user_id'], unique=False
    )
    op.create_index('ix_bgm_timeline_time', 'bgm_timeline', ['time'], unique=False)
    # ### end Alembic commands ###
