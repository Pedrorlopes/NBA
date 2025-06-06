from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Jogador(Base):
    __tablename__ = "jogadores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    numero = Column(Integer)
    posicao = Column(String)
    time_id = Column(Integer, ForeignKey("times.id"))
