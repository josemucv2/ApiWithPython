from config.database import Base
from sqlalchemy import Column , Integer ,String

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    title = Column(String)
    price= Column(Integer)
    description = Column(String)
    category = Column(String)
    image = Column(String)

