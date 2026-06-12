# Atualizações — Sistema de Stock | 11/05/2026

> **Branch:** `TESTE_NOVA_INTERFACE`
> **Status:** 🔨 Função `analisar_estoque` implementada — testes com SAP pendentes
> **Contexto anterior:** [[Atualizações 2026-05-08]]
> **Próxima sessão:** [[Atualizações 2026-05-12]]

---

## Resumo do dia

Sessão intensa de desenvolvimento e debug. A função `analisar_estoque` foi **completamente implementada** — tradução das 3 macros VBA para Python com DataFrames. Ao longo da sessão, múltiplos erros de runtime foram identificados e corrigidos.

---

## 1. Implementação — `analisar_cp_estoque.py`

> Nota de referência: [[Aproveitamento de Estoque]] | [[📄 analisar_cp_estoque — Documentação SAP]]

### O que foi feito

- Tradução completa das macros VBA para Python:
  - `modulo_lista.vba` → `_buscar_lista_comp_sap()` + `_processar_lista_comp()`
  - `modulo_estoque.vba` → `_enriquecer_com_estoque_mec()` + `_buscar_ztmm402()`
  - `modulo_quantidade_pep.vba` → `_buscar_qtd_pep()`
- Integração com SAP via `win32com.client` (SAP GUI Scripting)
- Substituição do arquivo Excel local `ESTOQUE MEC.xlsx` pelo bot GISWEB

### Remoção de dependências Excel

Conforme decisão de arquitetura:

| Dependência removida | Substituição |
|---------------------|--------------|
| `ESTOQUE MEC.xlsx` (local) | Bot Node.js baixa `reports.xlsx` do GISWEB |
| `COMPRADORES.xlsx` | Coluna `comprador` preenchida com `None` (implementação futura) |

---

## 2. Bugs corrigidos

### 2.1 ALV do ZTMM402 vazio após Close COM error

**Problema:** O workbook ALV era fechado com `wb.Close(False)`, que lançava `COMError: O método Close da classe Workbook falhou`. Por conta do erro, os dados não eram capturados.

**Solução:** Capturar os dados **antes** da tentativa de fechar. Fechar usando `DisplayAlerts=False` + `wb.Saved=True`. Ignorar erro de close com try/except — os dados já estão no DataFrame.

```python
dados = ws.UsedRange.Value      # captura ANTES
try:
    xl.DisplayAlerts = False
    wb.Saved = True
    wb.Close(False)
except Exception as close_err:
    print(f"Aviso ao fechar ALV (dados já capturados): {close_err}")
```

### 2.2 MD04 lendo arquivo errado (export do ZTMM402)

**Problema:** O `export.xlsx` do ZTMM402 ficava aberto/travado no Excel. Quando o MD04 tentava exportar, o arquivo não era sobrescrito e o Python lia os dados da BOM anterior.

**Solução:** Chamar `_fechar_workbooks_export_no_excel()` no início de `_buscar_qtd_pep()` para garantir que o arquivo seja liberado antes da nova exportação.

### 2.3 Fator calculado errado (soma vs. contagem)

**Problema:** `fator = sum(qtds_pep)` — somava os valores numéricos, mas os PEPs são códigos string.

**Solução:** `fator = float(len(qtds_pep))` — conta a quantidade de PEPs. O fator representa o número de ordens de projeto que usam o mesmo CP.

### 2.4 PEP codes como float causando AttributeError

**Problema:** O código tentava `float(row[col_pep])` para obter o código do PEP, mas PEPs são strings como `"150-2500096-1C"`.

**Solução:** Armazenar como string via `_clean_key(row[col_pep])`.

### 2.5 Colunas datetime com timezone quebravam iterrows

**Problema:** O ALV do ZTMM402 tem colunas datetime com timezone (`datetimetz`), que causavam `AttributeError: 'NoneType' object has no attribute 'total_seconds'` durante `iterrows()`.

