

import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_retriever(knowledge_dir="knowledge"):
    docs = []

    for fname in os.listdir(knowledge_dir):
        if fname.endswith(".txt"):
            loader = TextLoader(os.path.join(knowledge_dir, fname), encoding="utf-8")
            docs.extend(loader.load())

    #
    splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = FAISS.from_documents(split_docs, embeddings)

    return vectordb.as_retriever(search_kwargs={"k": 3})
