from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'

    nickname = Column(String, primary_key=True, index=True)
    streak = Column(Integer, default=0)
