# coding=utf-8

from database.base import Base, Session, engine
from database.models.author import Author
from database.models.city import City
from database.models.country import Country
from database.models.group import Group
from database.models.message import Message
from database.models.photo import Photo
from sqlalchemy.dialects.postgresql import insert

# 1 - generate database schema
Base.metadata.create_all(engine)

# 2 - create a new session
session = Session()

def session_close():
    session.close()

# @example for Authors
#[
#    {"id": 123, "username": "Username 1 edited", "first_name": "First name 1 edited", "type": "Type 1"},
#    {"id": 124, "username": "Username 2 edited", "first_name": "First name 2", "type": "Type 2"},
#    {"id": 125, "username": "Username 3 edited", "first_name": "First name 3", "type": "Type 3"},
#    {"id": 126, "username": "Username 4 new", "first_name": "First name 4", "title": "Title 4", "type": "Type 4", "avatar": "Avatar 4", "description": "Description 4"}
#]
def upsertBulk(model, values, constraintKey, updateKeys):
    values = removeDuplicates(values)
    stmt = insert(model).values(values)
    setValues = {}
    for key in updateKeys:
        setValues[key] = stmt.excluded[key]

    stmt = stmt.on_conflict_do_update(
        # Let's use the constraint name which was visible in the original posts error msg
        constraint=constraintKey,

        # The columns that should be updated on conflict
        set_=setValues
    )
    session.execute(stmt)
    session.commit()

def removeDuplicates(values):
    return list({v['id']:v for v in values}.values())

def get_authors():
    authors = session.query(Author).all()
    session.flush()
    return authors

def get_country_by_name(name):
    return session.query(Country).filter(Country.name == name).first()

def insert_country(name):
    country = Country(name=name)
    session.add(country)
    session.flush()
    return country

def get_city_by_name(name):
    return session.query(City).filter(City.name == name).first()

def insert_city(name, country_id):
    city = City(name=name, country_id=country_id)
    session.add(city)
    session.flush()
    return city

def get_group_by_name(username):
    return session.query(Group).filter(Group.username == username).first()

def update_channel(channel, channelAvatarPath):
    group = session.query(Group).filter(Group.id == channel.id).first()
    if group is None:
        group = Group(id=channel.id)
    group.username=channel.username
    group.title=channel.title
    group.avatar_path=channelAvatarPath
    session.add(group)
    session.flush()

def upsertParsedData(data):
    if data.get('photos', None) != None and len(data['photos']) > 0:
        upsertPhotos(data['photos'])
    if data.get('authors', None) != None and len(data['authors']) > 0:
        upsertAuthros(data['authors'])
    if data.get('messages', None) != None and len(data['messages']) > 0:
        upsertMessages(data['messages'])

def upsertAuthros(values):
    upsertBulk(Author, values, "telegram_authors_pkey", ["username", "first_name", "last_name", "title", "avatar_path"])
def upsertMessages(values):
    upsertBulk(Message, values, "telegram_messages_pkey", ["text", "price"])
def upsertPhotos(values):
    upsertBulk(Photo, values, "telegram_photos_pkey", ["path"])