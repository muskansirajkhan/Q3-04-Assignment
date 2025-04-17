import re

import streamlit as st
import requests  # pip install requests


WEBHOOK_URL = "https://hook.pabbly.com/api/webhook/67c35fae5da3b2b509aa2881/67c364212f8d685c80ec6148"


def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Email service is not set up. Please try again later.", icon="📧")
            st.stop()

        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}
        
        try:
            # Add headers to specify JSON content
            headers = {
                'Content-Type': 'application/json'
            }
            
            # Make the request with timeout
            response = requests.post(WEBHOOK_URL, json=data, headers=headers, timeout=10)
            
            # Debug information
            st.write(f"Response Status Code: {response.status_code}")
            st.write(f"Response Text: {response.text}")
            
            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon="🚀")
            else:
                st.error(f"Error sending message. Status code: {response.status_code}", icon="😨")
                
        except requests.exceptions.Timeout:
            st.error("Request timed out. Please try again.", icon="⏰")
        except requests.exceptions.RequestException as e:
            st.error(f"Error sending message: {str(e)}", icon="😨")