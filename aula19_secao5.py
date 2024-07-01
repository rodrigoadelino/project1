## Query Params (passa uma chave e valor na url)
## /url?to_currencies=USD,EUR,GBP&price=5.55

from fastapi import FastAPI
from routers import router

app = FastAPI() 
app.include_router(router=router)


@app.get('/converter/{from_currency}') 
def converter(from_currency: str, to_currencies: str, price: float):  # definindo-o as chaves e tipo
    return 'It Works'