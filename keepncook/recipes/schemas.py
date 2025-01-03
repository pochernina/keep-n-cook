from datetime import datetime
from pydantic import BaseModel


class SRecipe(BaseModel):
    id: int
    title: str
    description: str
    cooking_time: int
    image_id: int
    created_at: datetime
    author_id: int
