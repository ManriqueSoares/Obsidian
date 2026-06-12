# Atualizações — Sistema de Stock | 06/05/2026

> **Branch:** `TESTE_NOVA_INTERFACE`
> **Status:** ⚠️ Nada migrado para `master` ainda. Todas as mudanças estão apenas nessa branch.

---

## 1. Banco de Dados — `db_manager.py`

> Notas relacionadas: [[🗄️ Banco de Dados]] · [[📄 db_manager — Código]] · [[📝 db_manager — Documentação]] · [[✅ Tarefas do Banco]] · [[⚡ Trigger - lista_pilares]]

O utilitário interativo de gerenciamento do PostgreSQL foi expandido. Antes só era possível criar, consultar e atualizar dados. Agora o menu conta com **três novas operações de exclusão**:

| Opção | Função |
|-------|--------|
| 7 | Deletar **uma** linha (filtra por qualquer coluna) |
| 8 | Deletar **várias** linhas de uma vez (lista de valores separados por vírgula) |
| 9 | `TRUNCATE` — limpa a tabela inteira e reinicia o identity |

### Menu completo atual

```
╔══════════════════════════════════════╗
║       Gerenciador PostgreSQL         ║
╠══════════════════════════════════════╣
║  1. Listar tabelas                   ║
║  2. Criar tabela                     ║
║  3. Adicionar coluna a tabela        ║
║  4. Inserir linha                    ║
║  5. Listar linhas de uma tabela      ║
║  6. Atualizar linha existente        ║
║  7. Deletar uma linha                ║
║  8. Deletar várias linhas            ║
║  9. Limpar tabela inteira (TRUNCATE) ║
║  0. Sair                             ║
╚══════════════════════════════════════╝
```

### Código — Deletar uma linha (`delete_row`)

```python
def delete_row():
    tables = list_tables()
    if not tables:
        return

    table_name = input("\nNome da tabela: ").strip()
    coluna = input("Nome da coluna para filtrar (ex: id, cp): ").strip()
    valor = input(f"Valor de '{coluna}': ").strip()

    confirma = input(f"\nDeletar linha onde {coluna} = '{valor}' em '{table_name}'? (s/N): ").strip().lower()
    if confirma != "s":
        print("Operação cancelada.")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f'DELETE FROM {table_name} WHERE "{coluna}" = %s', (valor,))
            afetadas = cur.rowcount
        conn.commit()

    if afetadas:
        print(f"\n{afetadas} linha(s) deletada(s).")
    else:
        print(f"\nNenhuma linha encontrada com {coluna} = '{valor}'.")
```

### Código — Deletar várias linhas (`delete_rows`)

```python
def delete_rows():
    tables = list_tables()
    if not tables:
        return

    table_name = input("\nNome da tabela: ").strip()
    coluna = input("Nome da coluna para filtrar (ex: id, cp): ").strip()
    raw = input(f"Valores de '{coluna}' separados por vírgula: ").strip()
    valores = [v.strip() for v in raw.split(",") if v.strip()]

    if not valores:
        print("Nenhum valor informado.")
        return

    confirma = input(f"\nDeletar {len(valores)} linha(s) em '{table_name}'? (s/N): ").strip().lower()
    if confirma != "s":
        print("Operação cancelada.")
        return

    placeholders = ",".join(["%s"] * len(valores))
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f'DELETE FROM {table_name} WHERE "{coluna}" IN ({placeholders})', valores)
            afetadas = cur.rowcount
        conn.commit()

    print(f"\n{afetadas} linha(s) deletada(s).")
```

### Código — TRUNCATE (`truncate_table`)

```python
def truncate_table():
    tables = list_tables()
    if not tables:
        return

    table_name = input("\nNome da tabela a limpar: ").strip()
    confirma = input(f"\nATENÇÃO: isso apaga TODOS os dados de '{table_name}'. Continuar? (s/N): ").strip().lower()
    if confirma != "s":
        print("Operação cancelada.")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE")
        conn.commit()

    print(f"\nTabela '{table_name}' limpa com sucesso.")
```

---

## 2. Dashboard — Para Apresentação

Foram criados dois arquivos para geração e visualização de dashboards do banco de dados:

- **`generate_dashboard.js`** — script Node.js que conecta ao PostgreSQL e gera o HTML automaticamente
- **`dashboard.html`** — dashboard gerado, pronto para abrir no navegador

### Como rodar

```bash
npm install       # instala pg e dotenv (apenas na primeira vez)
node generate_dashboard.js
# Abre o dashboard.html gerado no navegador
```

### O que o dashboard mostra

**Aba Usuários**
- KPIs: total de usuários e colunas da tabela
- Tabela completa com todos os registros de `users`
- Campo de busca em tempo real filtrando qualquer coluna

