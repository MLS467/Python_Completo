from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from string import Template
import dotenv
import pathlib

# carrega variáveis de ambiente
dotenv.load_dotenv()

# Caminho do arquivo html
CAMINHO_HTML = pathlib.Path(__file__).parent / "email.html"


# dados do remetente
nome = "Maissão"
assunto = "Assunto do email"
email = os.getenv("FROM_EMAIL", "")
senha = os.getenv("APP_PASSWORD", "")

# configuraçães SMTP
smtp_gmail = os.getenv("SMTP_GOOGLE")
smtp_porta = 587
smtp_username = os.getenv("FROM_EMAIL", "")
smtp_password = senha

# mensagem de texto
with open(CAMINHO_HTML, "r") as arquivo:
    texto = arquivo.read()
    template = Template(texto)
    texto_email = template.substitute(nome=nome)

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart["from"] = email
mime_multipart["to"] = smtp_username
mime_multipart["subject"] = assunto

corpo_email = MIMEText(texto_email, "html", "utf-8")
mime_multipart.attach(corpo_email)


# Envia o e-mail
with smtplib.SMTP(smtp_gmail, smtp_porta) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("E-mail enviado com  sucesso!")
