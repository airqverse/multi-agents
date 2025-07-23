from langchain_core.runnables import RunnableParallel, RunnableLambda

def plus_one(x: int) -> int:
    return x + 1

def fake_llm(x: int) -> str:
    return f"Result = {x}"

chain1 = RunnableParallel(
    step1 = (plus_one | RunnableLambda(fake_llm)),
    step2 = RunnableLambda(fake_llm)
)

chain2 = (plus_one | chain1)

print("chain1:")
print(chain1.invoke(1))
print("chain2:")
print(chain2.invoke(1))

# Parallel chains using dictionary
chain3 = (RunnableLambda(plus_one) | {"step1": plus_one | RunnableLambda(fake_llm), "step2": fake_llm})
print(chain2 == chain3)
