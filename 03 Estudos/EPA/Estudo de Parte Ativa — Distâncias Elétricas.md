# Estudo de Parte Ativa — Distâncias Elétricas

> **Objetivo principal:** definir as **dimensões limite do tanque** (comprimento, largura e altura internos mínimos) a partir das distâncias elétricas exigidas entre os componentes da parte ativa e as paredes do tanque.

---

## 1. Conceito e Motivação

A parte ativa de um transformador de potência é o conjunto **núcleo + enrolamentos + terminais** imerso em óleo mineral isolante dentro do tanque. Toda a geometria do tanque é condicionada por uma regra fundamental:

> Nenhum componente em potencial diferente de zero pode se aproximar de outro componente (incluindo a parede aterrada do tanque) a uma distância menor do que aquela que o meio isolante (óleo) consegue suportar sob as condições de ensaio definidas pela norma.

Essas distâncias mínimas são as **distâncias elétricas** e variam conforme:
- O **nível de tensão** do componente (derivado da tensão nominal do sistema)
- O **nível de isolamento** adotado (NBI e TP)
- O **meio isolante** envolvido (óleo-óleo, óleo-papel, papel-papel)

**Norma de referência:** ABNT NBR 5356 / 2007 — partes 1 e 3 (equivalente às IEC 60076-1 e IEC 60076-3).

---

## 2. Dados de Entrada — O que deve ser levantado antes de qualquer cálculo

Antes de abrir qualquer tabela da folha de cálculo, estes parâmetros precisam estar definidos:

| Dado | Descrição | Onde buscar |
|------|-----------|-------------|
| **S (kVA / MVA)** | Potência nominal | Especificação do cliente |
| **U_AT (kV)** | Tensão nominal AT | Especificação do cliente |
| **U_BT (kV)** | Tensão nominal BT | Especificação do cliente |
| **f (Hz)** | Frequência nominal | 60 Hz (Brasil) |
| **Conexão** | Grupo de ligação (ex: Dyn11) | Especificação do cliente |
| **Um_AT (kV)** | Tensão máxima do sistema — AT | Tabela NBR 5356-1 Tab. 1 |
| **Um_BT (kV)** | Tensão máxima do sistema — BT | Tabela NBR 5356-1 Tab. 1 |
| **NBI_AT (kV pico)** | Nível Básico de Impulso — AT | Tabela NBR 5356-3 |
| **NBI_BT (kV pico)** | Nível Básico de Impulso — BT | Tabela NBR 5356-3 |
| **TP_AT (kV ef)** | Tensão de Prova Freq. Industrial — AT | Tabela NBR 5356-3 |
| **TP_BT (kV ef)** | Tensão de Prova Freq. Industrial — BT | Tabela NBR 5356-3 |
| **Tap range** | Faixa de regulação de tensão | Especificação / comutador |

> **NBT — Neutro de Baixa Tensão:** quando o enrolamento BT está em **estrela (Y/yn)**, o ponto neutro é conduzido para fora do tanque por uma bucha dedicada chamada **NBT**. Ela tem nível de isolamento reduzido (menor NBI que as fases BT) pois fica próxima ao potencial de terra. Isso afeta diretamente as distâncias elétricas que ela exige e seu posicionamento no lado S2.

---

## 3. Nível de Isolamento — NBR 5356-3

O nível de isolamento é o par **(NBI ; TP)** que o transformador deve suportar nos ensaios dielétricos.

### 3.1 Como determinar

A norma relaciona a **tensão máxima do sistema Um** a um conjunto de níveis de isolamento possíveis. O projetista escolhe o nível com base nos requisitos do cliente / sistema elétrico.

**Tabela de referência resumida (NBR 5356-3 Tabela 2):**

