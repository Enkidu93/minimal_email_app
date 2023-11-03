import streamlit as st
import smtplib
from email.mime.text import MIMEText
import os, ssl


email_receiver = st.text_input('To')
email_cc = st.text_input('Cc')
email_bcc = st.text_input('Bcc')
subject = st.text_input('Subject')
body = st.text_area('Body')

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = 'serval-app@languagetechnology.org'
        msg['To'] = email_receiver
        msg['Cc'] = email_cc
        msg['Bcc'] = email_bcc
        msg['Subject'] = subject

        context = ssl.create_default_context()
        server = smtplib.SMTP('mail.languagetechnology.org', 587)#, context=context)
        server.set_debuglevel(1)
        server.starttls(context=context)
        server.login("serval-app@languagetechnology.org",os.environ.get('SERVAL_APP_EMAIL_PASSWORD') )
        errs = server.sendmail("serval-app@languagetechnology.org", email_receiver, msg.as_string())
        print(errs)
        server.quit()
        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
