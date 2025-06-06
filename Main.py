from fastapi import FastAPI
from app.database.connection import create_db
from app.controllers import usuario_controller, time_controller, jogador_controller, partida_controller, estatistica_controller

app = FastAPI()

@app.on_event("startup")
async def startup():
    create_db()

app.include_router(usuario_controller.router)
app.include_router(time_controller.router)
app.include_router(jogador_controller.router)
app.include_router(partida_controller.router)
app.include_router(estatistica_controller.router)
