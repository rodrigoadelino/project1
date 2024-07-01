## Path Paramater (parametro vai no endpoint)

from fastapi import FastAPI
from routers import router

app = FastAPI() 
app.include_router(router=router)


@app.get('/converter/{from_currency}') #inclusão do Parameter
def converter(from_currency: str):  # definindo-o como uma string
    return 'It Works'