| Um (kV ef) | NBI (kV pico) | TP (kV ef) |
|-----------|--------------|-----------|
| 7,2 | 60 | 20 |
| 12 | 75 / 95 | 28 / 35 |
| 17,5 | 95 / 110 | 38 / 38 |
| 24 | 125 / 145 | 50 / 55 |
| 36 | 170 / 200 | 70 / 80 |
| 72,5 | 325 / 350 | 140 / 160 |
| 145 | 550 / 650 | 230 / 275 |
| 245 | 850 / 950 / 1050 | 395 / 395 / 460 |

> O critério determinante para as distâncias internas é o **maior** entre:  
> `d_impulso` (calculado pelo NBI) e `d_frequência` (calculado pelo TP).  
> Na prática, para tensões ≥ 72,5 kV o **NBI** sempre governa.

### 3.2 Nível do Neutro (NBT)

Para transformadores com neutro acessível (yn), o NBT pode ter nível de isolamento reduzido conforme a rigidez do aterramento do neutro do sistema. Valores típicos:

| Sistema | NBI_NBT (kV pico) | TP_NBT (kV ef) |
|---------|--------------------|----------------|
| Neutro sólido a terra | 38 – 75 | 10 – 20 |
| Neutro impedante | 95 – 170 | 35 – 70 |

---

## 4. Distâncias Elétricas em Óleo — Base dos Cálculos

Toda a estrutura dimensional do EPA depende deste passo. A distância elétrica mínima em óleo é determinada em função do NBI e/ou TP dos componentes envolvidos.

### 4.1 Formulação geral

A rigidez dielétrica do óleo mineral isolante é tipicamente:
- Sob impulso de raio: **~8 a 10 kV/mm**
- Sob frequência industrial: **~2 a 3 kV/mm**

A distância mínima bruta (sem folga de projeto) seria:

$$d_{min,impulso} = \frac{NBI}{k_{impulso}} \qquad d_{min,freq} = \frac{TP}{k_{freq}}$$

Na prática utiliza-se tabela interna com fator de segurança embutido (ver WPR-7583).

### 4.2 Tabela de distâncias internas em óleo (referência WPR-7583)

As distâncias abaixo são para **óleo limpo e seco** entre superfícies não revestidas. Superfícies com isolação papel/pressboard permitem redução.

| NBI (kV pico) | Fase–Terra `d_FT` (mm) | Fase–Fase `d_FF` (mm) |
|--------------|------------------------|----------------------|
| 60 | 12 | 20 |
| 75 | 16 | 28 |
| 95 | 20 | 35 |
| 125 | 26 | 45 |
| 145 | 30 | 52 |
| 170 | 36 | 62 |
| 200 | 43 | 75 |
| 250 | 53 | 92 |
| 325 | 68 | 118 |
| 350 | 74 | 128 |
| 450 | 95 | 165 |
| 550 | 116 | 200 |
| 650 | 137 | 237 |
| 750 | 158 | 273 |
| 850 | 178 | 308 |
| 950 | 198 | 342 |
| 1050 | 218 | 377 |

> **Fase–Terra** = distância mínima entre qualquer ponto em alta tensão e qualquer superfície aterrada (parede do tanque, núcleo, etc.)  
> **Fase–Fase** = distância mínima entre condutores de fases diferentes em igual potencial de NBI.

### 4.3 Distâncias com isolação sólida (pressboard / papel)

Quando um trecho da distância é percorrido por material sólido (envoltório do enrolamento, pressboard, etc.), a distância equivalente em óleo é **reduzida** porque o pressboard tem rigidez dielétrica maior:

$$d_{equiv,óleo} = d_{total} - \frac{e_{sólido}}{\varepsilon_r} \approx d_{total} - \frac{e_{sólido}}{3{,}5}$$

Onde `ε_r ≈ 3,5` é a permissividade relativa do pressboard em relação ao óleo.

---

## 5. Etapas do Estudo e Tabelas da Folha de Cálculo

### Tabela 1 — Dados do Transformador (Entrada)

**O que é:** cabeçalho geral com os dados elétricos e mecânicos do transformador que alimentam todas as demais tabelas.

