
import streamlit as st
from dotenv import load_dotenv 
#enables application to use the variables inside .env file 

from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
     text = "" 
     for pdf in pdf_docs:
          pdf_reader = PdfReader(pdf)
          #creates a pdf object that has pages
          #allow you to read for each page
          for page in pdf_reader.pages:
               text+= page.extract_text()
               #appends each pages' extracted text to text variable
     return text
     #returning concatenated text

def main():
     st.set_page_config(page_title="PDF Q&A ChatBot", page_icon=":books:")

     st.header("PDF Q&A ChatBot :books:")
     st.text_input("Ask a question about your documents:")

     with st.sidebar:
          st.subheader("Your documents")
          pdf_docs = st.file_uploader(
               "Upload your documents here and click on process", accept_multiple_files=True)
          if st.button("Upload"):
               with st.spinner("Uploading"): #Will process everything inside this loop with a processing spinner (loading symbol)

               # extract text from pdf
                    raw_text = get_pdf_text(pdf_docs)
                    #will take our pdf documents(list of files)
                    #return all of the text content for the pdfs


               # retrieve the chunks of text

               # create vector store (embedded numbers reps of each chunk)





          

    

if __name__ == '__main__':
    main()