---
tags: [dominio, mecanico, geometria, nucleo, enrolamentos]
---

# Parâmetros Mecânicos e Geométricos

Relacionado: [[parte-ativa]] | [[nucleo]] | [[enrolamentos]] | [[canecos]] | [[comutadores]]

---

## 1. Núcleo Magnético

Ver detalhes em [[nucleo]].

| Símbolo | Descrição | Unidade |
|---|---|---|
| `D_col` | Diâmetro da coluna (círculo inscrito no escalonamento) | mm |
| `h_col` | Altura da coluna (= altura dos enrolamentos) | mm |
| `n_col` | Número de colunas (3 = trifásico, 1 = monofásico, 5 = 5 colunas) | — |
| `Bmax` | Indução máxima | T |
| `sf` | Fator de empilhamento (stacking factor) | típico 0,96–0,98 |
| `mat_nucleo` | Material / grau do aço silício | ex: 23ZDKH90 |
| `Kf` | Fator de forma da coluna (razão área real / D²) | ≈ 0,785 para círculo |

**Seção transversal da coluna:**
$$A_{col} = K_f \cdot D_{col}^2 \cdot sf$$

---

## 2. Enrolamentos — Vista Geral

Ver [[enrolamentos]] para tipos e detalhes.

### BT (enrolamento interno — mais próximo do núcleo)

| Símbolo | Descrição | Unidade |
|---|---|---|
| `D_BT_int` | Diâmetro interno BT | mm |
| `D_BT_ext` | Diâmetro externo BT | mm |
| `h_BT` | Altura do enrolamento BT | mm |
| `n_turns_BT` | Número de espiras BT | — |
| `tipo_BT` | Tipo de bobina BT | ex: folha (foil), disco, camada |

### Cilindro isolante BT→AT

| Símbolo | Descrição |
|---|---|
| `t_cil` | Espessura do cilindro isolante (pressboard) |
| `n_cil` | Número de camadas do cilindro |
| `d_AT_BT` | Distância radial BT externo → AT interno (inclui cilindro + canais de óleo) |

### AT (enrolamento externo)

| Símbolo | Descrição | Unidade |
|---|---|---|
| `D_AT_int` | Diâmetro interno AT | mm |
| `D_AT_ext` | Diâmetro externo AT | mm |
| `h_AT` | Altura do enrolamento AT | mm |
| `n_turns_AT` | Número de espiras AT | — |
| `tipo_AT` | Tipo de bobina AT | ex: disco contínuo, disco interleaved, hélice |

---

## 3. Estrutura de Suporte e Pressagem

| Símbolo | Descrição |
|---|---|
| `h_prensagem_inf` | Altura da estrutura de pressagem inferior (lower yoke clamp) |
| `h_prensagem_sup` | Altura da estrutura de pressagem superior |
| `h_bloco_press` | Altura dos blocos de pressão entre enrolamentos e prensa |
| `mat_prensagem` | Material (isolado ou aterrado) |

---

## 4. Dimensões da Parte Ativa

| Símbolo | Descrição | Relação |
|---|---|---|
| `H_PA` | Altura total da parte ativa | = h_col + h_jugo_sup + h_jugo_inf + h_prensagens |
| `L_PA` | Largura total (trifásico) | = n_col × D_col + (n_col-1) × d_entre_colunas + 2 × D_AT_ext/2 |
| `W_PA` | Profundidade | ≈ D_AT_ext |

---

## 5. Dimensões do Tanque

Derivadas da parte ativa + distâncias elétricas:

| Símbolo | Fórmula | Descrição |
|---|---|---|
| `L_tanque` | `L_PA + 2 × d_AT_tanque` | Comprimento interno |
| `W_tanque` | `W_PA + 2 × d_AT_tanque` | Largura interna |
| `H_tanque` | `H_PA + d_fundo + d_topo` | Altura interna (sem comutador) |
| `H_tanque_c` | `H_tanque + h_comutador + d_comut_AT` | Com comutador no topo |

> As distâncias `d_AT_tanque`, `d_fundo`, `d_topo` vêm da análise dielétrica. Ver [[calculos/metodologia-distancias]].

---

## 6. Massa e Volume (estimativas)

| Grandeza | Estimativa |
|---|---|
| Massa do núcleo | `A_col × h_col × n_col × ρ_aço × sf` |
| Volume de óleo ativo | Volume interno do tanque − volume da parte ativa |
| Massa total (ordem de grandeza) | Depende fortemente de Sn e Um |

---

## Notas do usuário

> _Inserir referências de projetos com dimensões reais para calibrar as fórmulas_
