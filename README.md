# EnergyLinkProject

# Projeto de Automação de E-mails Promocionais com EnergyLink

## **Descrição do Problema**
O sistema foi desenvolvido para automatizar o envio de e-mails promocionais personalizados para usuários cadastrados. O objetivo é promover os benefícios da energia limpa (solar e eólica) e incentivar o interesse por soluções sustentáveis, de maneira eficaz e escalável.

## **Link Demonstração Vídeo**
https://www.youtube.com/watch?v=YKt3zPvLo7g
---

## **Metodologia Utilizada**
1. **Banco de Dados Oracle**:
   - Coleta de nomes e e-mails dos usuários cadastrados.
   - Conexão com o banco utilizando a biblioteca `oracledb`.

2. **Criação de Agente com OpenAI**:
   - Uso do modelo GPT-4 para gerar conteúdos persuasivos para e-mails.
   - Prompt customizado para criação de mensagens promocionais com tom otimista e acessível.

3. **Envio de E-mails**:
   - Implementação do protocolo SMTP com `smtplib` para envio dos e-mails personalizados.
   - Personalização do conteúdo para cada usuário utilizando o nome extraído do banco de dados.

4. **Estrutura Modular**:
   - Separação do código em scripts organizados para fácil manutenção e escalabilidade.
   - Utilização de variáveis de ambiente para gerenciar credenciais sensíveis, como chaves de API e dados de conexão.

---

## **Resultados Obtidos**
- E-mails personalizados foram gerados e enviados para todos os usuários registrados no banco de dados com sucesso.
- O sistema é escalável e pode ser adaptado para diferentes campanhas e listas de usuários.

---

## **Conclusões**
O sistema automatiza um processo crítico de marketing com alta personalização, garantindo eficiência e melhorando a experiência do usuário final. A modularidade do código permite fácil manutenção e expansibilidade para novas funcionalidades, como análise de métricas de abertura de e-mails.

---

## **Organização do Repositório**

Abaixo está a estrutura de diretórios do repositório:

## **Instalação e Configuração**

### **Pré-requisitos**
- Python 3.9 ou superior
- Banco de dados Oracle configurado e acessível
- Conta OpenAI API configurada
- Variáveis de ambiente definidas no arquivo `.env`:
  ```env
  OPENAI_API_KEY=your_openai_api_key
  EMAIL_PASSWORD=your_email_password
  ORACLE_USER=your_oracle_user
  ORACLE_PASSWORD=your_oracle_password
  ORACLE_DSN=your_oracle_dsn

### **Clone o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/EnergyLinkProject.git
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   Streamlit run main.py