**Solução:** Após `pd.concat`, remover timezone de todas as colunas datetime:

```python
for col in df_lista_sap.columns:
    if pd.api.types.is_datetime64_any_dtype(df_lista_sap[col]):
        try:
            df_lista_sap[col] = df_lista_sap[col].dt.tz_convert(None)
        except TypeError:
            df_lista_sap[col] = df_lista_sap[col].dt.tz_localize(None)
```

### 2.6 SAP GUI não conectado — erro críptico

**Problema:** `pywintypes.com_error: (-2147221020, 'Sintaxe inválida', None, None)` quando SAP não estava aberto.

**Solução:** Encapsular `_sap_session()` em try/except com mensagem clara:

```python
raise RuntimeError(
    "Não foi possível conectar ao SAP GUI.\n"
    "Verifique se:\n"
    "  1. O SAP GUI está aberto e logado\n"
    "  2. O scripting está habilitado (Opções → Acessibilidade → Scripting)"
)
```

---

## 3. Melhorias de UX e debug

- **Prints de debug** em todas as fases com prefixos: `[BOT]`, `[CS12]`, `[ESTOQUE MEC]`, `[ZTMM402]`, `[MD04]`, `[CALC]`, `[EXCEL]`, `[CLEANUP]`
- **Print de DataFrames** ao final de cada fase: `df_estoque_mec`, `df_lista_comp`, `df_entrada`, `df_lista_sap`, `df_resultado`
- **Print de PEPs** com quantidade e códigos encontrados

---

## 4. Limpeza do Excel ao final

**Problema:** Após o processo, a janela do Excel ficava aberta sem planilhas.

**Solução:** Ao final de `analisar_estoque()`, chamar:

```python
_fechar_workbooks_export_no_excel(fechar_aplicacao=True)
```

O parâmetro `fechar_aplicacao=True` fecha todos os workbooks restantes e chama `xl.Quit()` para encerrar o processo Excel completamente.

---

## 5. Formatação monetária na UI

**Arquivo:** `app/ui/layout/pages/aproveitamento_stock.py`

Valores monetários agora formatados com 2 casas decimais:

| Campo | Antes | Depois |
|-------|-------|--------|
| Valor Unit. (tabela) | `row["preco_unitario"]` | `f"{row['preco_unitario']:.2f}"` |
| Valor Aprov. (tabela) | `row["valor_aproveitamento"]` | `f"{row['valor_aproveitamento']:.2f}"` |
| Valor Total (rodapé) | `f"R$ {valor_total}"` | `f"R$ {valor_total:.2f}"` |

Também removidas duas linhas `.round(2)` que não tinham efeito (resultado não era atribuído de volta).

---

## 6. Bug UI — ft.Column argumento posicional errado

**Erro:**
```
TypeError: Column.__init__() got multiple values for argument 'controls'
```

**Causa:** `ft.MainAxisAlignment.CENTER` passado como primeiro argumento posicional, que é `controls`.

**Solução:** Mudar para `alignment=ft.MainAxisAlignment.CENTER` (argumento nomeado).

---

## Arquivos modificados hoje

| Arquivo | Tipo de mudança |
|---------|----------------|
| `app/ui/services/analisar_cp_estoque.py` | Reescrita completa — implementação das 5 fases |
| `app/ui/services/bot/index.js` | Bot GISWEB (já existia) — integrado ao fluxo Python |
| `app/ui/layout/pages/aproveitamento_stock.py` | Formatação monetária, fix argumento ft.Column |

---

## Pendências da sessão

- [ ] `pip install openpyxl` no venv (necessário para `pd.read_excel` com `.xlsx`)
- [ ] Coluna `comprador` — implementação do lookup futuro
- [ ] Teste completo com SAP aberto → [[Atualizações 2026-05-12]]
- [ ] Conectar `df_resultado` ao DataTable da UI

---

> **Próxima sessão:** [[Atualizações 2026-05-12]] — Testes com SAP
