import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


class GmailService:

    @staticmethod
    def send_email(subject: str, content: str):

        sender = os.getenv("GMAIL_ADDRESS")
        password = os.getenv("GMAIL_APP_PASSWORD")
        receiver = os.getenv("GMAIL_ADDRESS")

        message = MIMEMultipart("alternative")
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject

        message.attach(
            MIMEText(content, "html", "utf-8")
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(message)