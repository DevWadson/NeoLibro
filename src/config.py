"""Configurações de acesso ao banco de dados do NeoLibro.

Fornece funções puras para construção das URLs de conexão
a partir das variáveis de ambiente.
"""
import os
from typing import Optional

def get_mysql_url() -> Optional[str]:
    """Constrói e retorna a URL de conexão com o MySQL.

    Lê as variáveis de ambiente necessárias e monta a URL
    de conexão. Retorna None se alguma variável estiver ausente.
    """
    user = os.getenv("USER")
    password = os.getenv("PWRD")
    host = os.getenv("HOST")
    db_name = os.getenv("DB_NAME")

    fields = [user, password, host, db_name]

    if not all(fields):
        return

    mysql_url: str = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return mysql_url

def get_sqlite_url() -> Optional[str]:...

def get_active_db_url() -> Optional[str]:
    """Retorna a URL do banco de dados ativo conforme configuração.

    Lê a variável ACTIVE_DB e delega a construção da URL
    para a função correspondente ao banco configurado.
    """
    active_db = os.getenv("ACTIVE_DB")

    if active_db == "mysql":
        return get_mysql_url()
