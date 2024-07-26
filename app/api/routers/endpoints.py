from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.dto import DragonDTORequest,DragonDTOResponse, JineteDTORequest, JineteDTOResponse, AliadoDTORequest, AliadoDTOResponse
from app.api.models.tablas import Dragon,Jinete,Aliado
from app.database.config import SessionLocal, engine

rutas=APIRouter()

def getDB():
    db = SessionLocal()    
    try:    
        yield db   
    except Exception as e:       
          db.rollback()  
          raise e
    finally: db.close()

    #EndPoints para el api
    @rutas.post("/dragones", response_model=DragonDTOResponse, summary="Crea un dragon en la BD")
    def crearDragon(datosCliente:DragonDTORequest, db:Session =Depends(getDB())):
        try:
             dragon=Dragon(
                  nombre=datosCliente.nombre, 
                  edad= datosCliente.edad,
                  altura=datosCliente.altura,
                  numeroVictorias= datosCliente.numeroVictorias
              )
             db.add(dragon) #orden en bd
             db.commit()
             db.refresh(dragon)
             return dragon
        except Exception as error:
             db.rollback()
             raise HTTPException(status_code=500, detail= "Tenemos un problema en el servidor")

    
    @rutas.get("/dragones", response_model=List[DragonDTOResponse], summary="Buscar todos los dragones en la BD")
    def buscarDragones(db:Session=Depends(getDB())):
         try:
              dragones=db.query(Dragon).all()
              return dragones
         except Exception as error:
              raise HTTPException(status_code=500, detail= "Tenemos un problema en el servidor")
    
    @rutas.get("/dragones/{id}", response_model=DragonDTOResponse, summary="Buscar un dragon por id")
    def buscarDragonPorId(id: int, db:Session=Depends(getDB())):
         try:
              dragon=db.query(Dragon).get(id)
              return dragon  
         except Exception as error:
              raise HTTPException(status_code=500, detail= "Tenemos un problema en el servidor")
    
    @rutas.get("/dragones/", response_model=DragonDTOResponse, summary="Modificar un dragon")
    def modificarDragonPorId():
         pass
    
    def eliminarDragonPorId():
         pass
    
    @rutas.post("/jinetes", response_model=JineteDTOResponse, summary="Crea un jinete en la BD")
    def crearJinete(datosCliente:JineteDTORequest, db:Session =Depends(getDB())):
        try:
             jinete=Jinete(
                  nombre=datosCliente.nombre, 
                  edad= datosCliente.edad,
                  fechaMontura= datosCliente.fechaMontura   
              )
             db.add(jinete) #orden en bd
             db.commit()
             db.refresh(jinete)
             return jinete
        except Exception as error:
             db.rollback()
             raise HTTPException(status_code=500, detail= "Tenemos un problema en el servidor") 
         
    @rutas.get("/jinetes", response_model=List[JineteDTOResponse], summary="Buscar todos los jinetes en la BD")
    def buscarJinetes(datosCliente:JineteDTORequest, db:Session=Depends(getDB())):
         try:
              jinetes=db.query(Jinete).all()
              return jinetes
         except Exception as error:
              raise HTTPException(status_code=500, detail= "Tenemos un problema en el servidor")
         
    @rutas.get("/jinetes/{id}", response_model=JineteDTOResponse, summary="Buscar un jinete por id")
    def buscarJinetePorId(id: int, db:Session =Depends(getDB()) ):
         try:
              jinete=db.query(Jinete).get(id)
              return jinete
         except Exception as error:
              raise HTTPException(status_code=500, detail= "Tenemos un problema en el servidor")