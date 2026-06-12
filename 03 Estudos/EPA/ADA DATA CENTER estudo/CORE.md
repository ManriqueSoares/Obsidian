# CORE — Transformador ADA DATA CENTER

> **ID:** C19163865 | **Norma:** ABNT NBR 5356/2007 | **Autor EPA:** luissouza | **Data:** 09/04/2026
> **Arquivo-fonte:** `Cópia de C19163865.xlsm` — aba **Dados_DTDS**, coluna G contém os valores

---

## 1. Identificação Geral

| Parâmetro | Valor | Fonte (Dados_DTDS) |
|---|---|---|
| Cliente | ADA DATA CENTER | L6 |
| ID do Transformador | 19163865 | L2 |
| Número de Fases | 3 | L7 |
| Frequência | 60 Hz | L9 |
| Altitude de Instalação | < 1000 m | L8 |
| Temperatura Ambiente Máxima | 40 °C | L10 |
| Tipo de Óleo | Aceite Mineral Nafténico | L123 |

### Funcionamento físico — Parâmetros de identificação

**Número de fases: 3**
O sistema trifásico é universal em transmissão e distribuição de energia porque transmite 3× a potência de um sistema monofásico com apenas √3 vezes mais condutores (vs. 3×), reduzindo custo e perdas. Para um transformador de 40 MVA, o monofásico equivalente teria que suportar 40 MVA em uma única bobina — inviável para transporte e manutenção. O trifásico divide a potência em três colunas do núcleo, reduzindo as dimensões de cada enrolamento.

**Frequência: 60 Hz**
O Brasil adota 60 Hz (padrão americano). A frequência impacta diretamente o projeto:
- **Núcleo:** fluxo máximo Φ = V / (4,44 × f × N) — com 60 Hz, o núcleo precisa de menos espiras ou menor seção para a mesma tensão do que em 50 Hz, mas as perdas por correntes parasitas crescem com f²
- **Reatância de dispersão:** X = 2π × f × L — em 60 Hz, X é 20% maior que em 50 Hz para a mesma indutância, elevando a impedância de curto-circuito
- **Ruído:** a frequência fundamental do ruído do núcleo é 2 × 60 = **120 Hz**

**Altitude: < 1000 m**
A altitude afeta dois aspectos críticos do transformador:

*Isolamento:* o ar rarefeito em altitudes elevadas tem menor rigidez dielétrica. Acima de 1000 m, a NBR 5356 exige correção dos níveis de isolação (aumento do BIL e das distâncias de escoamento nos buchas). Como este transformador opera abaixo de 1000 m, **nenhuma correção é necessária** — os valores de BIL da seção 6 são aplicados diretamente sem fator de altitude.

*Resfriamento:* ar menos denso reduz a eficiência do resfriamento ONAF. Acima de 1000 m, a potência ONAF garantida seria derrubada. Abaixo de 1000 m, os valores de 32/40 MVA valem integralmente.

**Temperatura ambiente máxima: 40 °C**
Este não é necessariamente a temperatura real do local de instalação — é o valor **normativo máximo** definido pela NBR 5356 para transformadores de uso geral. Ele entra diretamente no balanço térmico da seção 2:
```
T_hot-spot = T_ambiente + ΔT_óleo + ΔT_gradiente = 40 + 55 + 10 = 105 °C
```
Se a temperatura real do data center for menor (ex.: 25 °C com ar-condicionado no ambiente do transformador), o transformador operará com margem térmica e maior vida útil. Se ultrapassar 40 °C, os limites garantidos de elevação são violados.

**Tipo de óleo: Aceite Mineral Nafténico**
O óleo mineral tem duas origens: **parafínico** (predominantemente parafinas de cadeia longa) e **nafténico** (predominantemente hidrocarbonetos cíclicos — naftenicos). O nafténico é o padrão de mercado para transformadores de potência no Brasil pela WEG e outras fabricantes, pelos seguintes motivos:

| Propriedade | Nafténico | Parafínico |
|---|---|---|
| Ponto de fluidez | Muito baixo (≈ −40 °C) | Mais alto (pode solidificar em frio) |
| Solubilidade de parafinas | Alta (não forma depósitos) | Menor (pode precipitar cera) |
| Envelhecimento com papel | Compatível e bem estudado | Similar |
| Disponibilidade no Brasil | Alta | Menor |

O óleo atua simultaneamente como **isolante** (rigidez dielétrica ≥ 30 kV/2,5 mm) e como **fluido de resfriamento** (transfere calor dos enrolamentos para os radiadores por convecção).

---

## 2. Classe de Temperatura e Elevações

| Parâmetro | Valor | Fonte |
|---|---|---|
| Classe de temperatura | 105 °C (A) | L11 |
| Elevação — Enrolamentos (garantido) | 55 °C | L12 |
| Elevação — Topo do óleo (garantido) | 55 °C | L13 |
| Elevação — Hot-spot (garantido) | 65 °C | L14 |
| Temperatura de referência (perdas) | 75 °C | L15 |

### Funcionamento físico — Classe de temperatura

A **classe de temperatura** define o limite máximo de temperatura que a isolação do transformador pode suportar sem degradação acelerada. A classe **105 °C (A)** significa que o ponto mais quente do enrolamento (*hot-spot*) não deve ultrapassar 105 °C em operação contínua.

**Balanço térmico:**

```
T_hot-spot = T_ambiente + ΔT_topo_óleo + ΔT_hot-spot_acima_do_óleo
```

Substituindo com os valores garantidos:
```
T_hot-spot_max = 40 + 55 + (65 − 55) = 40 + 55 + 10 = 105 °C  ← exatamente o limite da classe
```

> A diferença de 10 °C entre o hot-spot e o topo do óleo é o **gradiente** dentro do enrolamento. O óleo se aquece por convecção, mas o ponto mais quente do condutor sempre fica alguns graus acima do óleo local.

A **temperatura de referência de 75 °C** (L15) é usada como base de cálculo das perdas em carga, pois é a temperatura média esperada dos enrolamentos em regime permanente à plena carga (conforme NBR 5356).

**Regra de vida útil (Montsinger):** Para cada 6–8 °C de aumento permanente acima do hot-spot de referência, a vida útil da isolação de papel é reduzida à metade.

---

## 3. Potências de Operação

| Modo de Resfriamento | Potência (kVA) | Fonte |
|---|---|---|
| ONAN | 32.000 | L17 |
| ONAF1 | 40.000 | L18 |

### Funcionamento físico — Modos de resfriamento

- **ONAN** *(Oil Natural Air Natural)*: o óleo circula por convecção natural dentro do tanque; o calor é dissipado pelos radiadores por convecção natural do ar externo. Modo silencioso, sem equipamentos auxiliares.
- **ONAF** *(Oil Natural Air Forced)*: mantém a convecção natural do óleo, mas adiciona ventiladores nos radiadores, aumentando o coeficiente de troca térmica do lado do ar. Isso permite aumentar a potência de **32 para 40 MVA (+25%)** sem alterar a parte ativa.

A transição ONAN → ONAF normalmente ocorre de forma automática quando a temperatura do óleo atinge um setpoint (ex.: 55 °C de topo de óleo).

### Correntes nominais calculadas

Para **ONAF (40.000 kVA)** — condição de projeto:

$$I_{AT} = \frac{S}{\sqrt{3} \times V_{AT}} = \frac{40.000.000}{\sqrt{3} \times 138.000} = \frac{40.000.000}{239.002} \approx \mathbf{167,4\ A}$$

$$I_{BT} = \frac{S}{\sqrt{3} \times V_{BT}} = \frac{40.000.000}{\sqrt{3} \times 34.500} = \frac{40.000.000}{59.763} \approx \mathbf{669,5\ A}$$

Para **ONAN (32.000 kVA)**:

$$I_{AT} = \frac{32.000.000}{239.002} \approx \mathbf{133,9\ A} \qquad I_{BT} = \frac{32.000.000}{59.763} \approx \mathbf{535,6\ A}$$

> **Atenção:** estes valores são para o tap nominal (138 kV). A **corrente máxima da AT** ocorre no tap mínimo (124,2 kV) e é **185,9 A** — critério real de dimensionamento do condutor. Ver [[Correntes Máximas]] para análise completa por tap, corrente de fase vs. linha, densidades de corrente e verificação dos condutores.

---

## 4. Tensões e Regulação

### 4.1 AT (Alta Tensão)

| Parâmetro | Valor | Fonte |
|---|---|---|
| Tensão nominal (tap central, Tap 9) | 138.000 V | L20 |
| Tap máximo (Tap 1, +10%) | 151.800 V | L83 |
| Tap mínimo (Tap 17, −10%) | 124.200 V | L97 |
| Regulação positiva | 8 × 1,25% | L21 |
| Regulação negativa | 8 × 1,25% | L22 |

**Verificação dos taps:**

```
Tap positivo máximo = 138.000 × (1 + 8 × 0,0125) = 138.000 × 1,10 = 151.800 V  ✓
Tap negativo máximo = 138.000 × (1 − 8 × 0,0125) = 138.000 × 0,90 = 124.200 V  ✓
Passo por tap = 138.000 × 0,0125 = 1.725 V/tap
Total de posições = 8 + 1 + 8 = 17 taps
```

### 4.2 BT (Baixa Tensão)

| Parâmetro | Valor | Fonte |
|---|---|---|
| Tensão nominal BT1 | 34.500 V | L33 |

### Funcionamento físico — Regulação por tap

O comutador de tap (DETC ou OLTC) altera o **número de espiras ativas** no enrolamento AT. Mais espiras → maior relação de transformação → tensão BT cai; menos espiras → menor relação → tensão BT sobe. A tensão BT permanece fixa; o que muda é quantas espiras da AT são usadas.

**Relação de transformação por condição:**

Para um transformador Dyn1 a relação entre tensões de linha é direta:

```
a_Tap1  = 151.800 / 34.500 = 4,400
a_Tap9  = 138.000 / 34.500 = 4,000  ← nominal
a_Tap17 = 124.200 / 34.500 = 3,600
```

**Tensões de fase** (relevantes para o dimensionamento do enrolamento):

- AT em delta → tensão de fase = tensão de linha = **138.000 V**
- BT em estrela → tensão de fase = V_linha / √3 = 34.500 / 1,732 = **19.919 V**

**Relação de espiras real** (fase a fase):
```
a_fase = 138.000 / 19.919 = 6,927
```

### 4.3 Volt por espira

| Parâmetro       | Valor        | Fonte |
| --------------- | ------------ | ----- |
| Volt por espira | 108,25 V/esp | L120  |

**Cálculo e verificação:**

O volt/espira é a FEM induzida por espira, calculada pela lei de Faraday:

$$e = 4{,}44 \times f \times N \times \Phi_{max} \implies \frac{e}{N} = 4{,}44 \times f \times \Phi_{max}$$

```
Φ_max = 108,25 / (4,44 × 60) = 108,25 / 266,4 = 0,4063 Wb
```

**Estimativa do número de espiras:**

```
N_AT (delta) = V_fase_AT / (V/esp) = 138.000 / 108,25 ≈ 1.275 espiras
N_BT (estrela) = V_fase_BT / (V/esp) = 19.919 / 108,25 ≈  184 espiras
```


---

## 5. Grupo de Ligação e Diagrama Fasorial

| Parâmetro | Valor | Fonte |
|---|---|---|
| Grupo de Ligação | Dyn1 | L16 |

| Enrolamento | Ligação | Neutro |
|---|---|---|
| AT | Delta (D) | Não |
| BT | Estrela (y) | Sim (n) |
| Defasagem | 1 × 30° = 30° de atraso | — |

### Funcionamento físico — Grupo de Ligação

