# Atualizações — Sistema de Stock | 12/05/2026

> **Branch:** `TESTE_NOVA_INTERFACE`
> **Status:** 🧪 Sessão de testes — `analisar_estoque` com SAP real
> **Contexto anterior:** [[Atualizações 2026-05-11]]

---

## Objetivo da sessão

Executar pela primeira vez o fluxo completo de `analisar_estoque()` com o SAP GUI aberto e logado, verificando cada fase individualmente pelos prints de debug.

---

## Checklist de testes

### Pré-requisitos

- [ ] SAP GUI aberto e logado
- [ ] Scripting habilitado: SAP GUI → Opções → Acessibilidade → Scripting
- [ ] `openpyxl` instalado: `.venv\Scripts\pip install openpyxl`
- [ ] Node.js no PATH (`node --version` no terminal)
- [ ] Edge aberto com debug na porta 9222 (necessário para o bot GISWEB)
- [ ] Acesso à rede WEG (VPN ou presencial)

---

### Fase 0 — Bot GISWEB

- [ ] Print `[BOT] stdout:` aparece sem erro
- [ ] `returncode == 0`
- [ ] `reports.xlsx` aparece na pasta Downloads
- [ ] Print `[BOT] ESTOQUE MEC carregado: N linhas` com N > 0
- [ ] Colunas do DataFrame incluem: `Material`, `Valor Unitário`, `Centro`, `Área`

**O que verificar:** Se o bot falhar, checar se o Edge está aberto com debug (`--remote-debugging-port=9222`) e se o usuário está logado no GISWEB.

---

### Fase 1 — CS12

- [ ] Transação CS12 abre sem erro
- [ ] Variante `/josimart` é selecionada (print confirma)
- [ ] `export.xlsx` é gerado na pasta SAP GUI
- [ ] Print `[CS12] BOM lida: N linhas` com N > 0
- [ ] Print `[CS12] Componentes totais: N | Marcados VER ESTOQUE: M` — verificar se M faz sentido

**O que verificar:** Se `VER ESTOQUE == 0`, o problema pode ser que os códigos do reports.xlsx não batem com os da BOM (formatos diferentes — ex: zeros à esquerda).

---

### Fase 2 — Enriquecimento

- [ ] `df_entrada` não está vazio
- [ ] Colunas `centro_estoque` e `preco_unitario` preenchidas para a maioria dos componentes
- [ ] Componentes sem match de área listados no print `[ESTOQUE MEC] Sem match`

---

### Fase 3 — ZTMM402

- [ ] Print `[ZTMM402] Centros válidos a processar: [...]` lista pelo menos um centro
- [ ] Print `[ZTMM402] ALV encontrado: Planilha em ALV (1).xlsx`
- [ ] Print `[ZTMM402] ALV lido: N linhas | colunas: [...]` — verificar se colunas batem com esperado
  - Esperado: `Material`, `Centro`, `Tipo de suprimento`, `Saldo`
- [ ] Print `[ZTMM402] Saldo preenchido em X/Y componentes`
- [ ] `df_lista_sap` não está vazio no print final

**O que verificar:** Se o nome das colunas do ALV for diferente, ajustar as constantes `col_mat`, `col_cen`, `col_tip`, `col_sal` em `_buscar_ztmm402()`.

---

### Fase 4 — MD04

- [ ] Print `[MD04] Coluna tipo: '...' | Coluna PEP: '...'` — confirmar posições corretas
- [ ] Print `[MD04] Valores únicos na coluna tipo:` — verificar se `"EstqPr"` aparece
- [ ] Print `[MD04] PEPs encontrados (EstqPr): N | Códigos: [...]`
- [ ] Fator calculado = quantidade de PEPs (ex: 3 PEPs → fator = 3.0)

**O que verificar:** Se `EstqPr` não aparece, checar a coluna tipo (col C do export). Pode ter espaços extras ou nome diferente.

---

### Fase 5 — Cálculo

- [ ] `df_resultado` com colunas `qtd_aproveitavel` e `valor_aproveitamento` preenchidas
- [ ] `valor_total > 0` para pelo menos alguns componentes
- [ ] Resultado bate aproximadamente com valores do Excel VBA para o mesmo CP

---

### Limpeza

- [ ] Excel encerrado completamente ao final (sem janela aberta)
- [ ] Print `[EXCEL] Aplicação Excel encerrada.` aparece

---

### UI — DataTable

- [ ] Linhas do `DATATABLE_APROVEITAMENTO_ESTOQUE` preenchidas após análise
- [ ] Valores monetários com 2 casas decimais (R$ 1.234,56)
- [ ] `VALOR_TOTAL_APROVADO` exibe `R$ X.XX`
- [ ] Lista de PEPs aparece no painel lateral
- [ ] `QUANTIDADE_PEP` exibe número correto

---

## Referência rápida — prints esperados

```
============================================================
[INICIO] analisar_estoque
  usuario    : manriquef
  cp         : 150-XXXXXXX-XX
  centro_lt  : 1500
============================================================

[FASE 0] Baixando ESTOQUE MEC via bot...
[BOT] Executando bot Node.js...
[BOT] reports.xlsx encontrado. Lendo arquivo...
[BOT] ESTOQUE MEC carregado: XXXX linhas, colunas: [...]

[SAP] Sessão obtida com sucesso.

[FASE 1] BOM via CS12...
[CS12] BOM lida: XX linhas
[CS12] Componentes totais: XX | Marcados VER ESTOQUE: X

[FASE 2] Enriquecendo com ESTOQUE MEC...
[ESTOQUE MEC] df_entrada gerado: X componentes

[FASE 3] Buscando saldo no ZTMM402...
[ZTMM402] Centros válidos a processar: ['1500']
[ZTMM402] ALV encontrado: Planilha em ALV (1).xlsx
[ZTMM402] ALV lido: XX linhas | colunas: [...]
[ZTMM402] Saldo preenchido em X/X componentes

[FASE 4] Buscando quantidades PEP via MD04...
[MD04] PEPs encontrados (EstqPr): 3 | Códigos: [...]
[FASE 4] Fator (= qtd PEPs): 3.0

[FASE 5] Calculando aproveitamento...
[CALC] Valor total aproveitamento: R$ X.XXX,XX

[CLEANUP] Fechando Excel por completo...
[EXCEL] Aplicação Excel encerrada.
============================================================
[FIM] Análise concluída.
============================================================
```

---

## Links úteis para debug

- [[📄 analisar_cp_estoque — Documentação SAP]] — referência de IDs SAP e colunas
- [[📄 bot_gisweb — Documentação]] — troubleshooting do bot
- [[🐛 Debug]] — quadro de debug geral do projeto
- [[Atualizações 2026-05-11]] — bugs já corrigidos na sessão anterior
