from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

llm = ChatOpenAI(   
    model = "gpt-4o-mini",
    temperature = 0
)

@tool
def sum_numbers_with_complex_output( numbers: list[int]) -> int:
    """Add a list of numbers"""
    return sum(numbers)

add_agent = create_react_agent (

    model = llm, 
    tools =  [sum_numbers_with_complex_output],

    prompt =  """You are a helpful mathematical assistant that can perform various operations. Use
the tools precisely and explain your reasoning clearly."""
)

response =  add_agent.invoke( 
    {"messages": [("human", "Add the numbers -10, -20, -30")]}
)
#Get the final answer 
final_answer = response ["messages"][-1].content

print(final_answer)