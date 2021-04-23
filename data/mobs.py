import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm


class Mobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'mobs'

    room_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('rooms.id'), primary_key=True)

    mob_id = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey('mobs_list.id'), primary_key=True)

    rooms = orm.relationship("Rooms", backref="mobs")
    mobs = orm.relationship("Mobs_list", backref="rooms")

    hp = sqlalchemy.Column(sqlalchemy.Integer)

    armor = sqlalchemy.Column(sqlalchemy.Integer)
    attack = sqlalchemy.Column(sqlalchemy.Integer)
