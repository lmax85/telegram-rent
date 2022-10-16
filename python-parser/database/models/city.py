# coding=utf-8

from sqlalchemy import Column, String, BigInteger, TIMESTAMP, ForeignKey
from database.database import Base

class City(Base):
    __tablename__ = 'cities'

    id=Column(BigInteger, primary_key=True, unique=True)
    name=Column(String(255), nullable=True, unique=True)
    country_id=Column(BigInteger, ForeignKey('countries.id'), nullable=False)
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