O código **Dyn1** é lido assim:
- **D** → AT em delta (triângulo): cada bobina conecta entre dois terminais de linha; tensão de fase = tensão de linha
- **y** → BT em estrela: cada bobina conecta entre um terminal de linha e o ponto neutro; tensão de fase = V_linha / √3
- **n** → neutro da estrela acessível externamente (terminal N)
- **1** → índice horário: o vetor **U_BT** está **30° atrasado** em relação a **U_AT** (*U_BT* atrasa *U_AT* em 1 × 30°)

**Diagrama fasorial (Dyn1):**

```
AT — Delta (D):
          A
         / \
        /   \
       C─────B

Vetores AT:   U_AB (referência 0°)
              U_BC (−120°)
              U_CA (+120°)

BT — Estrela-n (yn):
         a
          \
     c────N────b

Vetores BT:   U_an (−30°)   ← 30° atrasado em relação a U_AB
              U_bn (−150°)
              U_cn (+90°)
```

**Por que Dyn1 é usado em redes de distribuição?**
A ligação delta na AT não cria caminho para correntes de sequência zero pelo lado da rede de AT (correntes de terceira harmônica circulam internamente no delta). A estrela na BT com neutro fornece o ponto de referência para cargas monofásicas e serve como aterramento do sistema de 34,5 kV.

---

## 6. Níveis de Isolação

→ [[Níveis de Isolação]] — AT (145 kV / BIL 650 kV), BT1 (36,2 kV / BIL 200 kV), Neutro BT (BIL 170 kV), ensaios e física completa.

---

## 7. Perdas em Vazio

| Condição | Calculada (W) | Garantida (W) | Fonte |
|---|---|---|---|
| 90% Vn | 21.102 | — | L66 |
| 100% Vn | 29.828 | **30.000** | L67 / L70 |
| 110% Vn | 46.109 | — | L68 |

### Funcionamento físico — Perdas no núcleo

As perdas em vazio ocorrem **exclusivamente no núcleo de aço-silício** e existem sempre que o transformador está energizado, independentemente da carga. São compostas por:

**1. Perdas por histerese** (Equação de Steinmetz):
$$P_h = K_h \times f \times B_{max}^{1{,}6}$$
Cada ciclo de magnetização e desmagnetização do aço percorre o laço de histerese, dissipando energia.

**2. Perdas por correntes parasitas (Foucault)**:
$$P_e = K_e \times f^2 \times B_{max}^2 \times t^2$$
onde *t* é a espessura da chapa. Por isso o núcleo é laminado em chapas finas (ex.: M4 – 0,27 mm) com revestimento isolante.

**Total:** $P_0 = P_h + P_e$

**Verificação da não-linearidade (saturação):**

```
Relação de perdas:
  P(90%) / P(100%) = 21.102 / 29.828 = 0,708   → esperado ≈ (0,9)^2 = 0,81 (linear seria este)
  P(110%) / P(100%) = 46.109 / 29.828 = 1,546   → esperado ≈ (1,1)^2 = 1,21 (linear)
```

O crescimento muito maior em 110% evidencia que o núcleo começa a **saturar** acima de 100% Vn, pois o aço-silício tem curva B-H não-linear. Na saturação, o campo *H* aumenta muito mais rápido que o fluxo *B*, ampliando as correntes de magnetização e as perdas.

**Margem garantida:**
```
Margem = P_garantida / P_calculada = 30.000 / 29.828 = 1,006 → +0,6% de folga
```

---

## 8. Corrente de Excitação

| Condição | Calculada (%) | Garantida (%) | Fonte |
|---|---|---|---|
| 90% Vn | 0,16 | — | L72 |
| 100% Vn | 0,30 | **0,50** | L73 / L76 |
| 110% Vn | 0,56 | — | L74 |

### Funcionamento físico — Corrente de excitação

A corrente de excitação I₀ é a corrente que o transformador consome em vazio para estabelecer o fluxo magnético no núcleo. É formada por duas componentes:

