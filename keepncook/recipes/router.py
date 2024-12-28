from fastapi import APIRouter
from sqlalchemy import select

from keepncook.db import async_session_maker
from keepncook.recipes.models import Recipes


router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.get("")
async def get_recipes():
    async with async_session_maker() as session:
        query = select(Recipes)
        result = await session.execute(query)
        return result.mappings().all()
