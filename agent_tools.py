import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_prompt(file_path):
    """
    Carrega o conteúdo do arquivo de prompt.
    """
    try:
        with open(file_path, 'r') as file:
            return " ".join(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Erro: Arquivo de prompt não encontrado em {file_path}")
        return ""

def send_email(to_email, subject, body, from_email="leosaheb2003@gmail.com", smtp_server="smtp.gmail.com", smtp_port=587):
    """
    Envia um e-mail usando as configurações SMTP fornecidas.
    """
    try:
        # Configure a mensagem de e-mail
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

        # Adicione o corpo do e-mail
        message.attach(MIMEText(body, "plain"))

        # Conecte ao servidor SMTP e envie o e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, os.getenv("EMAIL_PASSWORD"))  # Certifique-se de configurar o EMAIL_PASSWORD no .env
            server.send_message(message)

        print(f"E-mail enviado para {to_email}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def create_agent_executor(prompt_path, temperature=0.5):
    """
    Cria um agente que utiliza a OpenAI para gerar o corpo do e-mail.
    """
    try:
        load_dotenv()

        # Carrega o prompt do arquivo
        system_prompt = load_prompt(prompt_path)
        if not system_prompt:
            return None

        # Configuração do modelo GPT
        chat = ChatOpenAI(
            model="gpt-4", 
            temperature=temperature, 
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

        # Configura o prompt para o agente sem o chat_history
        prompt = ChatPromptTemplate.from_messages([
            ('system', system_prompt),
            ('user', '{input}')
        ])

        # Retorna o LLMChain configurado
        agent_chain = LLMChain(llm=chat, prompt=prompt)
        return agent_chain

    except Exception as e:
        print(f"Erro ao criar executor agent: {str(e)}")
        return None

def main():
    # Caminho do arquivo de prompt
    prompt_path = "prompt/prompt_email.txt"
    
    # Criação do agente
    agent = create_agent_executor(prompt_path)
    if agent is None:
        return
    
    # Dados do e-mail
    # to_email = "jumarianobf@gmail.com"
    # to_email = "ikesaheb03@gmail.com"
    # to_email = "dricagaspar@hotmail.com"
    to_email = "caio3martins@gmail.com"
    
    subject = "Assunto do E-mail"

    try:
        # Gera o corpo do e-mail automaticamente usando o agente
        response = agent.run({"input": "Crie um e-mail completo com base no contexto fornecido no prompt."})
        body = response

        # Envia o e-mail
        send_email(to_email, subject, body)
    except Exception as e:
        print(f"Erro durante o processo: {e}")

if __name__ == "__main__":
    main()
    

