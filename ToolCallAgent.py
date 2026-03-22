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


def run_agent(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful AI agent that can use tools."},
        {"role": "user", "content": user_input}
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-5.3",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message
        messages.append(message)

        #If tool is called this will work
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                # Calling the actual function
                if tool_name == "calculator":
                    result = calculator(**arguments)
                elif tool_name == "search_tool":
                    result = search_tool(**arguments)
                else:
                    result = "Unknown tool"

                #Add the tool response
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

        else:
            #Final response
            return message.content



if __name__ == "__main__":
    while True:
        query = input("You: ")
        answer = run_agent(query)
        print("Agent:", answer)
