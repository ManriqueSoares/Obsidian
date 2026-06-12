# Testes — Sistema Stock

← [[⭐ Sistema Stock]]

Suíte de testes automatizados do projeto. Usa **pytest 8.3** com mocks de banco de dados — nenhum teste acessa o PostgreSQL real.

---

## Estrutura

```
download-app-stock/
└── tests/
    ├── conftest.py              ← adiciona a raiz do projeto ao sys.path
    ├── api/
    │   ├── test_health.py
    │   └── test_items.py
    └── unit/
        ├── conftest.py          ← adiciona app/ui ao sys.path
        ├── test_config.py
        ├── test_add_chefia.py
        └── test_cadastrar_centro.py
```

---

## Arquivos

[[📄 test_cadastrar_centro — Documentação]]
Testes unitários do serviço `cadastrar_centro.py` — cobre inserção de responsável, chefias, pilares e tratamento de erros.

---

## Como rodar

**Todos os testes:**
```powershell
cd "C:\Users\manriquef\Documents\Download app teste\download-app-stock"
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

**Só os testes de unit:**
```powershell
.\.venv\Scripts\python.exe -m pytest tests/unit/ -v
```

**Um arquivo específico:**
```powershell
.\.venv\Scripts\python.exe -m pytest tests/unit/test_cadastrar_centro.py -v
```

---

## Configuração dos `conftest.py`

### `tests/conftest.py`
Adiciona a raiz do projeto ao `sys.path` para que `app.*` seja importável nos testes de API.

### `tests/unit/conftest.py`
Adiciona `app/ui` ao `sys.path`. Necessário porque os serviços da UI usam imports bare (`from database.conn_db import ...`, `from config.listas import ...`) que assumem `app/ui` como raiz. Sem isso, os imports falhariam ao rodar pytest da raiz do projeto.

---

## Padrão de mock do banco

Nenhum teste conecta ao banco real. O `get_connection` é substituído por um `MagicMock` que simula o context manager do `psycopg2`:

```python
conn = MagicMock()
conn.__enter__ = MagicMock(return_value=conn)
conn.__exit__ = MagicMock(return_value=False)
cur = MagicMock()
conn.cursor.return_value.__enter__ = MagicMock(return_value=cur)
conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

with patch("services.cadastrar_centro.get_connection", return_value=conn):
    add_centro()
```
