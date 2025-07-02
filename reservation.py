
import streamlit as st
import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

KAVENEGAR_API_KEY = os.getenv("KAVENEGAR_API_KEY")
RESERVATION_FILE = "data/reservation_data.json"

def reservation_form():
    st.header("📅 فرم رزرو وقت مشاوره")

    name = st.text_input("نام و نام خانوادگی")
    phone = st.text_input("شماره تماس")
    time = st.time_input("زمان مورد نظر")
    topic = st.text_input("موضوع مشاوره")

    if st.button("ثبت رزرو"):
        data = {"name": name, "phone": phone, "time": str(time), "topic": topic}
        save_reservation(data)
        send_sms_confirmation(phone, name, time)
        st.success("✅ رزرو شما با موفقیت ثبت شد و پیامک ارسال گردید.")

def save_reservation(entry):
    if os.path.exists(RESERVATION_FILE):
        with open(RESERVATION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    with open(RESERVATION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def send_sms_confirmation(phone, name, time):
    if not KAVENEGAR_API_KEY:
        return
    url = f"https://api.kavenegar.com/v1/{KAVENEGAR_API_KEY}/sms/send.json"
    payload = {
        "receptor": phone,
        "message": f"{name} عزیز، رزرو مشاوره شما برای ساعت {time} ثبت شد. از همراهی شما سپاسگزاریم. - کوچ‌بات"
    }
    requests.post(url, data=payload)
