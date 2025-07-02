
from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp

def create_chatbot(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", k=3)
    llm = LlamaCpp(
        model_path="models/gemma-3-27b.gguf",
        temperature=0.5,
        max_tokens=1024,
        n_ctx=2048,
        verbose=False
    )
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
