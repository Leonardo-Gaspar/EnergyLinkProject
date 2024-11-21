import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body, from_email="leosaheb2003@gmail.com", smtp_server="smtp.gmail.com", smtp_port=587):
    """
    Envia um e-mail usando as configurações SMTP fornecidas.
    """
    try:
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, os.getenv("EMAIL_PASSWORD"))  
            server.send_message(message)

        print(f"E-mail enviado para {to_email}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

    

