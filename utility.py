from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
   
)

def translateIt(text,inputLang,outputLang):
    prompt = ChatPromptTemplate.from_messages(
        [
        ("system",
         "You are a helpful assistant that translates {input_language} to {output_language}."
         ),
         ("human","{input}")
        ]
        )
    chain = prompt | llm 
    
    res = chain.invoke({
        "input_language":inputLang,
        "output_language":outputLang,
        
        "input":text,
    })
    return res
#r= translateIt("i love you","English","Hindi")
#print(r.content)



