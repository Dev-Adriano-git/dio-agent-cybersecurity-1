
import sqlite3


def criar_banco():
    conexao = sqlite3.connect(":memory:")

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        ("adriano", "senha123")
    )

    conexao.commit()

    return conexao


def autenticar(conexao, usuario, senha):
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT 1 FROM usuarios
        WHERE usuario = ? AND senha = ?
        """,
        (usuario, senha)
    )

    return cursor.fetchone() is not None

if __name__ == "__main__":

    conexao = criar_banco()

    # Teste 1: Login correto
    print("Teste 1:", autenticar(conexao, "adriano", "senha123"))

    # Teste 2: Senha incorreta
    print("Teste 2:", autenticar(conexao, "adriano", "errada"))

    # Teste 3: SQL Injection no usuário
    print("Teste 3:", autenticar(conexao, "' OR '1'='1", "qualquer"))

    # Teste 4: SQL Injection na senha
    print("Teste 4:", autenticar(conexao, "adriano", "' OR '1'='1"))

    conexao.close()
