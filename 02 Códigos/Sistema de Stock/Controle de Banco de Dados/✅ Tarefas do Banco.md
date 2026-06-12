# Tarefas do Banco de Dados

← [[🗄️ Banco de Dados]]

Use esta nota para registrar tudo que precisa ser feito, alterado ou revisado no banco PostgreSQL do Sistema Stock.

---

## Tabelas

> Registre aqui as tabelas que precisam ser criadas, alteradas ou removidas.

- [ ] Criar tabela `lista_pilares` com as colunas: `cp`, `cliente`, `centro`, `responsavel`, `data_cadastro`, `valor_total$`, `status`
- [ ] Criar tabela `users` com as colunas: `username`, `senha`, `tipo`, `email`, `centro`, `area`

---

## Colunas

> Colunas a adicionar ou modificar em tabelas existentes.

- [ ] 

---

## Dados

> Inserções, correções ou limpezas de dados que precisam ser feitas.

- [ ] 

---

## Pendências gerais

- [ ] Aplicar o trigger `trigger_lista_pilares` no banco rodando `apply_trigger.py`

---

## Histórico

> Registre aqui o que já foi feito (data + descrição).

| Data | O que foi feito |
|------|-----------------|
| 2026-05-05 | Criado `db_manager.py` — gerenciador interativo do banco com menu (listar tabelas, criar tabela, adicionar coluna, inserir linha, listar linhas, atualizar linha) |
| 2026-05-05 | Adicionada opção 6 no `db_manager.py` para atualizar linhas existentes via `UPDATE` |
| 2026-05-05 | Criado `trigger_lista_pilares.sql` — trigger que copia automaticamente para `lista_pilares` todo INSERT em `estoque_geral` com `valor_total$` >= R$ 50,00 com status `pendente` |
| 2026-05-05 | Criado `apply_trigger.py` — script para aplicar o trigger no banco sem conflito com o PowerShell |
| 2026-05-06 | Adicionadas opções 7, 8 e 9 no `db_manager.py`: deletar uma linha, deletar várias linhas (IN) e TRUNCATE com RESTART IDENTITY — ver [[Atualizações 2026-05-06]] |
