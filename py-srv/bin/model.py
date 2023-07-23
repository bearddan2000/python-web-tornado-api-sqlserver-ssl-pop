from sqlalchemy import Column, Integer, String
from tornado_sqlalchemy import SQLAlchemy

import settings

database_url = '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    )

db = SQLAlchemy(url=database_url)

class PopModel(db.Model):
    __tablename__ = 'pop'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    name = Column(String(20))
    color = Column(String(10))

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return "<Pop('%s', '%s')>" % (self.name, self.color)
