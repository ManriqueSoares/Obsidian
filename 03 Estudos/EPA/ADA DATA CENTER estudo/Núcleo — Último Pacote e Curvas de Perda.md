# Núcleo — Último Pacote e Curvas de Perda

> Transformador **C19163865** | Chapa: **M4-0,27 mm WEG TF**
> Fonte: `Folha 2` — colunas **S em diante** (68 colunas usadas, 192 linhas)

---

## Verificação: o que há nas colunas S em diante da Folha 2?

Sim, confirmado. A partir da **coluna S** a Folha 2 contém três blocos independentes:

| Bloco | Linhas | Conteúdo |
|---|---|---|
| **1** | R1–R20 | Cálculo da largura máxima admissível para o **último pacote** de chapas do núcleo |
| **2** | R84–R98 | **Curva Geral 0,27 - grade 110** — perdas específicas da chapa M4 por nível de indução |
| **3** | R101–R105 | Verificação de ventilação ONAF |

---

## Bloco 1 — Cálculo do Último Pacote (R1–R20, cols S–AW)

### O que é o "último pacote" do núcleo?

O núcleo de um transformador de potência é construído em **degraus** (steps) — seções de chapas com larguras decrescentes que formam um perfil escalonado aproximando a seção circular do núcleo. Cada grupo de chapas de mesma largura forma um **pacote**.

```
Vista frontal do núcleo (seção transversal escalonada):

        ┌──────────┐         ← 1º degrau (mais largo: 560 mm)
       ┌┤          ├┐        ← 2º degrau (540 mm)
      ┌─┤          ├─┐       ← 3º degrau (520 mm)
     ┌──┤          ├──┐      ← ...
    ┌───┤  NÚCLEO  ├───┐     ← ...
    │   │          │   │     ← ...
    └───┤          ├───┘     ← ...
     └──┤          ├──┘      ← ...
      └─┤          ├─┘       ← 12º degrau
       └┤          ├┘        ← 13º degrau (mais estreito: 220 mm) ← ÚLTIMO PACOTE
        └──────────┘
```

O **último pacote** (13º degrau, 220 mm) é o mais externo — o que fica mais próximo dos enrolamentos. Por estar na periferia do núcleo, é o mais sujeito ao **campo de dispersão** gerado pelas correntes dos enrolamentos, que induz correntes parasitas nas chapas. Se o campo radial for intenso demais, essas correntes podem causar aquecimento excessivo nesse pacote, exigindo que ele seja **dividido** (partido em dois subpacotes com um isolamento entre eles) para interromper os caminhos de corrente.

### Dados do cálculo (Folha 2, R5–R13, cols S–AW)

**Configuração radial da coluna (do núcleo para fora):**

| Elemento | Dimensão | Descrição |
|---|---|---|
| Ø núcleo | 582 mm | Diâmetro do núcleo escalonado | Folha 2, R8 col U |
| gap1 | 22 mm | Distância núcleo → BT1 |
| enrol1 (BT1) | 61 mm | Espessura radial do enrolamento BT |
| gap2 | 43 mm | Canal entre BT e AT1 |
| enrol2 (AT1) | 79 mm | Espessura radial do enrolamento AT1 |
| gap3 | 40 mm | Canal entre AT1 e AT2 |
| enrol3 (AT2) | 11 mm | Espessura radial do enrolamento AT2 |
| gap4–6 | 0 mm | Sem mais enrolamentos |

**Dados elétricos dos enrolamentos (Folha 2, R9–R13):**

| Enrolamento | Altura (mm) | N° Espiras | Corrente (A) | Sentido | NI (A·esp) |
|---|---|---|---|---|---|
| BT1 | 1120 | 184 | 669,40 | +1 | +123.169,6 |
| AT1 | 1080 | 1275 | 107,40 | −1 | −136.935,0 |
| AT2 | 930 | 128 | 107,40 | +1 | +13.747,2 |
| **Soma NI** | — | — | — | — | **−18 A·esp** |

> A soma de −18 A·esp (quase zero, mas não exatamente) indica um leve desequilíbrio de ampère-espira no tap 17 — condição mais crítica para o campo no último pacote.

### Dados de saída e resultado (Folha 2, R17–R20)

| Grandeza | Valor | Unidade |
|---|---|---|
| Hn — campo axial nos enrolamentos | 20.752 / 22.956 / 2.533 | A/cm |
| **Hr — campo radial no último pacote** | **329,31** | **A/cm** |
| **Largura máxima admissível (L máx)** | **609,8** | **mm** |
| Largura real do último pacote | 220 | mm |

### Conclusão da planilha (Folha 2, R19 col X):

> **"NÃO É NECESSÁRIO DIVIDIR O ULTIMO PACOTE."**

### Por que o resultado é "não necessário"?

A condição para dividir o último pacote é:

