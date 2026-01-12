import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Changed from Ollama to OpenAI
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import time
def type_effect(text, delay=0.01):
    placeholder = st.empty()
    output = ""
    for char in text:
        output += char
        placeholder.markdown(output)
        time.sleep(delay)

#streamlit framework
st.title("MY PERSONASL CHAT APP")

os.environ["LANGCHAIN_TRACING_V2"] = "true"


st.sidebar.header("Configuartion")
openaikey=st.sidebar.text_input("OpenAI API Key",key="openai_api_key",type="password")
langchain_project=st.sidebar.text_input("Langchain Project Name",key="langchain_project")
langchain_api_key=st.sidebar.text_input("Langchain API Key",key="langchain_api_key",type="password")


if openaikey and langchain_api_key and langchain_project:
    os.environ["OPENAI_API_KEY"] = openaikey
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    os.environ["LANGCHAIN_PROJECT"]=langchain_project

    ##use ollama llm model
    prompt=ChatPromptTemplate.from_messages(
        [
            ("system","You are a helpful assistant.please response tot he question asked"),
            ("user","Question: {question}"),
        ]
    )
    
    input_text=st.text_input("Enter your question here:")

    #GEMMA MMODEL
    llm=ChatOpenAI(model="gpt-4o")
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    if input_text:
        text=chain.invoke({"question":input_text})
        type_effect(text)
else:
    st.warning("Please enter all the configuration details in sidebar to proceed.")