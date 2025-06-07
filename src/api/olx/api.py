from fastapi import Depends
from src.models.create_table import get_session
from src.main import app



@app.get('olx/fridgers')
def get_olx_fridgers(session= Depends(get_session())):
    pass

