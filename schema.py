from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .database import BaseSQL


class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
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
