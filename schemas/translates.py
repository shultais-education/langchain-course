# [{"language": "язык", "text": "..."}, ]
from pydantic import BaseModel, Field


class Translation(BaseModel):
    language: str = Field(description="Язык")
    text: str = Field(description="Перевод")


class TranslatedText(BaseModel):
    translates: list[Translation] = Field(description="Список переводов")
