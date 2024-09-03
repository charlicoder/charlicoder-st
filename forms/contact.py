import re
import requests
import streamlit as st

WEBHOOK_URL = st.secrets['WEBHOOK_URL']


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "Email service not setup. Please try again later", icon=":email:"
                )
                st.stop()
            
            if not name:
                st.error("Please provide your name.", icon=":user:")
                st.stop()
            
            if not email:
                st.error("Please provide your email.", icon=":email:")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email.", icon=":email:")
                st.stop()
            
            if not message:
                st.error("Please provide message.", icon=":email:")
                st.stop()

            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message have beeen sent successfully!")
            else:
                st.error("There was an error in sending your message!")