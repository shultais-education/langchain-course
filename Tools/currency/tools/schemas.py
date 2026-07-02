from pydantic import BaseModel, Field, ConfigDict, field_validator


class ConvertCurrencyArgs(BaseModel):
    amount: float = Field(description="Сумма для конвертации.")
    from_currency: str = Field(min_length=3, max_length=3, description="Код ISO 4217, например USD.")
    to_currency: str = Field(min_length=3, max_length=3, description="Код ISO 4217, например EUR.")

    model_config = ConfigDict(str_strip_whitespace=True)

    @field_validator("from_currency", "to_currency")
    @classmethod
    def upper_code(cls, value: str) -> str:
        return value.upper()
