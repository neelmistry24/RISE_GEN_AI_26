import math
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_groq import ChatGroq

load_dotenv()


@tool
def calculator(expression: str) -> str:
    """Evaluate numeric expression."""
    try:
        result = eval(expression, {"math": math, "__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error calculating: {e}"


@tool
def email_generator(details: str) -> str:
    """Generate email. Format: to | subject | name"""
    try:
        to, subject, name = details.split("|")

        return f"""
To: {to.strip()}
Subject: {subject.strip()}

Dear {to.strip()},

I hope you are doing well.

My name is {name.strip()}. I am writing regarding "{subject.strip()}".
Please let me know your response.

Thank you.

Regards,
{name.strip()}
"""
    except:
        return "Use format: to | subject | name"


llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


if __name__ == "__main__":
    print("\nAI Agent Started")
    print("Ask:")
    print("- calculate 100+120")
    print("- email Rahul | Internship Request | Neel")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        if user_input.lower().startswith("calculate"):
            expression = user_input.lower().replace("calculate", "").strip()
            print("\nAgent:")
            print(calculator.invoke(expression))

        elif user_input.lower().startswith("email"):
            details = user_input.replace("email", "").strip()
            print("\nAgent:")
            print(email_generator.invoke(details))

        else:
            response = llm.invoke(user_input)
            print("\nAgent:")
            print(response.content)