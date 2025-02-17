from fastapi import APIRouter
from converter import sync_converter, async_converter
from asyncio import gather

router = APIRouter(prefix='/converter')


@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
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


@router.get('/async/{from_currency}')
async def async_converter_router(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')

    couroutines = []

    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency,
            to_corrency=currency,
            price=price
        )

        couroutines.append(coro)

    result = await gather(*couroutines)
    return result   