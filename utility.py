from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import pandas as pd
import streamlit as st



def askBot(df: pd.DataFrame,query: str) -> str:
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-4",openai_api_key=st.secrets['OPENAI_API_KEY']),
        df,
        verbose=False,
    )
    return agent.run(query)



if __name__ == "__main__":
    df = pd.read_csv("differnece - 副本.csv")
    print(askBot(df=df,query='how many rows are there?'))