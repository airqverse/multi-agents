from typing import Optional
from langchain_core.runnables import Runnable, RunnableConfig

def increment_x_by_one(x: int) -> int:
    return x+1

def fake_llm(x: int)->str:
    return f"Result = {x}"

class MyFirstChain(Runnable[int,str]):
    def invoke(
        self, input:str, config: Optional[RunnableConfig]=None
    )->str:
        increment=increment_x_by_one(input)
        return fake_llm(increment)
