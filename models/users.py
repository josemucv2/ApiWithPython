from config.database import Base
from sqlalchemy import Column, String,Integer

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name= Column(String)
    email= Column(String)
    last_name = Column(String)
    username= Column(String)
    identification = Column(String)
    password = Column(String)
    