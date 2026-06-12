# Trigger — Popular lista_pilares

← [[🗄️ Banco de Dados]]

## O que faz

Toda vez que uma linha é inserida em `estoque_geral`, o trigger verifica se `valor_total$` é maior ou igual a **R$ 50,00**. Se sim, copia automaticamente a linha para a tabela `lista_pilares` com o campo `status` definido como `"pendente"`.

## Regra

```
estoque_geral  →  INSERT  →  valor_total$ >= 50.00  →  copia para lista_pilares (status = 'pendente')
```

## Como aplicar no banco

Rodar o arquivo `trigger_lista_pilares.sql` diretamente no PostgreSQL:

```powershell
cd "C:\Users\manriquef\Documents\Download app teste\download-app-stock"
.\.venv\Scripts\python.exe -c "
import psycopg2, os
from dotenv import load_dotenv
load_dotenv()
conn = psycopg2.connect(
    host=os.getenv('POSTGRESQL_HOST'),
    port=os.getenv('POSTGRESQL_PORT'),
    user=os.getenv('POSTGRESQL_USERNAME'),
    password=os.getenv('POSTGRESQL_PASSWORD'),
    dbname=os.getenv('POSTGRESQL_NAME'),
)
cur = conn.cursor()
cur.execute(open('trigger_lista_pilares.sql').read())
conn.commit()
print('Trigger criado com sucesso.')
conn.close()
"
```

## Código SQL

```sql
-- 1. Função executada pelo trigger
CREATE OR REPLACE FUNCTION fn_importar_para_lista_pilares()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW."valor_total$" >= 50.00 THEN
        INSERT INTO lista_pilares (
            cp,
            cliente,
            centro,
            responsavel,
            data_cadastro,
            "valor_total$",
            status
        )
        VALUES (
            NEW.cp,
            NEW.cliente,
            NEW.centro,
            NEW.responsavel,
            NEW.data_cadastro,
            NEW."valor_total$",
            'pendente'
        );
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- 2. Trigger que chama a função após cada INSERT em estoque_geral
DROP TRIGGER IF EXISTS trigger_lista_pilares ON estoque_geral;

CREATE TRIGGER trigger_lista_pilares
AFTER INSERT ON estoque_geral
FOR EACH ROW
EXECUTE FUNCTION fn_importar_para_lista_pilares();
```

## Observações

- O `DROP TRIGGER IF EXISTS` no início garante que rodar o script mais de uma vez não cause erro.
- O nome da coluna `valor_total$` precisa de aspas duplas no SQL por conter o caractere `$`.
- A tabela `lista_pilares` precisa existir antes de aplicar o trigger. Crie ela pelo `db_manager.py` (opção 2) com as colunas necessárias mais a coluna `status VARCHAR(50)`.
