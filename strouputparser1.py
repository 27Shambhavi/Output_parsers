from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
print(parser)

import os


# Initialize ChatOpenAI with correct param
model = ChatOpenAI(
    model="claude-3-haiku-20240307",  
    api_key="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"
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
parser=StrOutputParser()
chain=template1 | model | parser | template2 | model
prompt2 = template2.invoke({"text": result.content})
chain.invoke({"topic": "Data Science"})
result= chain.invoke(prompt2)