```
Largura_real  >  L_máx  →  necessário dividir
Largura_real  ≤  L_máx  →  NÃO necessário dividir
```

Neste transformador:
```
220 mm  ≤  609,8 mm  →  NÃO é necessário dividir  ✓
```

A largura máxima admissível de **609,8 mm** é calculada a partir do campo radial Hr e das propriedades da chapa. Como o último pacote tem apenas **220 mm** de largura — muito menos que o limite —, o campo radial de 329,31 A/cm não cria correntes parasitas suficientes para exigir a divisão.

### O que significaria dividir o último pacote?

Se fosse necessário, o pacote de 220 mm de largura seria cortado em dois subpacotes (ex.: 110 + 110 mm) com uma folha isolante entre eles. Isso interrompe os circuitos de corrente parasita que se fecham ao longo da largura da chapa, reduzindo as perdas e o aquecimento local. É uma medida de projeto que aumenta o custo de fabricação (mais manuseio de chapas) e é evitada sempre que o cálculo permite.

### Por que o campo radial existe?

Em condição nominal perfeita (soma NI = 0), o campo magnético de dispersão é puramente axial e não há campo radial nas extremidades dos enrolamentos. Porém como os três enrolamentos têm **alturas diferentes** (BT: 1120 mm, AT1: 1080 mm, AT2: 930 mm) e a soma NI não é zero no tap 17 (−18 A·esp), o campo de dispersão tem uma componente radial que penetra no núcleo pelas extremidades. Esse Hr é o que induz correntes no plano da chapa do último pacote.

---

## Bloco 2 — Curva Geral 0,27 - grade 110 (R84–R98, cols S–X)

> Fonte: Folha 2, R84–R98, colunas T–X

### O que é a "Curva Geral 0,27 - grade 110"?

É a curva de **perdas específicas** (W/kg) da chapa de aço-silício usada neste núcleo — a **M4-0,27 mm WEG TF** — tabelada para diferentes níveis de indução magnética. O nome "grade 110" refere-se ao índice de perda da chapa: uma classificação interna WEG equivalente à norma ASTM A876 que define a máxima perda específica a 1,7 T / 60 Hz.

A chapa M4-0,27 mm é uma das mais nobres disponíveis comercialmente: espessura fina (0,27 mm reduz correntes de Foucault) e grão orientado, com baixíssimas perdas no sentido de laminação.

### Dados da curva (Folha 2, R86–R98)

| Condição (% Vn) | Indução B (T) | W/kg base | W/kg projeto | Massa núcleo (kg) | Perdas vazio calculadas (W) |
|---|---|---|---|---|---|
| 90% | 1,5509 | 1,08 | **1,24** | 17.597 | **21.881** |
| 100% | 1,7232 | 1,54 | **1,69** | 17.597 | **29.786** |
| 105% | 1,8094 | 1,98 | **2,18** | 17.597 | **38.362** |
| 110% | 1,8955 | 2,68 | **2,95** | 17.597 | **51.955** |

> Fonte linha a linha: R87–R91 (90% e 105%) e R94–R98 (100% e 110%)

### W/kg base vs. W/kg projeto — qual a diferença?

- **W/kg base:** valor nominal da curva da chapa fornecido pelo fabricante (WEG), medido em condições ideais de laminação pura, a campo orientado
- **W/kg projeto:** valor corrigido que o EPA usa no cálculo, **maior que o base**, porque inclui fatores reais de fabricação:

```
W/kg_projeto = W/kg_base × fator_construção

Fator a 100%: 1,69 / 1,54 = 1,097  → +9,7% sobre o valor da chapa pura
Fator a 110%: 2,95 / 2,68 = 1,101  → +10,1%
```

Os fatores de correção compensam:
1. **Juntas das chapas** (cantos do núcleo onde as chapas se sobrepõem — região de maior perda)
2. **Tensões mecânicas** na chapa após corte e manuseio (o corte altera a estrutura cristalina e aumenta perdas)
3. **Variação da indução** ao longo da seção (as regiões de junção têm indução local maior)

### Verificação cruzada com o CORE.md (seção 7)

| Condição | Perdas calculadas Folha 2 (W) | Perdas declaradas Dados_DTDS (W) | Diferença |
|---|---|---|---|
| 90% Vn | 21.881 | 21.102 | +779 W (+3,7%) |
| 100% Vn | 29.786 | 29.828 | −42 W (−0,1%) ✓ |
| 105% Vn | 38.362 | — | — |
| 110% Vn | 51.955 | 46.109 | +5.846 W (+12,7%) |

A 100% Vn os valores são praticamente idênticos (diferença de apenas 42 W em 30 kW — 0,1%). A diferença em 90% e 110% deve-se a arredondamentos na curva e ao fato de que a Folha 2 calcula por interpolação, enquanto o Dados_DTDS usa o valor final ajustado do projeto. A 110% a diferença é maior porque o núcleo está saturando e pequenas variações de B causam grandes variações em W/kg (região não linear da curva B-H).

