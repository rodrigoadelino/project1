from fastapi import APIRouter


router = APIRouter()


@router.get('/converter')
def converter():
    return "It works"