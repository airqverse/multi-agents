from langchain_core.runnables import RunnableLambda
runnable = RunnableLambda(lambda x: x+1)
response = runnable.invoke(1)
print(response)

def plus_one(x: int) -> int:
    return x + 1

def multiply_by_3(x: int) -> int:
    return x * 3

chain = (
    RunnableLambda(plus_one)
    | RunnableLambda(multiply_by_3)
)

result = chain.invoke(3)
print(result)
