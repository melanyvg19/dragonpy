from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Aliado(Base):
    __tablename__ = 'aliados'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    ubicacion = Column(String(70))
    aporteMonetario = Column(Float)
    
class Dragon(Base):
    __tablename__ = 'dragones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    edad = Column(Integer)
    altura = Column(Float)
    numeroVictorias=Column(Integer)
    aliado_id = Column(Integer, ForeignKey('aliados.id'))
    aliado = relationship("Aliado", back_populates="dragones")

class Jinete(Base):
    __tablename__ = 'jinetes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    fechaMontura = Column(Date)
    edad = Column(Integer)
    aliado_id = Column(Integer, ForeignKey('aliados.id'))
    aliado = relationship("Aliado", back_populates="jinetes")