```
I₀ = √(I_mag² + I_perda²)
```

- **I_mag**: componente reativa, responsável por criar o fluxo — está 90° atrasada da tensão. É determinada pela curva B-H do aço.
- **I_perda**: componente ativa, responsável por suprir as perdas no ferro — está em fase com a tensão.

Em transformadores de potência bem projetados, I₀ é muito pequena (< 1%) porque o núcleo tem alta permeabilidade e baixas perdas.

**Corrente de excitação absoluta a 100% Vn (ONAF, 40 MVA):**

$$I_0 = \frac{I_{0\%}}{100} \times I_{n,AT} = \frac{0{,}30}{100} \times 167{,}4 = \mathbf{0{,}50\ A}$$

**Verificação do crescimento com tensão (saturação):**
```
I0(90%)  = 0,16%   | razão 90→100: 0,30/0,16 = 1,875×
I0(100%) = 0,30%   | razão 100→110: 0,56/0,30 = 1,867×
```

O crescimento quase dobra a cada 10% de aumento de tensão, confirmando entrada na região de saturação. Acima de 110% Vn, o crescimento seria exponencial.

---

## 9. Perdas em Carga

Base de cálculo: **40.000 kVA @ 75 °C**

### 9.1 Condição 1 — Tap 1 (151.800 / 34.500 V) — Fonte: L82–L88

| Parâmetro | Valor (W) |
|---|---|
| Perdas resistivas AT | 76.801 |
| Perdas resistivas BT | 67.805 |
| Perda em carga calculada | 157.458 |
| Perda garantida | — |

### 9.2 Condição 2 — Tap 9 / Nominal (138.000 / 34.500 V) — Fonte: L89–L95 ← **principal**

| Parâmetro | Valor (W) |
|---|---|
| Perdas resistivas AT | 85.580 |
| Perdas resistivas BT | 67.805 |
| Perda em carga calculada | 166.083 |
| **Perda em carga garantida** | **210.000** |

### 9.3 Condição 3 — Tap 17 (124.200 / 34.500 V) — Fonte: L96–L102

| Parâmetro | Valor (W) |
|---|---|
| Perdas resistivas AT | 114.728 |
| Perdas resistivas BT | 67.805 |
| Perda em carga calculada | 195.111 |
| Perda garantida | — |

### Funcionamento físico — Perdas em carga

As perdas em carga ocorrem apenas quando o transformador está carregado. São compostas por:

**1. Perdas resistivas (efeito Joule):**
$$P_{resistiva} = I^2 \times R \quad \text{(proporcional ao quadrado da corrente)}$$

**2. Perdas parasitas nos enrolamentos (stray losses):**
- **Axiais:** campo magnético de dispersão na direção axial induz correntes parasitas nos condutores — maiores em condutores de maior seção ou CTC (Continuously Transposed Cable).
- **Radiais:** campo de dispersão radial induz perdas menores.
- Essas perdas também são proporcionais a I² mas dependem da geometria e frequência.

**Conferência da condição 2 (nominal):**
```
P_total_calculada = P_AT + P_BT = 85.580 + 67.805 = 153.385 W (resistivas)
P_parasitas ≈ 166.083 − 153.385 = 12.698 W (perdas parasitas nos enrolamentos)
```

**Por que as perdas resistivas AT aumentam com taps negativos?**

No tap 1 (151,8 kV), o número de espiras da AT é maior, portanto a corrente por espira é menor. No tap 17 (124,2 kV), menos espiras estão em uso, mas a corrente de fase permanece a mesma — a corrente por espira é maior, aumentando as perdas Joule:

```
Tap 9:  P_AT = 85.580 W
Tap 17: P_AT = 114.728 W  → aumento de +34% por usar menos espiras com mesma corrente de carga
Tap 1:  P_AT =  76.801 W  → menor porque usa mais espiras, distribuindo melhor a corrente
```

**Margem garantida vs. calculada (condição nominal):**
```
Margem = P_garantida / P_calculada = 210.000 / 166.083 = 1,265 → +26,5% de folga
```

