from langchain_core.runnables import RunnableSequence, RunnableLambda

def increment_x_by_one(x: int) -> int:
    return x+1

def fake_llm(x: int)->str:
    return f"Result = {x}"

a = (
        RunnableLambda(increment_x_by_one)|
        RunnableLambda(fake_llm)
    )

b = RunnableSequence(
        RunnableLambda(increment_x_by_one),
        RunnableLambda(fake_llm)
    )

print(a==b) # True
