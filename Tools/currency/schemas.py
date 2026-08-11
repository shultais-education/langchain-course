from pydantic import BaseModel, Field
from langchain.agents import AgentState


class ToolAnswer(BaseModel):
    answer: str = Field(description="Ответ")
    answer_date: str = Field(description="Дата ответа")


class AgentContext(BaseModel):
    user_id: int
    db: dict


class StateSchema(AgentState):
    models_calls: int