**O que observar:**
- Verificar se o **grupo de ligação** (ex: Dyn11) condiz com a presença/ausência do NBT
- Conferir se os **níveis de isolamento** (NBI e TP) estão corretos para a tensão nominal e o sistema do cliente
- Verificar o **número de tap** e a relação de transformação em cada tap — isso afeta as distâncias entre o enrolamento de regulação e outros componentes

---

### Tabela 2 — Distâncias Elétricas Mínimas em Óleo

**O que é:** a tabela que converte os NBI e TP (da Tabela 1) em distâncias mínimas lineares que devem ser respeitadas em todo o projeto.

**Saídas típicas desta tabela:**

| Variável | Descrição |
|----------|-----------|
| `d_FT_AT` | Distância fase-terra para o nível AT |
| `d_FF_AT` | Distância fase-fase para o nível AT |
| `d_FT_BT` | Distância fase-terra para o nível BT |
| `d_FF_BT` | Distância fase-fase para o nível BT |
| `d_FT_NBT` | Distância fase-terra para o neutro BT |
| `d_AT_BT` | Distância entre enrolamentos AT e BT (barreira isolante) |

**Por que essa tabela importa:** todas as distâncias nas vistas superior e lateral são derivadas daqui. Um erro nesta tabela contamina todas as dimensões do tanque.

**Ponto crítico:** a distância AT–BT (`d_AT_BT`) é calculada com base no **diferencial de NBI** entre os dois enrolamentos, não no NBI de um deles isoladamente. A condição de ensaio de indução tensiona a barreira entre AT e BT com a diferença de potencial entre eles.

---

### Tabela 3 — Dados do Núcleo (Core)

**O que é:** geometria do núcleo magnético que posiciona as colunas no espaço.

**Variáveis principais:**

| Variável | Significado |
|----------|-------------|
| `d_col` | Diâmetro equivalente da coluna do núcleo (mm) |
| `n_col` | Número de colunas (3 para transformador trifásico) |
| `C` | **Passo entre colunas** — distância entre eixos de colunas adjacentes (mm) |
| `H_jan` | Altura da janela do núcleo (mm) |
| `H_iog` | Altura do iógo (culatra) superior e inferior (mm) |

**Relação com distâncias elétricas:** o passo `C` deve garantir que os enrolamentos de fases adjacentes fiquem separados por pelo menos `d_FF_AT`:

$$C \geq \Phi_{ext,AT} + d_{FF,AT}$$

Onde `Φ_ext,AT` é o diâmetro externo do enrolamento AT.

---

### Tabela 4 — Dados dos Enrolamentos (Coil)

**O que é:** geometria completa dos enrolamentos BT e AT para cada fase.

**Variáveis principais:**

| Variável | Significado |
|----------|-------------|
| `Φ_int_BT` | Diâmetro interno do enrolamento BT |
| `Φ_ext_BT` | Diâmetro externo do enrolamento BT |
| `Φ_int_AT` | Diâmetro interno do enrolamento AT |
| `Φ_ext_AT` | Diâmetro externo do enrolamento AT |
| `L_ax` | Comprimento axial (altura) dos enrolamentos |
| `e_canal_AT_BT` | Espessura do canal de óleo entre AT e BT |

**Verificações obrigatórias:**

1. **Canal entre BT e núcleo:** `Φ_int_BT/2 - d_col/2 ≥ canal_mín` (canal de circulação de óleo ≥ 5–8 mm típico)

2. **Canal de óleo entre AT e BT:**
$$e_{canal,AT\_BT} \geq d_{AT\_BT} - e_{isolação,AT} - e_{isolação,BT}$$

3. **Distância entre enrolamentos AT de fases adjacentes:**
$$C - \Phi_{ext,AT} \geq d_{FF,AT}$$

---

### Tabela 5 — Vista Superior — Dimensionamento Horizontal do Tanque

**O que é:** a tabela mais crítica para definir o comprimento e a largura interna do tanque. Trabalha no plano XY (vista de cima).

#### 5.1 Eixo Longitudinal (comprimento do tanque)

