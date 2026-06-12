# analisar_cp_estoque.py — Documentação SAP

← [[Aproveitamento de Estoque]] | [[⭐ Sistema Stock]]

> **Arquivo:** `app/ui/services/analisar_cp_estoque.py`
> **Tecnologia SAP:** `win32com.client` — SAP GUI Scripting via COM (Windows)
> **Requisito:** SAP GUI aberto, logado e com scripting habilitado

---

## Como o Python fala com o SAP

O SAP GUI expõe uma interface COM (Component Object Model) do Windows. O Python acessa essa interface via `win32com.client.GetObject("SAPGUI")`, navegando pela hierarquia:

```
SAPGUI
 └── GetScriptingEngine   (GuiApplication)
      └── Children(0)     (GuiConnection — conexão ativa)
           └── Children(0) (GuiSession — sessão ativa)
```

Toda interação com telas SAP é feita pelo objeto `session`:

```python
session.findById("wnd[0]/tbar[0]/okcd").Text = "/ncs12"  # digita transação
session.findById("wnd[0]").sendVKey(0)                    # pressiona Enter
session.findById("wnd[0]/tbar[1]/btn[8]").press()         # F8 (executar)
```

### IDs dos elementos SAP

Os IDs seguem a notação:
```
wnd[N]          → janela (0 = principal, 1 = popup, 2 = segundo popup)
/tbar[N]        → toolbar (0 = barra de menu, 1 = barra de botões)
/btn[N]         → botão (número conforme layout SAP)
/usr/...        → área de usuário (campos de input)
/mbar/menu[N]/menu[N]/...  → menu na barra de menus
```

---

## Fase 0 — Bot GISWEB (reports.xlsx)

> Documentação completa: [[📄 bot_gisweb — Documentação]]

```python
_baixar_estoque_mec(usuario)  →  pd.DataFrame
```

- Executa `node index.js` na pasta `app/ui/services/bot/`
- O bot abre o Edge conectado ao GISWEB e clica em "Exportar Materiais"
- Aguarda até 60 segundos o arquivo `reports.xlsx` aparecer em `Downloads/`
- Lê com `pd.read_excel()` e retorna o DataFrame

**Colunas utilizadas do reports.xlsx:**

| Coluna | Uso |
|--------|-----|
| `Material` | Código do material (chave de cruzamento) |
| `Valor Unitário` | Preço unitário para cálculo de aproveitamento |
| `Centro` | Centro do armazém MEC onde o material está |
| `Área` | Tag de área (MECANICA, PARTE ATIVA, BOBINAGEM, etc.) |

---

## Fase 1 — CS12 (BOM Explosion)

```python
_buscar_lista_comp_sap(session, cp, centro_lt, usuario)  →  pd.DataFrame (raw)
_processar_lista_comp(df_raw, codigos_estoque_mec)        →  pd.DataFrame (processado)
```

### O que é CS12

Transação SAP que **explode a lista técnica** (BOM — Bill of Materials) de um material. Mostra todos os componentes de todos os níveis da estrutura do produto.

### Sequência de automação

```
1. /ncs12 → Enter
2. Preenche: Material = cp, Centro = centro_lt, Uso = "01", Aplicação = "pp01"
3. F8 (executar)
4. Abre seletor de variante → busca "/josimart" → seleciona
5. Menu: Lista → Exportar → Planilha → Local
   (mbar/menu[3]/menu[3]/menu[1]/menu[1])
6. Aguarda export.xlsx na pasta SAP GUI do usuário
```

