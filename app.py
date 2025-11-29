

import streamlit as st
import os
from retriever import build_retriever
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="HR Assistant", layout="centered")
st.title("🤖 HR Assistant Agent")

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_KEY:
    st.error("Please set OPENAI_API_KEY in your environment or .env file.")
    st.stop()

query = st.text_input("Ask a question ")

if st.button("Submit"):
    if not query.strip():
        st.warning("Please type a question.")
    else:
        with st.spinner("Preparing HR Assistant..."):
            retriever = build_retriever()

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff"
        )

        with st.spinner("Generating response..."):
            answer = qa_chain.run(query)

        st.subheader("Answer")
        st.write(answer)