O comprimento interno mínimo é determinado pelo espaço ocupado pelas 3 fases alinhadas:

$$L_{int} = 2 \times C + 2 \times \left(\frac{\Phi_{ext,AT}}{2} + d_{FT,AT\_parede}\right)$$

Onde:
- `C` = passo entre colunas
- `Φ_ext_AT` = diâmetro externo do enrolamento AT
- `d_FT,AT_parede` = distância mínima entre a superfície do enrolamento AT e a parede do tanque (função de `d_FT_AT`)

**Parede S1 / S4** (lados das buchas): a distância do enrolamento AT da fase extrema até a parede S1 ou S4 pode ser aumentada para acomodar leads internos, suportes, TCs de bucha, etc.

#### 5.2 Eixo Transversal (largura do tanque)

A largura é a maior entre três condições:

**Condição A — Core & Coil:**
$$L_{CC} = \Phi_{ext,AT} + 2 \times d_{FT,AT\_parede}$$

**Condição B — Lado S3 (buchas AT):**
$$L_{S3} = \text{espaço necessário para posicionar as 3 buchas AT com distâncias entre si e à parede}$$

**Condição C — Lado S2 (buchas BT + NBT):**
$$L_{S2} = \text{espaço necessário para posicionar 3 buchas BT + 1 bucha NBT com distâncias entre si e à parede}$$

O valor adotado é: $L_{int,transversal} = \max(L_{CC},\ L_{S3},\ L_{S2})$

> No tanque oblongo, S1 e S4 são os lados curtos (transversais) e S2 / S3 são os lados longos. **ATENÇÃO: verifique a convenção adotada na folha de cálculo** — algumas convenções invertem S2/S3 ou chamam de "comprimento" o eixo transversal.

---

### Tabela 6 — Vista Lateral — Altura do Tanque

**O que é:** determinação da altura interna mínima do tanque, trabalhando no eixo vertical Z.

**Cálculo da altura interna:**

$$H_{int} = H_{col\_enr} + \Delta_{inf} + \Delta_{sup}$$

Onde:
- `H_col_enr` = altura total da montagem núcleo + enrolamentos (iogue inf + janela + iogue sup)
- `Δ_inf` = folga inferior (espaço entre a base do núcleo e o fundo interno do tanque)
- `Δ_sup` = folga superior (espaço entre o topo do núcleo e a tampa interna)

**Composição da folga inferior `Δ_inf`:**
- Distância elétrica mínima entre o iogue aterrado e o fundo do tanque (geralmente ≥ 50–80 mm)
- Espaço para cavaletes/suportes do núcleo
- Espaço para circulação de óleo

**Composição da folga superior `Δ_sup`:**
- Distância elétrica dos terminais AT ao tampo
- Espaço para passagem de leads e conexões internas
- **Altura empilhada dos TCs** (quando montados sobre as buchas por dentro do tanque)
- Eventual comutador (se OLTC — regulação sob carga)

**Verificação crítica da folga superior com TCs:**
$$\Delta_{sup} \geq h_{TCs,empilhados} + d_{TC\_tampo} + h_{terminal\_bucha}$$

---

### Tabela 7 — Buchas AT e BT/NBT

**O que é:** dimensionamento do posicionamento das buchas no tampo ou nas paredes do tanque, e verificação das distâncias elétricas entre elas.

#### 7.1 Lado S3 — Buchas AT (3 fases: U, V, W)

As 3 buchas AT estão dispostas linearmente ao longo do comprimento do tanque (eixo longitudinal):

**Distância mínima entre buchas AT adjacentes (fase–fase):**
$$d_{bucha\_bucha,AT} \geq d_{FF,AT} + \Delta_{construtivo}$$

**Distância mínima da bucha AT à parede S3:**
$$d_{bucha\_parede,AT} \geq d_{FT,AT}$$

**Distância mínima da bucha AT à parede S1 ou S4 (lados curtos):**
$$d_{bucha\_lateral,AT} \geq d_{FF,AT}/2 + \Delta$$

