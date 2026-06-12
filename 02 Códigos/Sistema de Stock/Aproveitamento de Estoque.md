# Aproveitamento de Estoque

> **Módulo:** Análise de aproveitamento de estoque SAP — tradução de automação VBA para Python
> **Arquivo principal:** `app/ui/services/analisar_cp_estoque.py`
> **Página UI:** `app/ui/layout/pages/aproveitamento_stock.py`
> **Status:** 🔨 Em desenvolvimento — função implementada, testes pendentes

---

## Links rápidos

- [[📄 analisar_cp_estoque — Documentação SAP]] — como funciona toda a integração com o SAP
- [[📄 bot_gisweb — Documentação]] — bot Node.js que baixa o estoque do GISWEB
- [[Atualizações 2026-05-11]] — sessão de implementação completa
- [[Atualizações 2026-05-12]] — testes planejados para amanhã
- [[🧪 Testes]] — status de testes do projeto
- [[🚀 Melhorias]] — backlog de melhorias

---

## O que faz

Dado um **CP (código de produto)**, analisa quais componentes da sua lista técnica têm estoque disponível no armazém MEC e calcula o valor que pode ser aproveitado, evitando compras desnecessárias.

Substitui as macros VBA dos arquivos:
- `modulo_lista.vba` → Fase 1 (CS12)
- `modulo_estoque.vba` → Fases 2, 3
- `modulo_quantidade_pep.vba` → Fase 4

---

## Fluxo de 5 fases

```
FASE 0 → Bot GISWEB baixa reports.xlsx → df_estoque_mec
FASE 1 → CS12 (SAP) exporta BOM do CP → df_lista_comp
FASE 2 → Cruzamento BOM × Estoque MEC → df_entrada
FASE 3 → ZTMM402 (SAP) busca saldo disponível → df_lista_sap
FASE 4 → MD04 (SAP) lê quantidades PEP → qtds_pep / fator
FASE 5 → Cálculo: qtd_aproveitavel × preco_unitario → df_resultado
```

---

## Parâmetros da função principal

```python
analisar_estoque(usuario, centro_user, cp, centro_lt, area)
```

| Parâmetro | Exemplo | Descrição |
|-----------|---------|-----------|
| `usuario` | `"manriquef"` | Login Windows (para localizar pasta SAP GUI) |
| `centro_user` | `"1500"` | Centro do usuário |
| `cp` | `"150-1234567-1A"` | Código do CP a analisar |
| `centro_lt` | `"1500"` | Centro para CS12 e MD04 |
| `area` | `"MECANICA"` | Filtro do estoque: `GERAL`, `MECANICA`, ou tag específica |

---

## Fórmula de cálculo

```
fator          = quantidade de PEPs (EstqPr) encontrados no MD04
                 (= 1.0 se nenhum PEP encontrado)

qtd_aproveitavel  = min(qtd_necessaria × fator,  estoque_sap)

valor_aproveitamento = qtd_aproveitavel × preco_unitario
                       se > R$ 50,00, senão 0
```

---

## Estrutura de retorno

```python
{
    "df_resultado":  pd.DataFrame,  # resultado final com todos os campos
    "df_lista_comp": pd.DataFrame,  # BOM completa do CS12
    "df_lista_sap":  pd.DataFrame,  # ALV consolidado do ZTMM402
    "qtds_pep":      list[str],     # códigos dos PEPs encontrados no MD04
    "valor_total":   float,         # soma dos valores aproveitáveis
    "qtd_peps":      int,           # quantidade de PEPs
}
```

---

## Pendências

- [ ] Coluna `comprador` preenchida com `None` — implementar lookup futuro
- [ ] Conectar `df_resultado` ao DataTable da UI (`aproveitamento_stock.py`)
- [ ] Testes completos com SAP aberto → [[Atualizações 2026-05-12]]
- [ ] Verificar se coluna `"Tipo de suprimento"` no ALV bate com nome real
