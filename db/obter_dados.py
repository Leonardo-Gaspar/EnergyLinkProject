import oracledb
from db.db_connection import conectar_oracle

import oracledb
from db.db_connection import conectar_oracle

def obter_nomes():
    """
    Obtém os nomes dos usuários cadastrados na tabela Usuario_EnergyLink.
    """
    try:
        connection = conectar_oracle()  
        if connection is None:
            return []
        
        cursor = connection.cursor()
        query = "SELECT nome_usuario FROM Usuario_EnergyLink"
        cursor.execute(query)

        nomes = cursor.fetchall()
        
        if nomes:
            return [nome[0] for nome in nomes]  
        else:
            print("Nenhum nome encontrado.")
            return []

    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao acessar o banco de dados: {erro.message}")
        return []
    finally:
        if connection:
            connection.close()

def obter_emails():
    """
    Obtém os e-mails dos usuários cadastrados na tabela Usuario_EnergyLink.
    """
    try:
        connection = conectar_oracle()  
        if connection is None:
            return []

        cursor = connection.cursor()
        query = "SELECT email_usuario FROM Usuario_EnergyLink"
        cursor.execute(query)

        emails = cursor.fetchall()

        if emails:
            return [email[0] for email in emails]  
        else:
            print("Nenhum e-mail encontrado.")
            return []

    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao acessar o banco de dados: {erro.message}")
        return []
    finally:
        if connection:
            connection.close()