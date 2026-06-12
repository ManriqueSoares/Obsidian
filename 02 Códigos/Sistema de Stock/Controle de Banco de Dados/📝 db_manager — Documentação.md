# db_manager.py — Documentação

← [[🗄️ Banco de Dados]]

## O que é

Utilitário interativo de linha de comando para gerenciar o banco de dados PostgreSQL do projeto. Lê as credenciais do `.env` e oferece um menu com operações separadas para tabelas, colunas e linhas.

## Pré-requisitos

Dependências já presentes no `requirements.txt`:

- `psycopg2-binary` — driver PostgreSQL
- `python-dotenv` — leitura do `.env`

## Como executar

```powershell
cd "C:\Users\manriquef\Documents\Download app teste\download-app-stock"
.\.venv\Scripts\python.exe db_manager.py
```

## Variáveis de ambiente utilizadas (`.env`)

| Variável              | Descrição              |
|-----------------------|------------------------|
| `POSTGRESQL_HOST`     | Endereço do servidor   |
| `POSTGRESQL_PORT`     | Porta de conexão       |
| `POSTGRESQL_USERNAME` | Usuário do banco       |
| `POSTGRESQL_PASSWORD` | Senha do banco         |
| `POSTGRESQL_NAME`     | Nome do banco de dados |

## Menu de opções

### 1. Listar tabelas
Exibe todas as tabelas existentes no schema `public`.

### 2. Criar tabela
Solicita o nome da tabela e as colunas que devem ser criadas. A coluna `id SERIAL PRIMARY KEY` é adicionada automaticamente. Usa `CREATE TABLE IF NOT EXISTS`, então é seguro executar mais de uma vez.

Exemplo de colunas ao criar:
```
nome VARCHAR(100)
ativo BOOLEAN
quantidade INTEGER
```

### 3. Adicionar coluna a uma tabela existente
Executa `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`. Sem risco de erro caso a coluna já exista.

Tipos comuns:
- `VARCHAR(n)`, `TEXT`
- `INTEGER`, `BIGINT`
- `BOOLEAN`
- `DATE`, `TIMESTAMP`
- `NUMERIC(p, s)`

### 4. Inserir linha
Lista as colunas da tabela automaticamente (exceto `id`) e solicita um valor para cada uma. O `id` é gerado pelo banco e exibido ao final.

### 5. Listar linhas
Exibe as linhas de uma tabela em formato tabular. O número de linhas é configurável (padrão: 20).

## Estrutura do código

```
db_manager.py
├── get_connection()   — abre conexão usando DB_CONFIG do .env
├── list_tables()      — consulta information_schema.tables
├── create_table()     — CREATE TABLE IF NOT EXISTS
├── add_column()       — ALTER TABLE ... ADD COLUMN IF NOT EXISTS
├── insert_row()       — INSERT INTO ... RETURNING id
├── show_rows()        — SELECT * FROM ... LIMIT n
└── __main__           — loop do menu interativo
```

## Segurança

Nomes de tabelas e colunas são passados via `psycopg2.sql.Identifier`, que escapa os identificadores corretamente e evita SQL injection. Valores de linhas são passados como parâmetros (`%s`), nunca interpolados na string SQL.
