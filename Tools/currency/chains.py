from Tools.currency.prompts import currency_prompt
from Tools.currency.models import currency_model

from langchain_core.output_parsers import JsonOutputToolsParser, JsonOutputKeyToolsParser

tools_parser = JsonOutputKeyToolsParser(first_tool_only=True, return_id=True, strict=True, key_name="convert_currency")


currency_chain = currency_prompt | currency_model | tools_parser
