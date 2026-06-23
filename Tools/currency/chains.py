from Tools.currency.prompts import currency_prompt
from Tools.currency.models import currency_model


currency_chain = currency_prompt | currency_model
