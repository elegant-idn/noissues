import smtplib
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import status

def send_email(data, user, type):
    email = EmailMessage(
        data["email_subject"],
        render_to_string(data["email_file"], data["email_data"]),
        from_email="Emotell",
        to=[user.email]
    )
    email.content_subtype = "html"
    try:
        email.send()
    except (smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError) as error:
        return status.HTTP_204_NO_CONTENT
    # return status.HTTP_201_CREATED