import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


def main():
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask Questions to your PDF ")
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = " "
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function =len
        )
        chunks = text_splitter.split_text(text)
        #embedding used to convert the cunks in to vector representation
        embeddings = OpenAIEmbeddings()
        #used facbook semantic serach ai to build knowledge base 
        knowledge_base = FAISS.from_texts(chunks,embeddings)

        user_question = st.text_input("Ask a question respect to the content of your PDF")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            llm = OpenAI()
            chain = load_qa_chain(llm,chain_type="stuff")
            response = chain.run(input_documents = docs, question=user_question)
            st.write(response) 
            
if __name__ == '__main__':
    main()


