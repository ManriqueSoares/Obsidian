# Correntes Máximas — Transformador ADA DATA CENTER

> Transformador **C19163865** | Base: **40.000 kVA (ONAF)** | **ABNT NBR 5356/2007**
> Fontes: `Folha 1` L20–L21 (correntes) | L37–L41 (condutores e densidades)

---

## 1. Tabela Geral — Dados da Planilha

| Grandeza | BT1 | AT1 | AT2 | Fonte |
|---|---|---|---|---|
| Ligação | Estrela (YN) | Delta | Delta | Folha 1, L19 |
| Máxima corrente de linha (A) | **669,4** | **185,9** | **185,9** | Folha 1, L20 |
| Máxima corrente de fase (A) | **669,4** | **107,4** | **107,4** | Folha 1, L21 |
| Seção total do condutor (mm²) | 165,5 | 25,11 | 34,84 | Folha 1, L40 |
| Máxima densidade de corrente (A/mm²) | **4,045** | **4,275** | **3,081** | Folha 1, L41 |

---

## 2. A Discrepância — Por que a corrente AT da planilha difere do cálculo nominal?

No [[CORE]], a corrente AT foi calculada como **167,4 A**. A planilha mostra **185,9 A**. Ambos estão corretos — referem-se a condições diferentes.

**167,4 A** → corrente na AT no **tap nominal (Tap 9, 138 kV)**:
```
I_AT_nominal = S / (√3 × V_AT_nominal) = 40.000.000 / (√3 × 138.000) = 167,4 A
```

**185,9 A** → corrente na AT no **tap mínimo (Tap 17, 124,2 kV)** — a condição de máxima corrente:
```
I_AT_max = S / (√3 × V_AT_min) = 40.000.000 / (√3 × 124.200) = 185,9 A  ✓
```

### Por que o tap mínimo gera a corrente máxima?

A potência transmitida é constante em 40 MVA. A corrente é inversamente proporcional à tensão:

$$I = \frac{S}{\sqrt{3} \times V}$$

Quando o tap recua para 124,2 kV (−10%), com a mesma potência, a corrente sobe +11,1%:

```
I_Tap1  = 40.000.000 / (√3 × 151.800) = 152,1 A   (tap máximo — menor corrente AT)
I_Tap9  = 40.000.000 / (√3 × 138.000) = 167,4 A   (tap nominal)
I_Tap17 = 40.000.000 / (√3 × 124.200) = 185,9 A   (tap mínimo — MAIOR corrente AT)
```

O condutor da AT deve ser dimensionado para **185,9 A**, não para 167,4 A, porque ele precisa operar sem superaquecimento em qualquer posição de tap.

**Na BT não há esse efeito:** a tensão BT é sempre 34.500 V independentemente do tap (o tap changer age sobre a AT). Por isso a corrente BT é constante:
```
I_BT = 40.000.000 / (√3 × 34.500) = 669,4 A  — igual em qualquer tap  ✓
```

---

## 3. Corrente de Linha vs. Corrente de Fase

A corrente que circula pelo **condutor** da bobina é a **corrente de fase**, não necessariamente a de linha. A diferença depende da ligação:

### Ligação Estrela (BT1 — YN)

Em estrela, cada bobina está entre um terminal de linha e o neutro. A corrente de linha entra direto na bobina — portanto:

```
I_fase_BT1 = I_linha_BT1 = 669,4 A
```

O condutor BT1 carrega **669,4 A** — a corrente de linha completa.

### Ligação Delta (AT1 e AT2)

Em delta, cada bobina está conectada entre dois terminais de linha. A corrente de linha divide-se pelas duas bobinas adjacentes que compartilham aquele terminal. Pela geometria fasorial do delta:

$$I_{fase} = \frac{I_{linha}}{\sqrt{3}}$$

```
I_fase_AT1 = I_linha_AT1 / √3 = 185,9 / 1,7321 = 107,4 A  ✓  (Folha 1, L21)
I_fase_AT2 = 185,9 / √3 = 107,4 A                           ✓
```

**Verificação geométrica:**

```
          I_linha_A = 185,9 A →
                       ┌───────────────┐
                       │  bobina A–B   │ ← I_fase = 107,4 A
    linha A ───────────┤               ├─────────── linha B
                       │               │
                       └────────┬──────┘
                                │ bobina C–A ← I_fase = 107,4 A
                         linha C┘

A corrente de linha (185,9 A) é √3 × a corrente de fase (107,4 A)
```

O condutor AT1 só precisa conduzir **107,4 A** (fase), não os 185,9 A de linha. Isso é uma vantagem da ligação delta: permite usar condutores mais finos mesmo com alta tensão de linha.

---

## 4. Correntes por Tap — Tabela Completa

Base: **ONAF — 40.000 kVA**

