from pydantic import BaseModel, Field


class GeneratedMenu(BaseModel):
    dishes: list[str] = Field(description="Блюда")


class GeneratedRecipe(BaseModel):
    name: str = Field(description="Название рецепта")
    ingredients: list[str] = Field(description="Ингредиенты")
    steps: list[str] = Field(description="Шаги приготовления")
