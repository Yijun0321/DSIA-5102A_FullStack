from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Pokemon(Base):
    __tablename__ = "Pokemon"
    Types = Column(String)
    Abilities = Column(String)
    Tier = Column(String)
    HP = Column(int)
    Defense = Column(int)
    Special_Attack = Column(int)
    Special_Defense = Column(int)
    Speed = Column(int)
    Next_Evolution = Column(String)
    Moves = Column(String)
