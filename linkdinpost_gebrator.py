from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.0
)

prompt = PromptTemplate(
    input_variables=["topic", "tone", "targeted_audiance"],
    template="""
You are an AI assistant optimized to write linkdin posts.

Write a professional post about {topic}.

tone: {tone}

targeted_audiance: {targeted_audiance}
"""
)

topic = input("Topic: ")
tone = input("Tone: ")
targeted_audiance = input("Targeted Audience: ")

final_prompt = prompt.format(
    topic=topic,
    tone=tone,
    targeted_audiance=targeted_audiance
)

response = llm.invoke(final_prompt)

print("\nGenerated LinkedIn Post:\n")
print(response.content)