Essa margem de 26,5% é alta e reflete a garantia contratual — o transformador deve ser ensaiado e aprovado dentro desse valor.

---

## 10. Impedância de Curto-Circuito

Base: **40.000 kVA @ 75 °C** | Fonte: L103–L117

| Tap | Tensão AT / BT | Z calculada (%) | Z garantida (%) |
|---|---|---|---|
| Tap 1 | 151.800 / 34.500 V | 10,52 | — |
| **Tap 9 (nominal)** | **138.000 / 34.500 V** | **10,12** | **10,0** |
| Tap 17 | 124.200 / 34.500 V | 9,92 | — |

### Funcionamento físico — Impedância de curto-circuito

A impedância de curto-circuito representa a **queda de tensão interna** do transformador quando circula a corrente nominal. Fisicamente, é o resultado de dois componentes:

```
Z% = √(R%² + X%²)
```

**Componente resistiva (R%)** — calculada a partir das perdas em carga:
$$R\% = \frac{P_{cc}}{S_n} \times 100 = \frac{166.083}{40.000.000} \times 100 = \mathbf{0{,}415\%}\ \text{(calculado)}$$
$$R\% = \frac{210.000}{40.000.000} \times 100 = \mathbf{0{,}525\%}\ \text{(garantido)}$$

**Componente reativa (X%)** — dominante em transformadores de potência:
$$X\% = \sqrt{Z\%^2 - R\%^2} = \sqrt{10{,}12^2 - 0{,}415^2} = \sqrt{102{,}41 - 0{,}172} = \mathbf{10{,}11\%}\ \text{(calculado)}$$
$$X\%_{garantido} = \sqrt{10^2 - 0{,}525^2} = \sqrt{100 - 0{,}276} = \mathbf{9{,}99\%}$$

O X% é determinado pelo **fluxo de dispersão** (a fração do fluxo que não se fecha pelo núcleo e passa pelo espaço entre os enrolamentos). Quanto maior a distância AT-BT, maior o X%.

**Interpretação prática da Z%:**

- Z% = 10% significa: para circular a **corrente nominal** com o secundário em curto-circuito, é necessário aplicar apenas **10% da tensão nominal** no primário.
- Em curto-circuito com tensão plena: $I_{cc} = I_n / (Z\%/100) = I_n / 0{,}10 = 10 \times I_n$
- Corrente de curto-circuito AT: $I_{cc,AT} = 10 \times 167{,}4 = \mathbf{1.674\ A}$
- Corrente de curto-circuito BT: $I_{cc,BT} = 10 \times 669{,}5 = \mathbf{6.695\ A}$

**Regulação de tensão (fator de potência unitário, carga resistiva):**
$$\Delta V \approx R\% \cos\varphi + X\% \sin\varphi = 0{,}415 \times 1 + 10{,}11 \times 0 = \mathbf{0{,}415\%}$$

**Regulação (fp = 0,85 indutivo — carga típica de data center com UPS):**
$$\Delta V \approx 0{,}415 \times 0{,}85 + 10{,}11 \times 0{,}527 = 0{,}353 + 5{,}33 = \mathbf{5{,}68\%}$$

---

## 11. Nível de Ruído

| Condição | Distância | Calculado | Garantido | Fonte |
|---|---|---|---|---|
| ONAF | 2,0 m | 74,2 dB | 77 dB | L80 / L81 |

### Funcionamento físico — Ruído em transformadores

O ruído em transformadores tem duas origens principais:

**1. Ruído do núcleo (magnetostrição):** O aço-silício muda fisicamente de dimensão a cada semiciclo de magnetização — fenômeno chamado magnetostrição. Como ocorre em cada semiciclo positivo e negativo, a frequência fundamental do ruído é o **dobro da frequência da rede**: 2 × 60 = **120 Hz**, e seus harmônicos (240, 360 Hz…). A amplitude é proporcional à indução B — por isso núcleos projetados com indução mais baixa são mais silenciosos.

