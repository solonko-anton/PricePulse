from fastapi import Depends
from src.models.create_table import get_session
from src.api.olx.parser import parse_fridgers
from fastapi import APIRouter

router = APIRouter(prefix='/olx')

@router.get('/fridgers')
async def get_olx_fridgers(session=Depends(get_session)):
    return parse_fridgers()

