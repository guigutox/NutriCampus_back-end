from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from database import Base, engine
from scraping import timer
from routers import alimento_route, usuario_route, cardapio_route

Base.metadata.create_all(bind=engine)

timer.setup_scrape_jobs()
app = FastAPI()

app.include_router(usuario_route.router)
app.include_router(alimento_route.router)
app.include_router(cardapio_route.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}