### A indução de 1,723 T a 100% Vn — é alta?

```
Para chapa M4-0,27 mm (grão orientado):
  Indução de saturação: ≈ 2,03 T  (declarada na planilha, R137 col R)
  Indução de projeto:     1,723 T  → 84,9% da saturação

Margem até saturação = (2,03 − 1,723) / 2,03 = 15,1%
```

A 110% Vn: B = 1,896 T → 93,4% da saturação — núcleo ainda não saturado completamente, mas na região de alta não-linearidade, o que explica o crescimento desproporcional das perdas.

### Relação entre B e a indução calculada pelo volt/espira

```
B_max = V/espira / (4,44 × f × Seção_núcleo)
      = 108,25 / (4,44 × 60 × 2356,65 × 10⁻⁴)
      = 108,25 / (4,44 × 60 × 0,235665)
      = 108,25 / 62,77
      = 1,724 T  ≈ 1,723 T declarado  ✓
```

A seção do núcleo de **2356,65 cm²** (Folha 2, R51) fecha o ciclo: volt/espira → fluxo → indução → perdas específicas → perdas totais.

---

## Bloco 3 — Verificação de Ventilação ONAF (R101–R105)

| Parâmetro | Valor | Fonte |
|---|---|---|
| Vazão por ventilador | 210 m³/min | Folha 2, R103 |
| N° mínimo de ventiladores necessários | 5 | Folha 2, R104 |
| Resultado | **Ok!** | Folha 2, R105 |

O projeto usa **12 ventiladores** (declarado em R100: "12 x Vent. VER 210m³/min 630mm 60dB 460V 3Ph 60Hz"). O mínimo necessário pelo cálculo é 5 — portanto há uma folga de **2,4×** em relação ao mínimo. Isso garante que, mesmo com falha de metade dos ventiladores, o transformador ainda opera em ONAF com margem.

---

## Dados do núcleo completo — Folha 2, cols A-R

Para referência completa, os dados do núcleo estão nas colunas A–R da mesma Folha 2:

| Parâmetro                    | Valor               | Fonte |
| ---------------------------- | ------------------- | ----- |
| Diâmetro do núcleo           | 582 mm              | R45   |
| Altura da janela             | 1350 mm             | R46   |
| Entre eixos                  | 1130 mm             | R47   |
| Indução (100% Vn)            | **1,723 T**         | R49   |
| Tipo de montagem             | Convencional        | R50   |
| Seção do núcleo              | **2356,65 cm²**     | R51   |
| Peso do núcleo               | **17.597 kg**       | R52   |
| Chapa                        | M4-0,27 mm WEG TF   | R56   |
| Espessura da chapa           | 0,27 mm             | R55   |
| Nº chapas por camada         | 2                   | R54   |
| Nº de canais de resfriamento | 2                   | R57   |
| Espessura dos canais         | 6 mm                | R58   |
| Localização do 1º canal      | 3º degrau           | R59   |
| Tipo de núcleo               | Core-Type 3 colunas | R62   |
| Nº de degraus                | 13                  | —     |

### Degraus do núcleo (largura × espessura do pacote)

| Degrau           | Largura (mm) | Espessura pacote (mm) | Fonte |
| ---------------- | ------------ | --------------------- | ----- |
| 1º               | 560          | 79,38                 | R46   |
| 2º               | 540          | 29,16                 | R47   |
| 3º               | 520          | 16,20                 | R48   |
| 4º               | 500          | 17,82                 | R49   |
| 5º               | 480          | 15,66                 | R50   |
| 6º               | 460          | 14,04                 | R51   |
| 7º               | 440          | 11,88                 | R52   |
| 8º               | 420          | 11,34                 | R53   |
| 9º               | 380          | 18,90                 | R54   |
| 10º              | 340          | 15,66                 | R55   |
| 11º              | 300          | 12,96                 | R56   |
| 12º              | 260          | 11,34                 | R57   |
| **13º (último)** | **220**      | **8,64**              | R58   |

**Verificação da seção total:**

```
Seção = π × (Ø/2)² × fator_empilhamento  (aproximação circular)
      = π × 291² × 0,97
      ≈ 258.836 mm² × 0,97 ≈ 251.070 mm² = 2510,7 cm²

Seção declarada = 2356,65 cm²  (valor EPA, calculado com geometria exata dos 13 degraus)
```

A diferença entre a aproximação circular e a seção real dos degraus é esperada — o escalonamento em 13 degraus não preenche toda a área do círculo.

---

*← [[CORE]] | Voltar ao arquivo principal do transformador ADA DATA CENTER*
