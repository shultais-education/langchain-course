from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, Runtime
from Tools.currency.schemas import AgentContext


@before_agent
def before_agent_middleware(state: dict, runtime: Runtime[AgentContext]):
    print("🍰 before_agent")
    print("    messages:", len(state["messages"]))
    print("    context:", runtime.context)
    return None


@after_agent
def after_agent_middleware(state: dict, runtime: Runtime[AgentContext]):
    print("🍰 after_agent")
    print("    messages:", len(state["messages"]))
    print("    context:", runtime.context)
    print("    models_calls:", state["models_calls"])
    return None


@before_model
def before_model_middleware(state: dict, runtime: Runtime[AgentContext]):
    print("🍰 before_model")
    print("    messages:", len(state["messages"]))
    print("    context:", runtime.context)
    return None


@after_model
def after_model_middleware(state: dict, runtime: Runtime[AgentContext]):
    print("🍰 after_model")
    print("    messages:", len(state["messages"]))
    print("    context:", runtime.context)
    return {"models_calls": state["models_calls"] + 1}
