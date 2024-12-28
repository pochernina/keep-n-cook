from sqlalchemy import Column, DateTime, Integer, ForeignKey, String

from keepncook.db import Base


class Recipes(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    cooking_time = Column(Integer)
    image_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    author_id = Column(ForeignKey("users.id"), nullable=False)


class RecipesSteps(Base):
    __tablename__ = "recipes_steps"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(ForeignKey("recipes.id"), nullable=False)
    number = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    image_id = Column(Integer)


class Ingredients(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image_id = Column(Integer)


class RecipesIngredients(Base):
    __tablename__ = "recipes_ingredients"

    recipe_id = Column(ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(ForeignKey("ingredients.id"), primary_key=True)
    amount = Column(String, nullable=False)
