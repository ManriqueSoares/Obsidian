# db_manager.py — Código

← [[🗄️ Banco de Dados]]

Arquivo original: `download-app-stock/db_manager.py`

---

```python
"""
db_manager.py — Utilitário interativo para gerenciar o banco PostgreSQL.

Etapas disponíveis:
  1. Listar tabelas existentes
  2. Criar uma nova tabela
  3. Adicionar coluna a uma tabela existente
  4. Inserir uma linha em uma tabela
  5. Listar linhas de uma tabela
  6. Sair

Uso:
  python db_manager.py
"""

import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("POSTGRESQL_HOST"),
    "port": os.getenv("POSTGRESQL_PORT"),
    "user": os.getenv("POSTGRESQL_USERNAME"),
    "password": os.getenv("POSTGRESQL_PASSWORD"),
    "dbname": os.getenv("POSTGRESQL_NAME"),
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


# ─── Etapa 1: Listar tabelas ────────────────────────────────────────────────

def list_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = [row[0] for row in cur.fetchall()]

    if tables:
        print("\nTabelas encontradas:")
        for t in tables:
            print(f"  - {t}")
    else:
        print("\nNenhuma tabela encontrada no schema public.")
    return tables


# ─── Etapa 2: Criar tabela ──────────────────────────────────────────────────

def create_table():
    table_name = input("\nNome da nova tabela: ").strip()
    if not table_name:
        print("Nome inválido.")
        return

    columns = []
    columns.append("id SERIAL PRIMARY KEY")

    print("Adicione as colunas (deixe em branco para finalizar).")
    print("Formato: nome_coluna TIPO  (ex: nome VARCHAR(100), ativo BOOLEAN)")
    while True:
        col = input("  Coluna: ").strip()
        if not col:
            break
        columns.append(col)

    col_definitions = ", ".join(columns)
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({col_definitions});"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()

    print(f"\nTabela '{table_name}' criada com sucesso.")
    print(f"  SQL executado: {query}")


# ─── Etapa 3: Adicionar coluna ──────────────────────────────────────────────

def add_column():
    tables = list_tables()
    if not tables:
        return

    table_name = input("\nNome da tabela para adicionar a coluna: ").strip()
    col_name = input("Nome da nova coluna: ").strip()
    col_type = input("Tipo da coluna (ex: VARCHAR(200), INTEGER, BOOLEAN, TEXT): ").strip()

    if not all([table_name, col_name, col_type]):
        print("Dados incompletos.")
        return

    query = sql.SQL("ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {col} {type};").format(
        table=sql.Identifier(table_name),
        col=sql.Identifier(col_name),
        type=sql.SQL(col_type),
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()

    print(f"\nColuna '{col_name} {col_type}' adicionada à tabela '{table_name}'.")


# ─── Etapa 4: Inserir linha ─────────────────────────────────────────────────

def insert_row():
    tables = list_tables()
    if not tables:
        return

    table_name = input("\nNome da tabela para inserir dados: ").strip()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = %s
                  AND column_name != 'id'
                ORDER BY ordinal_position;
            """, (table_name,))
            cols = cur.fetchall()

    if not cols:
        print(f"Tabela '{table_name}' não encontrada ou sem colunas além de 'id'.")
        return

    print(f"\nInforme os valores para cada coluna da tabela '{table_name}':")
    values = {}
    for col_name, data_type in cols:
        val = input(f"  {col_name} ({data_type}): ").strip()
        values[col_name] = val if val else None

    col_identifiers = sql.SQL(", ").join(map(sql.Identifier, values.keys()))
    placeholders = sql.SQL(", ").join(sql.Placeholder() * len(values))
    query = sql.SQL("INSERT INTO {table} ({cols}) VALUES ({vals}) RETURNING id;").format(
        table=sql.Identifier(table_name),
        cols=col_identifiers,
        vals=placeholders,
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, list(values.values()))
            new_id = cur.fetchone()[0]
        conn.commit()

    print(f"\nLinha inserida com sucesso! ID gerado: {new_id}")


# ─── Etapa 5: Listar linhas ─────────────────────────────────────────────────

def show_rows():
    tables = list_tables()
    if not tables:
        return

    table_name = input("\nNome da tabela para listar linhas: ").strip()
    limit = input("Quantas linhas exibir? (padrão: 20): ").strip()
    limit = int(limit) if limit.isdigit() else 20

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql.SQL("SELECT * FROM {table} LIMIT %s;").format(
                    table=sql.Identifier(table_name)
                ),
                (limit,),
            )
            rows = cur.fetchall()
            col_names = [desc[0] for desc in cur.description]

    if not rows:
        print(f"\nA tabela '{table_name}' está vazia.")
        return

    col_widths = [max(len(c), max((len(str(r[i])) for r in rows), default=0)) for i, c in enumerate(col_names)]
    sep = "  ".join("-" * w for w in col_widths)
    header = "  ".join(c.ljust(col_widths[i]) for i, c in enumerate(col_names))

    print(f"\n{header}")
    print(sep)
    for row in rows:
        print("  ".join(str(v).ljust(col_widths[i]) for i, v in enumerate(row)))
    print(f"\n{len(rows)} linha(s) exibidas.")


# ─── Menu principal ──────────────────────────────────────────────────────────

MENU = """
╔══════════════════════════════════════╗
║       Gerenciador PostgreSQL         ║
╠══════════════════════════════════════╣
║  1. Listar tabelas                   ║
║  2. Criar tabela                     ║
║  3. Adicionar coluna a tabela        ║
║  4. Inserir linha                    ║
║  5. Listar linhas de uma tabela      ║
║  6. Sair                             ║
╚══════════════════════════════════════╝
"""

ACTIONS = {
    "1": list_tables,
    "2": create_table,
    "3": add_column,
    "4": insert_row,
    "5": show_rows,
}

if __name__ == "__main__":
    print(f"\nConectando a: {DB_CONFIG['host']}:{DB_CONFIG['port']} / {DB_CONFIG['dbname']}")
    try:
        with get_connection() as conn:
            print("Conexão OK.\n")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        raise SystemExit(1)

    while True:
        print(MENU)
        choice = input("Escolha uma opção: ").strip()

        if choice == "6":
            print("Saindo.")
            break
        elif choice in ACTIONS:
            try:
                ACTIONS[choice]()
            except Exception as e:
                print(f"\nErro: {e}")
        else:
            print("Opção inválida.")
```