| Tap | Tensão AT (V) | I linha AT (A) | I fase AT (A) | I linha BT (A) | I fase BT (A) |
|---|---|---|---|---|---|
| Tap 1 (+10%) | 151.800 | 152,1 | 87,8 | 669,4 | 669,4 |
| Tap 2 | 150.075 | 153,8 | 88,8 | 669,4 | 669,4 |
| Tap 3 | 148.350 | 155,6 | 89,8 | 669,4 | 669,4 |
| Tap 4 | 146.625 | 157,4 | 90,9 | 669,4 | 669,4 |
| Tap 5 | 144.900 | 159,3 | 92,0 | 669,4 | 669,4 |
| Tap 6 | 143.175 | 161,2 | 93,0 | 669,4 | 669,4 |
| Tap 7 | 141.450 | 163,2 | 94,2 | 669,4 | 669,4 |
| Tap 8 | 139.725 | 165,2 | 95,4 | 669,4 | 669,4 |
| **Tap 9 (nominal)** | **138.000** | **167,4** | **96,6** | **669,4** | **669,4** |
| Tap 10 | 136.275 | 169,6 | 97,9 | 669,4 | 669,4 |
| Tap 11 | 134.550 | 171,9 | 99,2 | 669,4 | 669,4 |
| Tap 12 | 132.825 | 174,2 | 100,6 | 669,4 | 669,4 |
| Tap 13 | 131.100 | 176,6 | 102,0 | 669,4 | 669,4 |
| Tap 14 | 129.375 | 179,1 | 103,4 | 669,4 | 669,4 |
| Tap 15 | 127.650 | 181,6 | 104,8 | 669,4 | 669,4 |
| Tap 16 | 125.925 | 184,2 | 106,4 | 669,4 | 669,4 |
| **Tap 17 (−10%)** | **124.200** | **185,9** | **107,4** | **669,4** | **669,4** |

> Tensão por tap = 138.000 − (n−9) × 1.725 V, onde n = número do tap (1 a 17)
> I_linha_AT = 40.000.000 / (√3 × V_tap) | I_fase_AT = I_linha / √3

A variação de corrente na AT ao longo dos taps é de **152,1 A (Tap 1) a 185,9 A (Tap 17)** — uma diferença de **+22,2%** entre o tap mais leve e o mais carregado para o condutor AT.

---

## 5. Verificação da Seção e Densidade de Corrente

A densidade de corrente J = I_fase / A_total confirma que os condutores foram dimensionados para a **corrente máxima de fase** (condição pior de tap).

### BT1 — CTC WEG

| Parâmetro | Valor | Fonte |
|---|---|---|
| Tipo de condutor | CTC WEG (Cabo Transposto Continuamente) | Folha 1, L32 |
| Dimensão de cada subcond. (axial × radial) | 4,7 × 1,4 mm — 13 subcondutores | Folha 1, L37 |
| Cabos em paralelo (axial × radial) | 1 × 2 | Folha 1, L39 |
| Seção total (mm²) | 165,5 | Folha 1, L40 |
| Corrente de fase | 669,4 A | Folha 1, L21 |
| **Densidade calculada** | 669,4 / 165,5 = **4,045 A/mm²** | — |
| Densidade declarada | 4,045 A/mm² | Folha 1, L41 ✓ |

**Seção por CTC (verificação):**
```
Seção 1 subcond. = 4,7 × 1,4 = 6,58 mm²
Seção 1 CTC = 13 × 6,58 = 85,5 mm²  (valor nominal, antes dos arredondamentos de fabricação)
2 CTCs em paralelo: 2 × 85,5 = 171 mm² → valor EPA arredondado: 165,5 mm²
(diferença absorvida pelos raios de canto e arredondamentos do CTC)
```

### AT1 — Condutor Retangular

| Parâmetro | Valor | Fonte |
|---|---|---|
| Tipo de condutor | Retangular isolado | Folha 1, L32 |
| Dimensão (axial × radial) | 6,8 × 1,9 mm | Folha 1, L37 |
| Condutores em paralelo (axial × radial) | 1 × 2 | Folha 1, L39 |
| Seção total (mm²) | 25,11 | Folha 1, L40 |
| Corrente de fase (máx.) | 107,4 A | Folha 1, L21 |
| **Densidade calculada** | 107,4 / 25,11 = **4,277 A/mm²** | — |
| Densidade declarada | 4,275 A/mm² | Folha 1, L41 ✓ |

```
Seção 1 condutor = 6,8 × 1,9 = 12,92 mm²
2 em paralelo = 25,84 mm²  →  EPA: 25,11 mm²
(diferença por raios de canto do condutor retangular)
```

### AT2 — Condutor Retangular (Enrolamento de Regulação)

| Parâmetro | Valor | Fonte |
|---|---|---|
| Tipo de condutor | Retangular isolado | Folha 1, L32 |
| Dimensão (axial × radial) | 4,2 × 8,5 mm | Folha 1, L37 |
| Condutores em paralelo | 1 × 1 | Folha 1, L39 |
| Seção total (mm²) | 34,84 | Folha 1, L40 |
| Corrente de fase (máx.) | 107,4 A | Folha 1, L21 |
| **Densidade calculada** | 107,4 / 34,84 = **3,083 A/mm²** | — |
| Densidade declarada | 3,081 A/mm² | Folha 1, L41 ✓ |

