## Criar um arquivo na raiz do projeto routers.py
from fastapi import APIRouter


router = APIRouter()


@router.get('/converter')
def converter():
    return "It works"


## Adicionar o endpoint no main
from fastapi import FastAPI
from routers import router #importar o router 

app = FastAPI() 
app.include_router(router=router) #inclusão da rota


@app.get('/hello-world')
def hello_world():
    return 'helloWorld!'


## Documentação autogerada
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc