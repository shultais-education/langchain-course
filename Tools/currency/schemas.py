from pydantic import BaseModel, Field


class ToolAnswer(BaseModel):
    answer: str = Field(description="Ответ")
    answer_date: str = Field(description="Дата ответа")
