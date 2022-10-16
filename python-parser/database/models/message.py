# coding=utf-8

from sqlalchemy import Column, String, Text, BigInteger, TIMESTAMP, ForeignKey
from database.database import Base

class Message(Base):
    __tablename__ = 'telegram_messages'

    id = Column(BigInteger, primary_key=True, unique=True)
    telegram_group_id=Column(BigInteger, ForeignKey('telegram_groups.id'), nullable=False)
    telegram_author_id=Column(BigInteger, ForeignKey('telegram_authors.id'), nullable=False)
    city_id=Column(BigInteger, ForeignKey('cities.id'), nullable=False)
    grouped_id=Column(BigInteger, nullable=False)
    text=Column(Text, nullable=False)
    price=Column(BigInteger, nullable=True)
    created_at=Column(TIMESTAMP, nullable=True)
    updated_at=Column(TIMESTAMP, nullable=True)
    deleted_at=Column(TIMESTAMP, nullable=True)

    # def __init__(self, id, username, first_name, last_name, title, type, avatar, description):
    #     self.id = id
    #     self.username = username
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.title = title
    #     self.type = type
    #     self.avatar = avatar
    #     self.description = description
