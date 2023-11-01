import streamlit as st
import smtplib
from email.mime.text import MIMEText
import os, ssl


email_receiver = st.text_input('To')
subject = st.text_input('Subject')
body = st.text_area('Body')

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = 'serval-app@languagetechnology.org'
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg['Signed by'] = 'languagetechnology.org'

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('mail.languagetechnology.org', 465, context=context, timeout=10)
        server.set_debuglevel(1)
        server.login("serval-app@languagetechnology.org",os.environ.get('SERVAL_APP_EMAIL_PASSWORD') )
        server.sendmail("serval-app@languagetechnology.org", email_receiver, msg.as_string())
        server.quit()
        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
