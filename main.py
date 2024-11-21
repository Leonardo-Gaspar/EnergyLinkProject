from db.obter_dados import obter_emails, obter_nomes
from agent_scripts.agent_initializer import create_agent_executor
from agent_scripts.agent_tools import send_email

def main():
    nomes = obter_nomes()
    emails = obter_emails()

    if not nomes or not emails:
        print("Não há usuários para enviar e-mails.")
        return
    
    if len(nomes) != len(emails):
        print("Erro: o número de nomes e e-mails não coincide.")
        return

    prompt_path = "prompt/prompt_email.txt"

    agent = create_agent_executor(prompt_path)
    if agent is None:
        return

    subject = "Descubra o poder da energia limpa com a EnergyLink!"

    try:
        response = agent.run({"input": "Crie um e-mail genérico com o texto 'Olá [nome do destinatário]'."})
        body_template = response

        for nome, to_email in zip(nomes, emails):  
            body_personalizado = body_template.replace("[nome do destinatário]", nome)
            send_email(to_email, subject, body_personalizado)

        print(f"E-mails enviados para {len(nomes)} usuários.")

    except Exception as e:
        print(f"Erro durante o processo: {e}")


if __name__ == "__main__":
    main()