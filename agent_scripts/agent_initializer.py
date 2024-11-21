import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from prompt.carregar_prompt import load_prompt

def create_agent_executor(prompt_path, temperature=0.5):
    """
    Cria um agente que utiliza a OpenAI para gerar o corpo do e-mail.
    """
    try:
        load_dotenv()

        system_prompt = load_prompt(prompt_path)
        if not system_prompt:
            return None

        chat = ChatOpenAI(
            model="gpt-4", 
            temperature=temperature, 
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

        prompt = ChatPromptTemplate.from_messages([
            ('system', system_prompt),
            ('user', '{input}')
        ])

        agent_chain = LLMChain(llm=chat, prompt=prompt)
        return agent_chain

    except Exception as e:
        print(f"Erro ao criar executor agent: {str(e)}")
        return None
