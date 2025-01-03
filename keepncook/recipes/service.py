from keepncook.recipes.models import Recipes
from keepncook.service.base import BaseService


class RecipesService(BaseService):
    model = Recipes

    @classmethod
    async def get_all_recipes(cls):
        return await cls.find_all()

    @classmethod
    async def get_recipe(cls, recipe_id: int):
        return await cls.find_by_id(recipe_id)
