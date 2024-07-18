# Criar a rota assicrona no arquivo routers.py

from fastapi import APIRouter
from converter import sync_converter, async_converter ### importar a função (async_converter)
from asyncio import gather  ### para utilizar as coroutines

router = APIRouter(prefix='/converter')  ##### quando todas as rotas tiverem o mesmo prefixo (comecarem da mesma forma)


@router.get('/{from_currency}')         ##### rota sincrona
async def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')

    result = []

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_corrency=currency,
            price=price
        )

        result.append(response)

    return result


@router.get('/async/{from_currency}')         ##### rota asincrona
async def async_converter_router(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')

    coroutines = [] ### Lista de corotinas

    for currency in to_currencies:
        coro = async_converter(     ##retorna as corotinas
            from_currency=from_currency,
            to_corrency=currency,
            price=price
        )

        coroutines.append(coro)

    result = await gather(*coro)   ##### * sintaxe de integracao de lista
    return result