**Pasta de export:** `C:\Users\{usuario}\Documents\SAP\SAP GUI\` (ou OneDrive equivalente)

### Processamento do DataFrame

A BOM exportada tem 9 colunas. A coluna de índice 2 é descartada (coluna de agrupamento interno do CS12). O resultado é renomeado:

| Índice (após drop col 2) | Nome | Conteúdo |
|--------------------------|------|----------|
| 0 | `nivel` | Nível hierárquico na BOM |
| 1 | `parent` | Material pai |
| 2 | `codigo` | **Código do componente** |
| 3 | `descricao` | Descrição do material |
| 4 | `uom` | Unidade de medida |
| 5 | `quantidade` | Quantidade necessária |
| 6 | `modificacao` | Modificação/revisão |
| 7 | `col_h` | Campo adicional |

Após renomear, cada linha recebe `ver_estoque = "VER ESTOQUE"` se o código está no conjunto `codigos_estoque_mec` (vindo do `reports.xlsx`).

---

## Fase 2 — Enriquecimento com Estoque MEC

```python
_enriquecer_com_estoque_mec(df_lista_comp, df_estoque_mec, area)  →  pd.DataFrame
```

Filtra apenas os componentes marcados `VER ESTOQUE` e faz o cruzamento com o `df_estoque_mec` para obter preço e centro.

### Regras de filtro por área

| `area` passado | Comportamento |
|----------------|---------------|
| `"GERAL"` | Aceita qualquer linha do estoque MEC |
| `"MECANICA"` | Exclui linhas com área: `PARTEATIVA`, `BOBINAGEM`, `CALCULO`, `FIACAO` |
| outra tag | Aceita apenas linhas onde a área normalizada bate exatamente |

> A normalização remove acentos, espaços, hifens e converte para maiúsculas. Ex: `"Parte Ativa"` → `"PARTEATIVA"`.

### Resultado: df_entrada

| Coluna | Tipo | Origem |
|--------|------|--------|
| `codigo` | str | BOM (CS12) |
| `descricao` | str | BOM (CS12) |
| `qtd_necessaria` | float | soma das quantidades na BOM |
| `modificacao` | str | BOM (CS12) |
| `centro_estoque` | str | `reports.xlsx` col `Centro` |
| `preco_unitario` | float | `reports.xlsx` col `Valor Unitário` |
| `estoque_sap` | float | preenchido na Fase 3 (começa em 0.0) |
| `comprador` | None | pendente implementação |
| `tipo_suprimento` | str | preenchido na Fase 3 (começa vazio) |

---

## Fase 3 — ZTMM402 (Saldo Disponível)

```python
_buscar_ztmm402(session, df_entrada)              →  pd.DataFrame (df_lista_sap)
_buscar_ztmm402_por_centro(session, centro, materiais)  →  pd.DataFrame | None
```

### O que é ZTMM402

Transação customizada WEG que mostra o **saldo de estoque disponível** por material e centro. É um relatório ALV (ABAP List Viewer).

### Sequência de automação

```
1. /nZTMM402 → Enter
2. Carrega variante "PROVISÃO 1500" (btn[17] → digita nome → Enter)
3. Seleciona tipo de agrupamento (radP_AGR_W)
4. Insere centro via popup de múltiplos valores
5. Cola lista de materiais via clipboard (win32clipboard)
6. F8 (executar)
7. Seleciona variante de layout "JOSIMART" (btn[33])
8. Exporta ALV para Excel (btn[43])
```

### Captura do ALV

O SAP exporta o ALV como workbook do Excel (nome contém "ALV"). O Python acessa via COM:

```python
xl = win32com.client.GetActiveObject("Excel.Application")
for wb in xl.Workbooks:
    if "ALV" in wb.Name:
        dados = wb.Sheets(1).UsedRange.Value
        # dados[0] = cabeçalhos, dados[1:] = linhas