```
Seção 1 condutor = 4,2 × 8,5 = 35,7 mm²  →  EPA: 34,84 mm²
```

### Por que o AT2 tem densidade menor que o AT1?

AT1 e AT2 conduzem a mesma corrente de fase (107,4 A), mas o AT2 usa um condutor único mais largo (34,84 mm²) enquanto o AT1 usa dois condutores menores em paralelo (25,11 mm² total).

O AT2 é o **enrolamento de regulação** — suas espiras são chaveadas pelo comutador de tap durante a operação (em OLTC) ou em parada (em DETC). Por operar em uma região sujeita a esforços mecânicos e elétricos adicionais do comutador, o projeto usa um condutor único de maior seção, que oferece:
- **Maior rigidez mecânica** por espira (importante para resistir aos esforços de comutação)
- **Menor densidade** (3,08 vs. 4,28 A/mm²) → condutor mais frio → maior margem térmica na região de comutação

---

## 6. Correntes para ONAN (32.000 kVA)

| Condição | I linha AT (A) | I fase AT (A) | I linha BT (A) | I fase BT (A) |
|---|---|---|---|---|
| Tap 1 (151.800 V) | 121,7 | 70,3 | 535,5 | 535,5 |
| **Tap 9 — nominal (138.000 V)** | **133,9** | **77,3** | **535,5** | **535,5** |
| Tap 17 (124.200 V) | **148,7** | **85,9** | **535,5** | **535,5** |

```
I_AT_ONAN_max = 32.000.000 / (√3 × 124.200) = 148,7 A   (tap 17, pior caso)
I_BT_ONAN    = 32.000.000 / (√3 × 34.500)  = 535,5 A   (constante)
```

O condutor é dimensionado para ONAF (185,9 A e 669,4 A) — em ONAN os condutores operam folgados.

---

## 7. Por que a corrente máxima é o critério de projeto — Aplicações práticas

### 7.1 Dimensionamento do condutor (seção mínima)

O condutor deve operar sem superaquecimento em qualquer condição prevista de tap e potência. Se fosse dimensionado apenas para o tap nominal:

```
Seção mínima com J_max = 4,275 A/mm²:

Com I_nominal (167,4 A):  A_min = 167,4 / 4,275 = 39,2 mm²  → subestimado
Com I_máxima  (185,9 A):  A_min = 185,9 / 4,275 = 43,5 mm²  → correto
```

Um condutor dimensionado para a corrente nominal esquentaria além do limite de projeto ao operar no Tap 17, reduzindo a vida útil da isolação de papel.

### 7.2 Cálculo das perdas resistivas

As perdas resistivas crescem com I²:

```
Perdas ∝ I²:
  Tap 9  (167,4 A): fator = 167,4² = 28.023
  Tap 17 (185,9 A): fator = 185,9² = 34.559  → +23,3% mais perdas que no tap nominal
```

Por isso as perdas em carga são declaradas separadamente para cada condição de tap no [[CORE]] (seção 9) — a maior perda total ocorre no Tap 17 (Pcc calculada = 195.111 W).

### 7.3 Dimensionamento do sistema de proteção

Os relés de sobrecorrente e diferenciais são ajustados com base na corrente máxima de operação, não na nominal:

```
Corrente de pickup do relé de sobrecorrente BT:
  Tipicamente ajustado em 1,2 × I_max = 1,2 × 669,4 = 803,3 A

Corrente de operação do diferencial:
  Corrente de restrição calculada com base em I_linha_max = 185,9 A (AT) e 669,4 A (BT)
  A relação de transformação usada no diferencial deve considerar os taps extremos
  para evitar operação indevida.
```

### 7.4 Bitola dos cabos externos de ligação (barramento)

Os barramentos e cabos que conectam o transformador ao disjuntor e às barras de alta e baixa tensão devem ser dimensionados para as correntes máximas:

```
Barramento AT: ≥ 185,9 A  (corrente de linha máxima AT)
Barramento BT: ≥ 669,4 A  (corrente de linha BT — constante)
```

---

## 8. Resumo Visual das Correntes

```
                        DELTA (AT)              ESTRELA (BT)
                   ┌──────────────────┐    ┌──────────────────┐
                   │  I_linha = 185,9 A│    │  I_linha = 669,4 A│
                   │  I_fase  = 107,4 A│    │  I_fase  = 669,4 A│
                   │  (Tap 17 — pior) │    │  (qualquer tap)  │
                   └──────────────────┘    └──────────────────┘
                          AT1 / AT2                  BT1
                        Seção: 25,11 /           Seção: 165,5 mm²
                               34,84 mm²          J: 4,045 A/mm²
                        J: 4,275 / 3,081 A/mm²
```

---

*← [[CORE]] | Voltar ao arquivo principal do transformador ADA DATA CENTER*
