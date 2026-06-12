# test_cadastrar_centro.py — Documentação

← [[🧪 Testes]]

## O que é

Testes unitários do serviço `app/ui/services/cadastrar_centro.py`, que persiste no banco os dados da tela de **Cadastro Centro**: responsável, chefias e pilares.

## Arquivo testado

```
app/ui/services/cadastrar_centro.py
└── add_centro(on_error=None)
```

## Pré-requisitos

Nenhuma conexão real com banco — tudo mockado. Dependências já no `.venv`:
- `pytest`
- `pandas`
- `psycopg2-binary`

## Como rodar

```powershell
cd "C:\Users\manriquef\Documents\Download app teste\download-app-stock"
.\.venv\Scripts\python.exe -m pytest tests/unit/test_cadastrar_centro.py -v
```

## Testes e o que verificam

| Teste | O que verifica |
|-------|----------------|
| `test_add_centro_insere_responsavel` | SQL contém o nome do responsável e tipo `RESPONSAVEL` |
| `test_add_centro_responsavel_email_weg` | Email do responsável é `{usuario}@weg.net` |
| `test_add_centro_responsavel_centro_correto` | Centro informado é enviado corretamente ao banco |
| `test_add_centro_insere_chefias` | SQL contém todos os nomes das chefias |
| `test_add_centro_chefias_email_weg` | Email de cada chefia é `{usuario}@weg.net` |
| `test_add_centro_sem_chefias_nao_falha` | Com lista de chefias vazia, só 1 `execute` (o do responsável) |
| `test_add_centro_insere_pilares` | SQL contém todos os responsáveis de pilares do DataFrame |
| `test_add_centro_pilares_area_correta` | Cada pilar é gravado com a área correta (`ÁREA` do DataFrame) |
| `test_add_centro_total_execucoes` | 1 resp + N chefias + M pilares = total de `execute` calls |
| `test_add_centro_commit_tres_vezes` | `conn.commit()` é chamado exatamente 3 vezes (após resp, chefias e pilares) |
| `test_add_centro_erro_chama_on_error` | `psycopg2.Error` aciona o callback `on_error` com a mensagem de erro |
| `test_add_centro_erro_sem_on_error_nao_propaga` | Erro de banco sem callback não lança exceção |
| `test_add_centro_on_error_nao_chamado_em_sucesso` | `on_error` não é chamado quando tudo ocorre sem erro |

## Estrutura de dados esperada pelo serviço

`listas_cadastro` (singleton de `config/listas.py`) deve estar preenchida antes de chamar `add_centro()`:

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `resp_centro` | `str` | Login do responsável (sem `@weg.net`) |
| `centro` | `str` | Código do centro (ex: `CC001`) |
| `chefias` | `list[str]` | Logins das chefias |
| `datatable_pilares` | `pd.DataFrame` | Colunas: `RESPONSÁVEL`, `CENTRO`, `ÁREA` |

## Fluxo de commits no banco

```
1. INSERT responsável  →  conn.commit()
2. INSERT chefias (loop)  →  conn.commit()
3. INSERT pilares (loop)  →  conn.commit()
```

## Observação sobre imports

Os testes importam via caminho relativo (`from config.listas import listas_cadastro`) em vez de `from app.ui.config.listas import ...` para evitar **double import**: se os dois caminhos fossem usados ao mesmo tempo, Python criaria duas instâncias separadas de `listas_cadastro` e as alterações feitas no teste não seriam vistas pelo serviço.
