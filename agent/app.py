import sqlite3
from contextlib import closing

def fazer_login(usuario, senha, caminho_banco="banco_de_dados.db"):
    with closing(sqlite3.connect(caminho_banco)) as conexao:
        cursor = conexao.execute(
            """
            SELECT 1
            FROM usuarios
            WHERE username = ? AND password = ?
            LIMIT 1
            """,
            (usuario, senha),
        )
        resultado = cursor.fetchone()

    if resultado is not None:
        return "Acesso Permitido"
    return "Acesso Negado."