**2. Ruído dos ventiladores (ONAF):** Os motores e pás dos ventiladores geram ruído mecânico e aerodinâmico. Em ONAF, esse ruído domina sobre o do núcleo e eleva o nível total medido.

**Por que ONAN é medido a 0,3 m e ONAF a 2,0 m?**
Em ONAN, o ruído é baixo e se concentra na superfície do tanque; medir a 0,3 m captura o nível superficial do equipamento. Em ONAF, os ventiladores projetam ruído a distâncias maiores; a medição a 2,0 m representa melhor a exposição de pessoas ao redor. As posições são padronizadas pela NBR 5356 / IEC 60076-10 para cada modo de operação.

**O que significa 77 dB na prática?**

A escala dB é logarítmica — cada +10 dB representa 10× mais potência sonora (percebida como ~2× mais alto):

```
Referência auditiva comum (dBA ≈ dB para estas frequências):
  30 dB → biblioteca silenciosa
  60 dB → conversa normal
  75 dB → aspirador de pó a 1 m         ← próximo do garantido deste trafo
  77 dB → garantido ONAF a 2 m          ← este transformador
  85 dB → tráfego urbano intenso
  90 dB → limite NR-15 para 8h/dia sem EPI
```

**Aplicação — data center:**
Data centers têm o transformador geralmente em subestação fechada ou em área técnica externa. O nível de 77 dB a 2 m cai rapidamente com a distância:

```
Atenuação geométrica (campo livre): ΔL = 20 × log(d2/d1)
De 2 m para 10 m: ΔL = 20 × log(10/2) = 20 × 0,699 = 14 dB
→ A 10 m: 77 − 14 = 63 dB  (equivalente a uma conversa normal)
De 2 m para 20 m: ΔL = 20 × log(10) = 20 dB
→ A 20 m: 77 − 20 = 57 dB  (ambiente de escritório)
```

Paredes e barreiras acústicas da subestação reduzem adicionalmente 10–20 dB, tornando o ruído imperceptível nas áreas de trabalho adjacentes.

---

## 12. Inrush (Corrente de Energização)

| Parâmetro | Valor | Fonte |
|---|---|---|
| Corrente de inrush (pico) | 4,02 × In | L118 |

**Valor absoluto:**
```
I_inrush_pico = 4,02 × I_n,AT = 4,02 × 167,4 = 672,9 A  (na AT)
```

### Funcionamento físico — Corrente de inrush

Quando o transformador é energizado, o núcleo pode ter um **fluxo residual** da última desenergização. Se o fluxo residual tem a mesma polaridade que o fluxo aplicado pela tensão da rede, ambos se somam:

```
Φ_total = Φ_residual + Φ_aplicado
```

O núcleo pode atingir indução de 2 × Bmax_nominal, entrando em saturação profunda. Na saturação, a indutância do núcleo cai drasticamente, e a impedância do circuito é limitada apenas pela resistência do enrolamento — resultando em uma corrente de pico muito alta.

**Características do inrush:**
- Decai exponencialmente com a constante de tempo L/R (pode durar vários ciclos)
- Contém elevada componente de corrente contínua (componente CC) e harmônicos pares (2ª, 4ª harmônica)
- Os relés de proteção diferenciais usam o conteúdo de 2ª harmônica para distinguir inrush de curto-circuito

**Comparação com corrente de curto-circuito:**
```
I_cc_simetrica = 10 × In = 10 × 167,4 = 1.674 A
I_inrush_pico  = 4,02 × In = 672,9 A
→ Inrush é menor que o curto-circuito simétrico, mas dura ciclos vs. poucos ms
```

---

## 13. Parâmetros de Projeto Interno

