# Controle de Banco de Dados — Sistema Stock

Banco: **PostgreSQL**
Host: `qas-postgresql-ap.weg.net:40346`
Database: `stocksistem`

---

## Arquivos

[[⚡ Trigger - lista_pilares]]
Trigger que copia automaticamente linhas de `estoque_geral` para `lista_pilares` quando `valor_total$` >= R$ 50,00.


[[📄 db_manager — Código]]
Código Python do utilitário interativo para gerenciar o banco (criar tabelas, colunas e linhas).

[[📝 db_manager — Documentação]]
Explicação completa do código: como rodar, opções do menu, estrutura das funções.

[[✅ Tarefas do Banco]]
Notas e pendências sobre o que precisa ser feito no banco de dados.

[[Atualizações 2026-05-06]]
Registro de todas as alterações feitas em 06/05/2026 (delete, dashboard, nova interface).

---

## Como rodar o gerenciador

```powershell
cd "C:\Users\manriquef\Documents\Download app teste\download-app-stock"
.\.venv\Scripts\python.exe db_manager.py
```

## Como aplicar o trigger

```powershell
cd "C:\Users\manriquef\Documents\Download app teste\download-app-stock"
.\.venv\Scripts\python.exe apply_trigger.py
```

## Menu do db_manager (opções atuais)

| Opção | Ação |
|-------|------|
| 1 | Listar tabelas |
| 2 | Criar tabela |
| 3 | Adicionar coluna a uma tabela |
| 4 | Inserir linha |
| 5 | Listar linhas de uma tabela |
| 6 | Atualizar linha existente |
| 7 | Deletar uma linha |
| 8 | Deletar várias linhas |
| 9 | Limpar tabela inteira (TRUNCATE) |
| 0 | Sair |
