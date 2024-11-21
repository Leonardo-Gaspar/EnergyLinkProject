import oracledb
import os
from dotenv import load_dotenv

def conectar_oracle():
    load_dotenv()
    try:
        user = os.getenv('ORACLE_USER')     
        password = os.getenv('ORACLE_PASSWORD')  
        dsn = os.getenv('ORACLE_DSN')        
        connection = oracledb.connect(user=user, password=password, dsn=dsn) 
        return connection
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar ao banco de dados Oracle: {erro.message}")
        return None