from fastapi import FastAPI
from app.database.config import engine
from app.api.models.tablas import Base
from starlette.responses import RedirectResponse
from app.api.routers.endpoints import rutas

#Alistar el ambiente para desarrollar y probar
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(rutas)