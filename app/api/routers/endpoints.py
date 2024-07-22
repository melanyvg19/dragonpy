from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.dto import DragonDTORequest,DragonDTOResponse, JineteDTORequest, JineteDTOResponse, AliadoDTORequest, AliadoDTOResponse
from app.api.models.tablas import Dragon,Jinete,Aliado
from app.database.config import SessionLocal, engine

rutas=APIRouter()

def gerDB():
    db = SessionLocal()    
    try:    
        yield db   
    except Exception as e:       
          db.rollback()  
          raise e
    finally: db.close()

    #EndPoints para el api

    def crearDragon(dragon:DragonDTORequest,db:Session=Depends(gerDB)):
        nuevoDragon=Dragon(nombre=dragon.nombre,edad=dragon.edad,altura=dragon.altura,numeroVictorias=dragon.numeroVictorias)
        db.add(nuevoDragon)
        db.commit()
        db.refresh(nuevoDragon)
        return nuevoDragon
    
    def buscarDragones():
         pass
    
    def buscarDragonPorId():
         pass
    
    def modificarDragonPorId():
         pass
    
    def eliminarDragonPorId():
         pass