---
tags: [dominio, canecos, discos, secoes, bobinas]
---

# Canecos (Seções de Bobina / Discos)

Relacionado: [[enrolamentos]] | [[distancias-eletricas]] | [[calculos/metodologia-distancias]]

---

## Definição

"Canecos" = **discos** ou **seções** de um enrolamento de disco contínuo. Cada caneco é um grupo de espiras enroladas radialmente num plano horizontal, empilhados axialmente para formar o enrolamento completo.

```
    ─────────────────────────   ← d_entre_canecos (canal de óleo)
    ┌───────────────────────┐
    │      Caneco n         │   h_caneco
    └───────────────────────┘
    ─────────────────────────   ← d_entre_canecos
    ┌───────────────────────┐
    │      Caneco n-1       │
    └───────────────────────┘
    ─────────────────────────
         ...
```

---

## Parâmetros Geométricos

| Símbolo | Descrição | Unidade |
|---|---|---|
| `n_c` | Número de canecos total no enrolamento | — |
| `n_esp_c` | Número de espiras por caneco | — |
| `h_c` | Altura do caneco (axial) | mm |
| `d_ec` | Distância entre canecos (axial — canal de óleo) | mm |
| `D_int` | Diâmetro interno do caneco (= D_int do enrolamento) | mm |
| `D_ext` | Diâmetro externo do caneco (= D_ext do enrolamento) | mm |
| `b_c` | Largura radial do caneco = (D_ext − D_int) / 2 | mm |
| `angulo_c` | Ângulo de inclinação (em bobinas helicoidais inclinadas) | ° |

---

## Altura total do enrolamento

$$h_{enrol} = n_c \cdot h_c + (n_c - 1) \cdot d_{ec}$$

---

## Tensão por Caneco

Para enrolamento de disco contínuo com tensão uniformemente distribuída:

$$U_{por\_caneco} = \frac{U_{AT}}{n_c} \cdot n_{esp\_c}$$ (aproximado, campo estático)

> Em condições de impulso, a distribuição de tensão **não é uniforme** — os canecos do topo (linha) absorvem muito mais tensão. Isso define `d_entre_canecos` nos extremos como sendo maior.

### Distribuição de tensão sob impulso

```
Tensão (kV)
  BIL ─────────────────────────────────────────────────────── topo (linha)
       \
        \
         \──────────────────────────── região intermediária (dist. uniforme)
                                                              \
                                                               \──── 0 V (neutro)
  0 ─────────────────────────────────────────────────────────────────────────
       Caneco 1       ...       Caneco n/2         ...        Caneco n
```

O fator de distribuição `α` define quão não-uniforme é a distribuição:
$$\alpha = h \sqrt{\frac{C_s}{C_g}}$$

- `C_s`: capacitância série (entre espiras / canecos)
- `C_g`: capacitância shunt (caneco → terra)

Para `α` grande (típico em discos): tensão concentrada no topo.

---

## Tipos de Caneco / Disco

| Tipo | Característica |
|---|---|
| **Disco simples** | Espiras contínuas num plano, saída interna e externa alternadas |
| **Disco interleaved (entrelaçado)** | Espiras de canecos adjacentes intercaladas → aumenta C_s → melhora distribuição de impulso |
| **Disc com blindagem eletrostática** | Eletrodo metálico no topo para redistribuir tensão de impulso |
| **Caneco reforçado (end disc)** | Canecos extremos com isolamento adicional (mais papel, espaçadores maiores) |

---

## Distâncias Críticas dos Canecos

### Entre canecos (d_entre_canecos)

Determinado pelo maior dos critérios:
1. **Dielétrico**: tensão entre canecos adjacentes (impulso) → distância mínima em óleo
2. **Térmico**: canal de óleo mínimo para resfriamento por convecção

$$d_{ec,min} = \max(d_{ec,dieletrico},\; d_{ec,termico})$$

### Caneco extremo → estrutura aterrada (prensa)

Este é o `d_fundo` e `d_topo` do enrolamento AT. O caneco de topo está à tensão BIL_AT, enquanto a estrutura de pressagem pode ser aterrada.

$$d_{extrem} = f(BIL_{AT},\; \text{geometria do eletrodo})$$

### Entre canecos em posição de tap (comutador)

Os canecos de derivação (tap discs) têm tensões em relação ao restante do enrolamento dependentes da posição do tap. Ver [[comutadores]].

---

## Notas do usuário

> _Preencher com número típico de canecos por projeto, dimensões reais, tipo de disco utilizado (simples, interleaved)_
