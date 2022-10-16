# coding=utf-8

# 1 - imports
from author import Author
from database.base import Session, engine, Base
from sqlalchemy.dialects.postgresql import insert

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create authors
values = [
    {"id": 123, "username": "Username 1 edited", "first_name": "First name 1 edited", "type": "Type 1"},
    {"id": 124, "username": "Username 2 edited", "first_name": "First name 2", "type": "Type 2"},
    {"id": 125, "username": "Username 3 edited", "first_name": "First name 3", "type": "Type 3"},
    {"id": 126, "username": "Username 4 new", "first_name": "First name 4", "title": "Title 4", "type": "Type 4", "avatar": "Avatar 4", "description": "Description 4"}
]

print(values)

# Prepare all the values that should be "upserted" to the DB
# values = [
#     {"id": 1, "title": "mytitle 1"},
#     {"id": 2, "title": "mytitle 2"},
#     {"id": 3, "title": "mytitle 3"},
#     {"id": 4, "title": "mytitle 4"},
# ]

stmt = insert(Author).values(values)
stmt = stmt.on_conflict_do_update(
    # Let's use the constraint name which was visible in the original posts error msg
    constraint="authors_pkey",

    # The columns that should be updated on conflict
    set_={
        "username": stmt.excluded.username,
        "first_name": stmt.excluded.first_name
    }
)
session.execute(stmt)


# session.add(author1)
# session.add(author2)
# session.add(author3)

# # 10 - commit and close session
session.commit()
session.close()