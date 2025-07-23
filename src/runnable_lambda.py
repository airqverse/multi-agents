from langchain_core.runnables import RunnableLambda

# ╭────────────────────────────────────────────╮
# │    Simple Example                          │
# ╰────────────────────────────────────────────╯
runnable = RunnableLambda(lambda x: x+1)
response = runnable.invoke(1)
print(response)

# ╭────────────────────────────────────────────╮
# │    My Example                              │
# ╰────────────────────────────────────────────╯
def fibonacci_step(data: dict) -> dict:
    """
    Takes a dict {'x': int, 'y': int} and returns the next step in the
    Fibonacci sequence in the same format.
    """
    x = data['x']
    y = data['y']
    print(x)
    return {'x': y, 'y': x + y}

chain = (
    RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
    | RunnableLambda(fibonacci_step)
)

chain.invoke({'x': 0, 'y': 1})

# ╭────────────────────────────────────────────╮
# │    Bonus                                   │
# ╰────────────────────────────────────────────╯
"""
"a | b" equals to "b.__or__(a)"
"""
print(False | True) # True
print(True.__or__(False)) # True

# ╭────────────────────────────────────────────╮
# │    Bonus                                   │
# ╰────────────────────────────────────────────╯
