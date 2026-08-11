from pydantic import BaseModel, Field, ConfigDict, field_validator
from langchain.tools import ToolRuntime
from Tools.currency.schemas import AgentContext


class ConvertCurrencyArgs(BaseModel):
    amount: float = Field(description="Сумма для конвертации.")
    from_currency: str = Field(min_length=3, max_length=3, description="Код ISO 4217, например USD.")
    to_currency: str = Field(min_length=3, max_length=3, description="Код ISO 4217, например EUR.")
    runtime: ToolRuntime[AgentContext]

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)

    @field_validator("from_currency", "to_currency")
    @classmethod
    def upper_code(cls, value: str) -> str:
        return value.upper()
