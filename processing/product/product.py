

# with db_helper.get_resource() as (cursor, _):
#     cursor.execute('select * from users')
#     for record in cursor.fetchall():
import json

from processing.db.db_helper import db_helper


def findUser():
    # (cursor, _) = db_helper.get_resource()
    with db_helper.get_resource() as (cursor, _):
        cursor.execute('select * from users')
        users = list()
        for record in cursor.fetchall():

            name = record['name']
            age = record['age']
            print(name)
            user = User(name, age)
            # user.name = name
            # user.age = age
            users.append(user)
    return users


class User:
    name:str
    age:int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age
        }

    def serialize(self):
        return {'name': self.name}

    def to_json(self):
        return json.dumps({'name': self.name})
