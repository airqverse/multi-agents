from langchain_core.runnables import RunnableParallel, RunnableLambda

def plus_one(x: int) -> int:
    return x + 1

def fake_llm(x: int) -> str:
    return f"Result = {x}"

chain = RunnableParallel(
    step1 = (plus_one | RunnableLambda(fake_llm)),
    step2 = RunnableLambda(fake_llm)
)

print(chain.invoke(1))