**Aba Estoque Geral**
- KPI: total de itens e quantidade de indicadores gerados
- Geração automática de gráficos conforme o tipo de cada coluna:
  - Colunas de **data** → gráfico de linha (série temporal)
  - Colunas **numéricas** → histograma de distribuição + pizza/barra por categoria de texto
  - Colunas de **texto** → frequência de valores (quando não há numérico associado)

### Snapshot dos dados atuais (06/05/2026)

| Indicador | Valor |
|-----------|-------|
| Usuários cadastrados | 8 |
| Itens em estoque | 4 |
| Gráficos gerados | 9 |

---

## 3. Interface — Melhorias (`TESTE_NOVA_INTERFACE`)

### 3.1 Nova página: Cadastro Centro

Criada a página `CadastroCentro` (`app/ui/layout/pages/cadastro_centro.py`) com:

- Campo **Responsável** (`@weg.net` automático)
- Campo **Centro** (máx. 4 dígitos)
- Campo **Chefia** com botão de adicionar e **remoção individual** de chefias
- **DataTable de Pilares** com 7 áreas pré-configuradas (Parte Ativa, Bobinagem, Cálculo, Fiação, Mecânica, Aprovação, Geral)
- O campo Centro atualiza automaticamente todos os registros da tabela ao ser alterado (`on_change`)
- Botão de Download/Confirmar envia os dados ao banco via `add_centro()`

### 3.2 Home Page integrada com Cadastro

`home_page.py` agora possui o botão **"Cadastro Centro"** conectado: ao clicar, navega para `CadastroCentro` sem recarregar a aplicação.

```python
def open_page_cadastro_page(self, e):
    from layout.raiz import raiz
    from layout.pages.cadastro_centro import CadastroCentro
    raiz.controls.clear()
    raiz.controls.append(CadastroCentro())
    raiz.update()
```

### 3.3 Novo serviço: `cadastrar_centro.py`

Serviço que persiste no banco todos os dados da tela de cadastro de uma só vez:
1. Insere o responsável do centro (tipo `RESPONSAVEL`)
2. Insere cada chefia adicionada (tipo `CHEFE`)
3. Insere cada responsável de pilar do DataTable (tipo `PILAR`)

### 3.4 Novo utilitário: `MensagemBox` (`utils/mensagem_alerta.py`)

Componente de alerta/modal reutilizável com:
- Título e mensagem configuráveis
- Botão de fechar com hover de destaque vermelho
- Remove-se do `raiz` ao fechar (sem recarregar página)

### 3.5 `add_chefia.py` — remoção de chefia

O serviço de adição de chefia agora suporta **remover** uma chefia já adicionada clicando no ícone `X` ao lado do nome. Remove o item tanto da UI quanto da lista `listas_cadastro.chefias`.

### 3.6 Novo arquivo: `runtime.py`

Configuração de ambiente de execução:

```python
IS_STANDALONE = False
DOWNLOAD_SERVER_PORT = 18001
```

Controla se a aplicação está rodando standalone (com servidor local de download) ou em modo produção (FastAPI + uvicorn).

### 3.7 Widgets novos em `widgets.py`

Adicionados ao `create_widgets()`:
- `BOTAO_ENTRAR_CADASTRO_CONTAINER` — botão "Cadastro Centro" na home
- `LOGO_WEG`, `TITULO_JANELA_PRINCIPAL`, `BOTAO_RETORNAR`
- `ENTRADA_RESP`, `ENTRADA_CENTRO`, `ENTRADA_CHEFIA`, `BOTAO_ADD_CHEFIA`
- `TEXTO_PILARES`, `DATATABLE_PILARES` (com 7 linhas de pilares)
- `BOTAO_DOWNLOAD`

---

## 4. Novo banco: `app/ui/database/`

Diretório criado para centralizar a conexão com o banco dentro da camada de UI (`conn_db.py` com `get_connection()`), separando da configuração do `db_manager.py`.

---

## Status dos arquivos

| Arquivo | Status |
|---------|--------|
| `db_manager.py` | Modificado |
| `app/ui/flet_app.py` | Modificado |
| `app/ui/config/listas.py` | Modificado |
| `app/ui/layout/components/widgets.py` | Modificado |
| `app/ui/layout/pages/cadastro_centro.py` | Modificado |
| `app/ui/layout/pages/home_page.py` | Modificado |
| `app/ui/services/add_chefia.py` | Modificado |
| `app/ui/config/runtime.py` | Novo |
| `app/ui/database/` | Novo |
| `app/ui/layout/pages/alerta_mensagem.py` | Novo |
| `app/ui/services/cadastrar_centro.py` | Novo |
| `app/ui/utils/mensagem_alerta.py` | Novo |
| `dashboard.html` | Novo (gerado) |
| `generate_dashboard.js` | Novo |
| `package.json` / `package-lock.json` | Novo |

---

> ⚠️ **Nenhuma dessas alterações foi mergeada para `master`.** Tudo está na branch `TESTE_NOVA_INTERFACE`.
