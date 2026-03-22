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

#Tool Definition
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Solve math expressions",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression like 2+2"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_tool",
            "description": "Search for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]