#### 7.2 Lado S2 — Buchas BT e NBT (3+1 buchas: u, v, w, NBT)

Quatro buchas no lado S2, geralmente dispostas como: **u — v — w — NBT** ou **NBT — u — v — w**

**Distância mínima entre buchas BT adjacentes (fase–fase):**
$$d_{bucha\_bucha,BT} \geq d_{FF,BT}$$

**Distância mínima NBT–BT fase adjacente:**
$$d_{NBT\_BT} \geq d_{FT,BT}$$
*(o NBT está próximo ao potencial de terra, portanto a distância para a fase BT é a distância fase–terra do nível BT)*

**Distância mínima da bucha BT ou NBT à parede S2:**
$$d_{bucha\_parede,BT} \geq d_{FT,BT}$$

> **Verificação do lado S2:** com 4 buchas, o espaçamento acumulado costuma ser o fator determinante da **largura do tanque**. Calcule sempre o espaço total ocupado e compare com `L_CC` da Tabela 5.

#### 7.3 Ângulo das buchas

Buchas instaladas na tampa em posição inclinada (comum em AT) — verificar que a **projeção da bucha sobre o plano horizontal** não viola as distâncias fase–terra em relação à borda da abertura do tampo ou a outras buchas.

---

## 6. TCs do Transformador de Potência *(seção complementar)*

Os **Transformadores de Corrente (TCs)** instalados internamente no transformador de potência são componentes que **impactam diretamente a altura do tanque** e devem ser considerados no EPA.

### 6.1 Tipos de TC internos

| Tipo | Descrição | Localização típica |
|------|-----------|-------------------|
| **TC de bucha** | Núcleo toroidal que envolve o terminal passante da bucha | Abaixo da bucha, dentro do tanque |
| **TC de janela** | Núcleo toroidal com fio que passa pela janela | Sobre a bucha AT ou BT |
| **TC barra** | Para correntes muito elevadas (BT) | Terminal BT antes da bucha |

### 6.2 Dados necessários dos TCs para o EPA

Para cada TC é preciso conhecer:

| Dado | Símbolo | Impacto no EPA |
|------|---------|---------------|
| Diâmetro interno | `d_int_TC` | Deve acomodar o terminal passante da bucha |
| Diâmetro externo | `d_ext_TC` | Define o espaço lateral necessário |
| Altura de um núcleo | `h_TC` | Influencia a altura empilhada |
| Número de núcleos por fase | `n_TC` | Multiplica a altura empilhada |
| **Altura total empilhada** | `H_TC = n_TC × h_TC + folgas` | **Entra diretamente na folga superior** |

### 6.3 Posicionamento dos TCs

#### TCs no lado AT (S3 — 3 fases)

Cada fase AT tem seus `n_TC` núcleos empilhados sobre o terminal interno da bucha AT:

```
TAMPO
  │
  ├─── Bucha AT (exterior)
  │
  ╠═══ TC_AT nº 1  ┐
  ╠═══ TC_AT nº 2  ├─ Empilhamento: H_TC,AT = n_TC × h_TC + folgas
  ╠═══ TC_AT nº n  ┘
  │
  └─── Terminal AT do enrolamento
```

A altura total dos TCs AT é adicionada à folga superior:
$$\Delta_{sup} \geq H_{TC,AT} + d_{TC\_tampo,AT} + \text{outros}$$

#### TCs no lado BT (S2 — 3 fases + NBT)

O NBT geralmente **não tem TC** (não há medição nem proteção no neutro na maioria dos projetos). As 3 fases BT têm TCs:

```
Fase BT (u, v, w):
  H_TC,BT = n_TC,BT × h_TC,BT + folgas
```

> **Ponto de atenção:** quando os TCs BT têm dimensão maior (corrente de BT elevada → núcleo maior), eles podem se tornar o fator limitante da folga superior, mesmo com NBI BT menor.

### 6.4 Distâncias elétricas dos TCs

O corpo do TC (se metálico ou com núcleo condutor) é geralmente **aterrado**. Portanto:

