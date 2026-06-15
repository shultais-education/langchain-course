from langchain_core.callbacks import BaseCallbackHandler


class BaseCallback(BaseCallbackHandler):

    def on_chain_start(self, serialized: dict, inputs: dict, run_id, **kwargs):
        parent_run_id = kwargs.get("parent_run_id")
        if parent_run_id is None:
            print(f"Начало корневой цепочки: {run_id}")
        else:
            print(f"Старт: {parent_run_id} -> {run_id}")
            print(inputs)
            print()

    def on_chain_end(self, outputs: dict, run_id, **kwargs):
        parent_run_id = kwargs.get("parent_run_id")
        if parent_run_id is None:
            print(f"Конец корневой цепочки: {run_id}")
        else:
            print(f"Конец: {parent_run_id} -> {run_id}")
            print(outputs)
            print()

    def on_chat_model_start(self, serialized: dict, messages: dict, **kwargs):
        print("Старт запроса к LLM")
        print(messages)
        print()
