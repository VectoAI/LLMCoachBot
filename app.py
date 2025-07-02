
import streamlit as st
from doc_loader import load_docx_text
from vector_store import build_vector_store
from chatbot import create_chatbot
from reservation import reservation_form

st.title("🤖 کوچ‌بات | چت‌بات مشاوره‌ای")

uploaded_file = st.file_uploader("📄 فایل ورد خدمات مشاوره را آپلود کنید", type="docx")

if uploaded_file:
    text = load_docx_text(uploaded_file)
    with st.spinner("در حال پردازش فایل..."):
        vectorstore = build_vector_store(text)
        chatbot = create_chatbot(vectorstore)
    st.success("✅ چت‌بات آماده پاسخگویی است")

    query = st.text_input("❓ سوال خود را وارد کنید")
    if query:
        response = chatbot.run(query)
        st.write("🧠 پاسخ:", response)

    st.markdown("---")
    reservation_form()