| Parâmetro | Valor | Fonte |
|---|---|---|
| Anelão | 20,0 mm | L124 |
| Folga superior | 50 mm | L121 |
| Folga inferior | 0 mm | L122 |
| Distância entre fases | 36 mm | L119 |
| Volt por espira | 108,25 V/esp | L120 — ver [[#4.3 Volt por espira]] |

### Funcionamento físico — Parâmetros internos

**Anelão (20,0 mm)**
O anelão é o anel metálico (geralmente aço carbono ou inox) colocado sobre a culatra superior do núcleo, dentro da estrutura de prensagem. Sua função é distribuir uniformemente a força de prensagem sobre o pacote de chapas do núcleo.

Sem prensagem adequada, as chapas vibram na frequência de magnetostrição (120 Hz e harmônicos), gerando ruído excessivo e desgaste da isolação entre chapas. A espessura de 20 mm representa o anelão em si — a força total de prensagem que ele transmite é dimensionada em função do peso e área do núcleo (campo L125 na planilha, não preenchido nesta revisão).

**Folga superior: 50 mm | Folga inferior: 0 mm**
A "folga" é o espaço axial entre a extremidade dos enrolamentos e a culatra do núcleo (a parte horizontal que fecha o circuito magnético no topo e na base).

*Por que a folga inferior é zero?*
O enrolamento assenta diretamente sobre a base de suporte (cama inferior), sem espaço livre abaixo. Isso acontece porque:
1. O enrolamento é posicionado de baixo para cima durante a montagem — a cama inferior é a referência mecânica
2. Não há necessidade de canal de óleo na base quando o fluxo de óleo é dirigido (D) pela parte superior e lateral
3. Reduzir a janela ocupada na base permite usar todo o espaço disponível da janela do núcleo para os enrolamentos

*Por que a folga superior é 50 mm?*
O espaço de 50 mm entre o topo dos enrolamentos e a culatra superior serve para:
1. **Canal de óleo:** o óleo quente sobe por convecção e precisa de espaço para circular e sair em direção aos radiadores
2. **Margem de montagem:** acomoda tolerâncias de fabricação e a compressão do papelão isolante (presspan) durante a prensagem — a Folha 1 mostra que a redução na prensagem é de 4,7 mm no BT e 7,7 mm no AT, valores que afetam a folga final
3. **Isolamento culatra-enrolamento:** mantém a distância elétrica necessária entre o ponto de maior potencial do enrolamento AT e a culatra aterrada

**Distância entre fases: 36 mm**
É o espaço no óleo entre as bobinas de duas fases adjacentes (ex.: fase A e fase B). Esse espaço precisa suportar a tensão de impulso entre fases.

*Verificação da rigidez dielétrica no óleo:*
A tensão entre fases durante um impulso é proporcional à tensão de linha. Para a AT:

```
V_linha_AT_impulso ≈ BIL × √3 / √2  (tensão de fase → tensão de linha)
                   = 650 × 1,732 / 1,414 ≈ 796 kV crista (entre linhas)
```

A rigidez dielétrica do óleo mineral processado com isolação de papel (sistema óleo-papel) é tipicamente **10–20 kV/mm** dependendo do nível de pureza e pressão. Com 36 mm de distância:

```
Tensão suportável estimada = 36 mm × 15 kV/mm = 540 kV
```

A distância de 36 mm entre fases, combinada com o espaço entre as bobinas dentro da janela do núcleo e as barreiras isolantes de presspan, compõe o sistema de isolação interfase que suporta os 650 kV de BIL. O valor exato é verificado por métodos de campo elétrico (FEM) na EPA.

---

## 14. Núcleo — Chapa, Último Pacote e Curvas de Perda

→ [[Núcleo — Último Pacote e Curvas de Perda]] — Chapa M4-0,27 mm WEG TF (13 degraus, seção 2356,65 cm², indução 1,723 T), curvas de perdas específicas por nível de tensão (90–110% Vn), cálculo do último pacote (**não é necessário dividir**) e verificação de ventilação ONAF.

---

*Fonte primária: `Cópia de C19163865.xlsm` — aba **Dados_DTDS** | Coluna F = descrição, coluna G = valor | Linha (L) conforme indicado em cada parâmetro*
