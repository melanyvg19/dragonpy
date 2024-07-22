from pydantic import BaseModel, Field
from datetime import date

class AliadoDTORequest(BaseModel):
    nombre: str
    direccion: str
    aporteMonetario: float
    class Config:
        orm_mode = True

class AliadoDTOResponse(BaseModel):
    id: int
    nombre: str
    direccion: str
    aporteMonetario: float
    class Config:
        orm_mode = True

class DragonDTORequest(BaseModel):
    nombre: str
    edad: int
    altura: float
    numeroVictorias: int
    class Config:
        orm_mode = True
    
class DragonDTOResponse(BaseModel):
    id: int
    nombre: str
    edad: int
    altura: float
    numeroVictorias: int
    class Config:
        orm_mode = True

class JineteDTORequest(BaseModel):
    nombre: str
    fechaMontura: date
    edad: int
    class Config:
        orm_mode = True

class JineteDTOResponse(BaseModel):
    id: int
    nombre: str
    fechaMontura: date
    edad: int
    class Config:
        orm_mode = True
