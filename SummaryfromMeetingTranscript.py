#import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.summarize import load_summarize_chain
#from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os



def main():
        
        loader = PyPDFLoader("shortdesc.pdf")
        docs_raw = loader.load()
        docs_raw_text = [docs.page_content for docs in docs_raw]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=300)
        docs = text_splitter.create_documents(docs_raw_text)


        
        prompt_template =            """Q:Summarize the given article based on the hint
                                      Hint:summary should give details of differnt type of cements;
                                      raw material used ot make the cements;
                                      process follow to make the cement;
                                      world wide opportunity in making the cement;
                                      how IT could help in automating the process:"{docs}"

                                    """
        prompt  = PromptTemplate.from_template(prompt_template)

        llm = OpenAI(temperature=0)
        llm_chain = LLMChain(llm=llm, prompt=prompt)

        #stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="docs")

        #docs = loader.load()
        #print(stuff_chain.run(docs))
      
        chain = load_summarize_chain(llm,chain_type="map_reduce")
        #chain = load_summarize_chain(llm,chain_type="stuff")

        response = chain.run(docs)
        print(response)

    


if __name__ == '__main__':
    main()


