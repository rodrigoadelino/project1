from fastapi import FastAPI
from routers import router

app = FastAPI() 
app.include_router(router=router)


@app.get('/converter/{from_currency}') 
def converter(from_currency: str, to_currencies: str, price: float):
    return 'It Works'