- **Distância TC–terminal AT:** mínimo `d_FT_AT`
- **Distância TC–TC de fases diferentes:** mínimo `d_FF` do nível correspondente
- **Distância TC–tampo (parede aterrada):** mínimo conforme o nível da bucha associada

### 6.5 Verificação da altura com TCs

A equação completa da altura interna com TCs é:

$$H_{int} = H_{nucleo\_enr} + \Delta_{inf} + h_{TCs,AT} + h_{leads,AT} + d_{AT\_tampo} + e_{tampo}$$

Se os TCs BT forem mais altos que os AT, substitui-se `h_TCs,AT` por `h_TCs,BT`.

---

## 7. Síntese — Dimensões Limite do Tanque Oblongo

### 7.1 Convenção de faces do tanque oblongo

```
        ┌────────────── S3 (AT) ──────────────┐
        │  ●AT_U        ●AT_V        ●AT_W    │  (buchas AT)
  S4    │                                     │  S1
(curto) │  [Fase U]   [Fase V]   [Fase W]    │ (curto)
        │                                     │
        │  ●BT_u  ●BT_v  ●BT_w  ●NBT        │  (buchas BT + NBT)
        └────────────── S2 (BT) ──────────────┘
```

### 7.2 Tabela de dimensões mínimas

| Dimensão | Fórmula resumida | Condição determinante |
|----------|------------------|-----------------------|
| **Comprimento int. (S1→S4)** | `L = 2C + Φ_ext,AT + 2×d_FT,AT_parede` | Distância AT à parede + passo |
| **Largura int. (S2→S3)** | `max(L_CC, L_S2, L_S3)` | Geralmente L_S2 (4 buchas BT) |
| **Altura int.** | `H = H_nuc_enr + Δ_inf + Δ_sup` | Folga superior com TCs |

### 7.3 Sequência de cálculo

```
1. Dados elétricos → NBI e TP
         ↓
2. NBI/TP → d_FT, d_FF (Tabela distâncias em óleo)
         ↓
3. Núcleo (d_col, passo C) + Enrolamentos (Φ_int, Φ_ext)
         ↓
4. Vista Superior → L_int (comprimento) e L_int_transv (largura)
         ↓
5. Buchas AT (S3) e BT+NBT (S2) → verifica/aumenta largura
         ↓
6. TCs → h_TCs empilhados → alimenta Δ_sup
         ↓
7. Vista Lateral → H_int (altura)
         ↓
8. Dimensões limite do tanque: L × l × H (internos mínimos)
```

---

## 8. Checklist — Pontos Críticos nas Análises

- [ ] O NBI do NBT está correto para o tipo de aterramento do neutro do sistema?
- [ ] A distância AT–BT considera a barreira de pressboard (redução da distância equivalente)?
- [ ] O passo entre colunas garante `d_FF_AT` entre os enrolamentos AT?
- [ ] A largura do lado S2 acomoda as 4 buchas (3 BT + 1 NBT) com todas as distâncias?
- [ ] Os TCs de todas as fases (AT e BT) foram incluídos na folga superior?
- [ ] O NBT tem TC? (geralmente não — confirmar na especificação)
- [ ] A distância dos TCs aterrados ao terminal AT respeita `d_FT_AT`?
- [ ] Em tap extremo (maior tensão), as distâncias do enrolamento de regulação ao tanque ainda estão ok?
- [ ] O comutador (se OLTC) está incluído na folga superior?

---

## 9. Referências

- ABNT NBR 5356-1:2007 — Transformadores de potência: Generalidades
- ABNT NBR 5356-3:2007 — Transformadores de potência: Níveis de isolamento, ensaios dielétricos e distâncias de isolamento externo no ar
- WPR-7583 PT.3 — Procedimento interno WEG: Distâncias elétricas em parte ativa
- [[Canecos]] — Referência de imagens de canecos e terminais
- [[Folga e cordão]] — Folgas e cordões de vedação dos enrolamentos
