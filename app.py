import streamlit as st
from dotenv import load_dotenv, find_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import huggingface_hub
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def get_pdf_text(pdf_docs):
  text =""
  for pdf in pdf_docs:
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
      text += page.extract_text()
  return text

def get_text_chunks(text):
  text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
  )
  chunks = text_splitter.split_text(text)
  return chunks

def get_vector_store(text_chunks):
  # embeddings = OpenAIEmbeddings()
  embeddings = HuggingFaceEmbeddings(model_name='hkunlp/instructor-xl')
  vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
  return vector_store

def get_conversation_chain(vector_store):
  # llm = ChatOpenAI()
  llm = huggingface_hub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
  memory = ConversationBufferMemory(memory_key='chat_history', return_message=True)
  conversation_chain = ConversationalRetrievalChain.from_llm(
    llm = llm,
    retrieve=vector_store.as_retriever(),
    memory=memory
  )
  return conversation_chain
  
def handle_user_input(user_question):
  response = st.session_state.conversation({'question': user_question})
  st.write(response)

def main():
  load_dotenv(find_dotenv())
  st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
  
  st.write(css, unsafe_allow_html=True)
  
  if "conversation" not in st.session_state:
    st.session_state.conversation = None
  
  st.header("Chat with multiple PDFs")
  
  user_question = st.text_input("Ask a question about your documents:")
  if user_question:
    handle_user_input(user_question)
    
  st.write(user_template.replace("{{MSG}}", "hello bot"), unsafe_allow_html=True)
  st.write(bot_template.replace("{{MSG}}", "hello human"), unsafe_allow_html=True)
  
  with st.sidebar:
    st.subheader("Your documents")
    pdf_docs = st.file_uploader("Upload your PDFs here and click 'Process'", accept_multiple_files=True)
    
    if st.button("Process"):
      with st.spinner("Processing"):
        # get pdf text
        raw_text = get_pdf_text(pdf_docs)
        
        # get the text chunks
        text_chunks = get_text_chunks(raw_text)
        
        # create vector store with embedings
        vector_store = get_vector_store(text_chunks)   
        
        # create conversation chain
        st.session_state.conversation = get_conversation_chain(vector_store)  
        


if __name__ == '__main__':
  main()