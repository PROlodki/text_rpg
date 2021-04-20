import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin

# формируем связь многие ко многим к персонажам через промежуточную таблицу inventory


items_in_room = sqlalchemy.Table(
    'items_in_room',  # название промежуточной таблицы в базе
    SqlAlchemyBase.metadata,
    # что с чем связываем - rooms.id с
    sqlalchemy.Column('room_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('rooms.id')),
    # items.id
    sqlalchemy.Column('item_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('items.id'))
)


class Items(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    item_type_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('item_types.id'))

    attack_armor = sqlalchemy.Column(sqlalchemy.Integer, default=1)
