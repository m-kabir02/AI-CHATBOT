# PDF Q&A ChatBot

### A conversational AI powered by Retrieval-Augmented Generation (RAG) that answers questions about your documents.

## 📖 Project Overview

This project is a full-stack, AI-driven application designed to allow users to ask natural language questions about their PDF documents and receive accurate, context-aware answers. It solves the problem of needing to manually search through large files for specific information.

The core of the application is a **Retrieval-Augmented Generation (RAG)** pipeline, which intelligently combines document retrieval with a Large Language Model (LLM) to provide grounded and reliable responses.

## 📸 Demo

<img width="1214" height="616" alt="AI ChatBot PDF Q&A" src="https://github.com/user-attachments/assets/fc34015f-f16c-4c06-b5bb-9e1c99e69b97" />

## ✨ Features

* **Document Upload:** Securely upload one or more PDF files.
* **Intelligent Q&A:** Ask questions and receive precise answers.
* **Context-Aware Responses:** The chatbot uses information directly from your documents to prevent "hallucinations" and provide accurate information.
* **Hybrid AI Backend:** Utilizes a **Hugging Face** model for cost-effective embeddings and an **OpenAI** model for superior conversational quality.

## 💻 Technologies Used

* **Frontend:** Streamlit
* **Backend:** Python
* **LLMs:** OpenAI GPT-3.5-Turbo
* **Embeddings:** Hugging Face `sentence-transformers/all-MiniLM-L6-v2`
* **Vector Store:** FAISS
* **PDF Processing:** PyPDF2
* **Framework:** LangChain


### Prerequisites

You will need Python and `pip` installed.

1.  Clone the repository:
    `git clone [your_repo_link]`
    `cd [your_repo_name]`

2.  Set up your virtual environment:
    `python -m venv venv`
    `source venv/bin/activate`

3.  Install the required packages:
    `pip install -r requirements.txt`

4.  Set up your environment variables:
    Create a file named `.env` in the root directory and add your OpenAI API key:
    `OPENAI_API_KEY="YOUR_API_TOKEN_HERE"`

### Running the App

Run the Streamlit application from your terminal:
`streamlit run app.py`
