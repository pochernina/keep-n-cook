import uvicorn
from fastapi import FastAPI

from keepncook.recipes.router import router as router_recipes


app = FastAPI()

app.include_router(router_recipes)

if __name__ == "__main__":
    uvicorn.run("keepncook.main:app", reload=True)