```

> **Atenção:** o workbook é fechado com `DisplayAlerts=False` + `wb.Saved=True` + `wb.Close(False)` para contornar o erro COM "O método Close falhou". Os dados são capturados **antes** da tentativa de fechar.

### Colunas do ALV ZTMM402

| Coluna | Uso |
|--------|-----|
| `Material` | Chave de busca |
| `Centro` | Centro do saldo |
| `Tipo de suprimento` | Transferência interna, compra externa, etc. |
| `Saldo` | Quantidade disponível |

### Centros válidos

Apenas os centros `{"1202", "1500", "1502", "1504", "1505"}` são processados. Cada centro gera uma execução separada do ZTMM402.

### Preenchimento do df_entrada

A chave de cruzamento é `codigo|centro_estoque`. O saldo e tipo_suprimento são preenchidos diretamente no `df_entrada`:

```python
chave = codigo + "|" + centro_estoque
df_entrada.at[i, "estoque_sap"]     = idx_saldo.get(chave, 0.0)
df_entrada.at[i, "tipo_suprimento"] = idx_supr.get(chave, "")
```

---

## Fase 4 — MD04 (Quantidade PEP)

```python
_buscar_qtd_pep(session, cp, centro_lt, usuario)  →  list[str]
```

### O que é MD04

Transação SAP de **MRP (Material Requirements Planning)**. Mostra a lista de necessidades/estoques planejados para um material+centro, incluindo quantidades reservadas por ordens de projeto (PEPs/WBS Elements).

### Sequência de automação

```
1. /nmd04 → Enter
2. Preenche Material = cp, Área de MRP = centro_lt, Centro = centro_lt
3. Menu: Pasta → Exportar → Planilha Local (menu[0]/menu[5])
4. Exporta para Excel (btn[43])
5. Aguarda export.xlsx na pasta SAP GUI
```

### Leitura do export

O arquivo exportado é lido com `pd.read_excel()`. As colunas relevantes são:

| Posição | Nome (variável) | Conteúdo |
|---------|-----------------|----------|
| col C (índice 2) | `col_tipo` | Tipo de elemento MRP |
| col F (índice 5) | `col_pep` | Código do PEP/WBS Element |

Apenas as linhas onde `col_tipo == "EstqPr"` (Estoque de Projeto) são coletadas. O valor `col_pep` é o código do PEP (ex: `"150-2500096-1C"`).

### Fator

```python
fator = float(len(qtds_pep))   # número de PEPs encontrados
# Se não houver PEPs:
fator = 1.0
```

> O fator representa **quantas ordens de projeto** estão consumindo o mesmo CP. Se há 3 PEPs, a quantidade necessária do componente é multiplicada por 3.

---

## Fase 5 — Cálculo Final

```python
_calcular_aproveitamento(df_entrada, fator)  →  pd.DataFrame
```

```python
qtd_aproveitavel     = min(qtd_necessaria * fator, estoque_sap)
valor_aproveitamento = qtd_aproveitavel * preco_unitario  if > 50  else 0.0
```

O limiar de R$ 50,00 existe para filtrar aproveitamentos insignificantes (replicado do VBA original).

---

## Limpeza ao final

```python
_fechar_workbooks_export_no_excel(fechar_aplicacao=True)
```

Ao final de `analisar_estoque()`, o código fecha **todos** os workbooks abertos no Excel e depois chama `xl.Quit()` para encerrar a aplicação Excel completamente.

Durante o processo (antes do MD04), apenas os workbooks `export*` são fechados para liberar o arquivo em disco sem derrubar o Excel.

---

## Tratamento de erros comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `RuntimeError: Não foi possível conectar ao SAP GUI` | SAP não aberto ou scripting desabilitado | Abrir SAP, logar e habilitar scripting em Opções → Acessibilidade |
| `FileNotFoundError: export.xlsx não gerado` | Timeout — SAP demorou mais de 20s para exportar | Aumentar `timeout` em `_aguarda_arquivo` ou verificar SAP |
| `df_lista_sap vazio` | ALV do ZTMM402 não encontrado no Excel | Verificar se o nome do workbook contém "ALV" |
| `ModuleNotFoundError: openpyxl` | Pacote não instalado | `pip install openpyxl` no venv |
| Colunas do ALV com nome errado | Nome da coluna no SAP diferente do esperado | Verificar print `[ZTMM402] ALV lido: ... colunas: ...` |

---

## Dependências Python

```
win32com.client   (pywin32)   — SAP GUI Scripting e Excel COM
win32clipboard    (pywin32)   — colar materiais no SAP
pandas                        — DataFrames
openpyxl                      — engine para pd.read_excel com .xlsx
subprocess                    — executar o bot Node.js
```
