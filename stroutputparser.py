from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os


# Initialize ChatOpenAI with correct param
model = ChatOpenAI(
    model="google/gemma-1.5-xxl",  
    api_key="_"
)

# 1st prompt
template1 = PromptTemplate(
    template="Write a detailed report on the following topic:\n{topic}",
    input_variables=["topic"]
)
prompt1 = template1.invoke({"topic": "Data Science"})
result = model.invoke(prompt1)

# 2nd prompt
template2 = PromptTemplate(
    template="Write a 7 line summary on the following topic:\n{text}",
    input_variables=["text"]
)
prompt2 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt2)

print(result1.content)