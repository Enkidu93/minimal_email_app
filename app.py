# import streamlit as st
# import smtplib
# from email.mime.text import MIMEText
# import os, ssl


# email_receiver = st.text_input('To')
# email_cc = st.text_input('Cc')
# email_bcc = st.text_input('Bcc')
# subject = st.text_input('Subject')
# body = st.text_area('Body')

# if st.button("Send Email"):
#     try:
#         msg = MIMEText(body)
#         msg['From'] = 'serval-app@languagetechnology.org'
#         msg['To'] = email_receiver
#         msg['Cc'] = email_cc
#         msg['Bcc'] = email_bcc
#         msg['Subject'] = subject

#         context = ssl.create_default_context()
#         server = smtplib.SMTP('mail.languagetechnology.org', 587)#, context=context)
#         server.set_debuglevel(1)
#         server.starttls(context=context)
#         server.login("serval-app@languagetechnology.org",os.environ.get('SERVAL_APP_EMAIL_PASSWORD') )
#         errs = server.sendmail("serval-app@languagetechnology.org", email_receiver, msg.as_string())
#         print(errs)
#         server.quit()
#         st.success('Email sent successfully! 🚀')
#     except Exception as e:
#         st.error(f"Failed to send email: {e}")

import streamlit as st
import yagmail
import os

# Set up your email configuration
email_address = os.environ.get('APP_EMAIL') #"your_email@gmail.com"  # Replace with your email address
email_password = os.environ.get('APP_PASSWORD') #"your_password"        # Replace with your email password

st.title("Email Sender App")

recipient_email = st.text_input("Recipient Email", "")
subject = st.text_input("Subject", "")
message = st.text_area("Message", "")

if st.button("Send Email"):
    if recipient_email and subject and message:
        try:
            # Initialize yagmail SMTP client
            yag = yagmail.SMTP(email_address, email_password)

            # Send the email
            yag.send(
                to=recipient_email,
                subject=subject,
                contents=message
            )

            st.success("Email sent successfully!")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please fill in all the required fields.")

st.write("Note: Make sure you enable 'Less secure apps' for your Gmail account if you are using Gmail. "
         "Additionally, use an 'App Password' if you have two-factor authentication enabled.")

