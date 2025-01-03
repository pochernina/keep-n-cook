from fastapi import APIRouter

from keepncook.recipes.schemas import SRecipe
from keepncook.recipes.service import RecipesService

router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.get("")
async def get_recipes() -> list[SRecipe]:
    return await RecipesService.get_all_recipes()


@router.get("/{id}")
async def get_recipe(id: int) -> SRecipe:
    return await RecipesService.get_recipe(id)
