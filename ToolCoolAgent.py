import json
from openai import OpenAI

client = OpenAI()


#CALCULATOR TOOL 
def calculator(expression: str):
    try:
        return str(eval(expression))
    except:
        return "Error in calculation"

def search_tool(query: str):
    # mock search (replace with real API later)
    return f"Search results for '{query}': [Sample data]"


