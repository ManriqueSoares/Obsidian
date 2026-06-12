# Níveis de Isolação — Transformador ADA DATA CENTER

> Transformador **C19163865** | Norma **ABNT NBR 5356/2007**
> Fontes: `Dados_DTDS` L23–L42 | `Folha 1` L16

---

## Tabela Geral — Visão por Enrolamento

| Enrolamento | Classe Um (kV) | BIL — Onda Plena (kV crista) | Onda Cortada (kV crista) | Aplicada (kV ef.) | Induzida (kV ef.) |
|---|---|---|---|---|---|
| AT (linha) | 145 | 650 | 715 | 275 | 275 |
| BT1 (linha) | 36,2 | 200 | 220 | 70 | 69 |
| NBT1 (neutro BT) | 36,2 | 170 | — | 70 | — |

> **Folha 1, L16:** confirmação resumida dos níveis — BT1: 36,2 kV | AT1: 145 kV | AT2: 145 kV

---

## 1. AT — Classe 145 kV

| Ensaio | Valor | Fonte (Dados_DTDS) |
|---|---|---|
| Classe de tensão (Um) | 145 kV | L23 |
| Impulso onda plena (BIL) | 650 kV crista | L24 |
| Impulso onda cortada | 715 kV crista | L25 |
| Tensão aplicada | 275 kV eficaz | L26 |
| Tensão induzida | 275 kV eficaz | L27 |

### Por que a classe é 145 kV e não 138 kV?

A **classe de tensão (Um)** não é a tensão nominal de operação — é a **tensão máxima do sistema** para a qual o transformador é projetado, conforme tabelas padronizadas da NBR 5356 / IEC 60076. O sistema de 138 kV no Brasil opera com variações e sobretensões temporárias, e a norma exige que o equipamento suporte a tensão máxima do sistema sem degradação:

```
Tensão nominal AT:  138,0 kV
Tensão máxima (Um): 145,0 kV  → margem de +5,1% acima do nominal
```

A classe 145 kV é o próximo nível padronizado acima de 138 kV na tabela NBR 5356.

---

## 2. BT1 — Classe 36,2 kV

| Ensaio | Valor | Fonte (Dados_DTDS) |
|---|---|---|
| Classe de tensão (Um) | 36,2 kV | L34 |
| Impulso onda plena (BIL) | 200 kV crista | L35 |
| Impulso onda cortada | 220 kV crista | L36 |
| Tensão aplicada | 70 kV eficaz | L37 |
| Tensão induzida | 69 kV eficaz | L38 |

```
Tensão nominal BT:  34,5 kV
Tensão máxima (Um): 36,2 kV  → margem de +4,9% acima do nominal
```

### De onde vem o BIL 200 kV?

A NBR 5356-3 / IEC 60076-3 define tabelas de níveis de isolação padronizados para cada classe Um. Para **Um = 36,2 kV** existem dois níveis de BIL disponíveis:

| Opção | BIL (kV crista) | Aplicação típica |
|---|---|---|
| Nível 1 (reduzido) | 170 kV | Neutro de enrolamento aterrado (NBT1) |
| Nível 2 (pleno) | **200 kV** | Terminais de linha — este transformador |

O projetista escolhe o nível 2 (200 kV) para os terminais de linha da BT porque o sistema de 34,5 kV pode ter aterramentos não efetivos ou operar com neutro isolado em certas configurações, expondo os terminais a sobretensões mais elevadas. O nível 1 (170 kV) é reservado ao neutro (NBT1), que opera muito próximo do terra.

### Por que a tensão induzida BT é 69 kV e não 70 kV?

São dois ensaios distintos com origens diferentes na norma:

```
Tensão aplicada BT:  70 kV eficaz  → valor tabelado na NBR 5356 para Um = 36,2 kV (separado)
Tensão induzida BT:  69 kV eficaz  → 2 × V_nominal = 2 × 34,5 kV = 69,0 kV (calculado)
```

A **aplicada** (70 kV) é fixada pela tabela normativa e testa a isolação principal enrolamento-terra. A **induzida** (69 kV) é exatamente o dobro da tensão nominal de linha e testa a isolação longitudinal — os dois valores não precisam ser iguais porque testam regiões diferentes. A diferença de 1 kV entre eles não é erro de projeto, é intencional.

---

## 3. NBT1 — Neutro da BT — Classe 36,2 kV

| Ensaio | Valor | Fonte (Dados_DTDS) |
|---|---|---|
| Classe de tensão | 36,2 kV | L39 |
| Impulso onda plena (BIL) | 170 kV crista | L40 |
| Tensão aplicada | 70 kV eficaz | L42 |

### Por que o neutro tem BIL menor que a linha (170 vs. 200 kV)?

O neutro da estrela está eletricamente mais próximo do terra (potencial zero) do que os terminais de linha. Em sistemas aterrados, o neutro experimenta sobretensões menores durante faltas e impulsos. Por isso a NBR 5356 permite um **BIL reduzido no neutro** quando o sistema de aterramento é efetivo — é o chamado isolamento **não uniforme** (graded insulation):

```
BIL linha BT1:  200 kV crista  (terminal sob plena tensão de fase)
BIL neutro BT1: 170 kV crista  (terminal próximo do terra — 85% do BIL de linha)
```

---

## 3b. NAT — Neutro AT — Por que está ausente?

Os campos da planilha para o neutro AT (Dados_DTDS L28–L31: classe NAT, BIL NAT, impulso de manobra AT, aplicada NAT) estão **todos em branco**. Isso não é esquecimento — é uma consequência direta do grupo de ligação.

**A AT está ligada em delta (D).** Em uma ligação delta, as três bobinas formam um triângulo fechado: o terminal final de cada bobina conecta-se diretamente ao terminal inicial da próxima. Não existe ponto central — portanto, **não há terminal neutro na AT**.

```
Ligação delta AT:

    A ────────┐
              │ bobina AB
    B ────────┘────────┐
                       │ bobina BC
    C ────────┐────────┘
              │ bobina CA
    A ─────── ┘

→ Nenhum ponto comum acessível = sem neutro = sem NAT
```

Se a AT fosse ligada em estrela (Y), haveria um ponto neutro e os campos NAT seriam preenchidos. No Dyn1 deste transformador, apenas a BT tem neutro acessível (terminal N).

---

## 3c. Impulso de Manobra — Por que o campo L30 está vazio?

O campo **"Impulso de Manobra AT" (Dados_DTDS L30)** está vazio porque esse ensaio **não é exigido pela NBR 5356 / IEC 60076-3 para a classe 145 kV**.

O impulso de manobra (switching impulse) simula sobretensões geradas por manobras de disjuntores e chaves seccionadoras em linhas energizadas. Sua forma de onda é muito mais lenta que o impulso de raio:

```
Impulso de raio (lightning):   1,2 / 50 µs    → frente rápida, 650 kV crista (AT)
Impulso de manobra (switching): 250 / 2500 µs  → frente lenta, nível próprio
```

A norma só exige o ensaio de impulso de manobra para equipamentos com **Um ≥ 300 kV**, porque é nessa faixa que as sobretensões de manobra se tornam o critério dimensionador da isolação (em sistemas de 500 kV e acima, o impulso de manobra pode ser mais crítico que o de raio para distâncias longas no óleo).

Para a classe **Um = 145 kV**, o impulso de raio (BIL 650 kV) é o ensaio determinante e o campo de manobra fica em branco por isenção normativa — não por omissão do projetista.

---

## 4. O que cada ensaio testa — Funcionamento físico

### 4.1 Tensão Aplicada *(Applied Voltage Test — AV)*

**O que testa:** a **isolação principal** entre o enrolamento e a terra (tanque, núcleo, outros enrolamentos aterrados).

**Como é feito:** uma fonte externa de tensão é conectada ao enrolamento; todos os outros enrolamentos e o tanque são aterrados. A tensão é mantida por **60 segundos**.

**O que pode falhar:** perfuração do papel/pressspan entre a bobina e o núcleo, ou contornamento (flashover) pelo óleo entre terminais e tanque.

```
AT:  275 kV eficaz × √2 = 389 kV crista aplicados entre o enrolamento AT e a terra
BT:   70 kV eficaz × √2 =  99 kV crista aplicados entre BT e a terra
```

**Relação com a tensão nominal:**
```
AT: 275 / (138/√3) = 275 / 79,67 = 3,45×  a tensão de fase nominal
BT:  70 / (34,5/√3) = 70 / 19,92 = 3,51×  a tensão de fase nominal
```

O ensaio estressa a isolação a ~3,5 vezes a tensão de operação por 1 minuto.

**Por que exatamente 60 segundos?**
O tempo de 60 segundos é um valor normativo consagrado pelo IEC e adotado pela NBR 5356. A lógica é dupla:
- **Longo o suficiente** para que pontos fracos acumulem ionização e se rompam — um defeito real de fabricação (bolha de ar no papel, contaminação no óleo) não sobrevive a 60 s sob 3,5× a tensão nominal
- **Curto o suficiente** para não causar dano térmico à isolação sã — o papel impregnado em óleo suporta 60 s a esse nível sem envelhecimento significativo

**O que acontece quando a isolação falha durante o ensaio:**
1. O arco perfura o papel ou o óleo ioniza-se no ponto mais fraco
2. A tensão colapsa instantaneamente (o circuito se torna condutor)
3. A corrente na fonte de ensaio sobe abruptamente — detectada pelo sistema de monitoramento
4. No óleo: o arco produz bolhas de gás (H₂, C₂H₂) visíveis e partículas carbonizadas — o transformador é reprovado e deve ser reprocessado

---

### 4.2 Tensão Induzida *(Induced Voltage Test — IV)*

**O que testa:** a **isolação longitudinal** — entre espiras adjacentes, entre camadas, entre discos e entre seções dentro do mesmo enrolamento.

**Como é feito:** aplica-se no enrolamento BT uma tensão elevada; a AT induz proporcionalmente a tensão de ensaio. Como o fluxo no núcleo cresce com a tensão, para não saturar o núcleo em 60 Hz, o ensaio é realizado em **frequência dobrada (120 Hz)**.

**Verificação dos valores:**
```
AT induzida: 275 kV ≈ 2 × 138 kV = 276 kV  ✓  (2× a tensão nominal de linha)
BT induzida:  69 kV = 2 × 34,5 kV = 69 kV  ✓  (2× a tensão nominal de linha)
```

**Por que 120 Hz?**
O fluxo no núcleo é proporcional a V/f. Se tentarmos aplicar 2× a tensão em 60 Hz, o fluxo também dobra — o núcleo satura, a corrente de excitação dispara e o ensaio fica inviável. Usando 120 Hz com 2× a tensão, o fluxo fica igual ao de operação normal:

```
Φ = V / (4,44 × f × N)

Normal:   Φ = 138.000 / (4,44 × 60 × 1275) = 0,406 Wb
Ensaio:   Φ = 276.000 / (4,44 × 120 × 1275) = 0,406 Wb  ← mesmo fluxo
```

---

### 4.3 Impulso Onda Plena *(Lightning Impulse — LI / BIL)*

**O que simula:** uma descarga atmosférica (raio) que atinge a linha de transmissão e se propaga até o transformador.

**Forma de onda padronizada (NBR 5356 / IEC 60060):**
```
Tempo de frente:    T1 = 1,2 µs  (tempo para atingir o pico)
Tempo de meia-onda: T2 = 50 µs   (tempo até cair à metade do pico)
Notação:            1,2 / 50 µs
```

**O que pode falhar:** perfuração da isolação entre espiras — e o motivo pelo qual isso acontece preferencialmente nas primeiras espiras é a **distribuição capacitiva do impulso**, explicada abaixo.

**Por que as primeiras espiras recebem a maior parte da tensão?**

Em regime permanente (60 Hz), a tensão distribui-se uniformemente ao longo do enrolamento — cada espira recebe V_total / N_total. Durante um impulso de 1,2 µs, isso muda radicalmente porque a frequência equivalente do impulso é muito alta (centenas de kHz) e o comportamento do enrolamento passa a ser dominado pelas capacitâncias, não pelas indutâncias.

O enrolamento pode ser modelado como uma rede de capacitâncias:

```
Cs = capacitância série (entre espiras/discos adjacentes)
Cg = capacitância de terra (entre espiras e o núcleo/tanque aterrado)

         Cs      Cs      Cs      Cs
entrada ──||──●──||──●──||──●──||──● saída
             |       |       |       |
            Cg      Cg      Cg      Cg
             |       |       |       |
            GND     GND     GND     GND
```

O parâmetro α = √(Cg / Cs) define o grau de não-uniformidade. Quanto maior α, mais a tensão se concentra na entrada. Para enrolamentos convencionais α pode ser 5–20.

```
Distribuição inicial (t = 0⁺, início do impulso):
  Tensão na 1ª espira ≈ (α / 2) × (V_total / N)   ← muito maior que 1/N
  Tensão na última espira ≈ quase zero
```

Para este transformador, o AT1 usa o tipo **"Disco — 16DE + 60DC + 16DE"** (Folha 1, L17):
- **DC** = Disco Contínuo (standard)
- **DE** = Disco de Entrada — discos especiais no início e fim do enrolamento com geometria modificada para **aumentar Cs** e reduzir α

Os 16 discos DE na entrada são o recurso de engenharia para "achatar" a distribuição da tensão de impulso nas primeiras seções, protegendo a isolação entre as primeiras espiras que, sem essa medida, seriam as mais estressadas.

**Valores:**
```
AT:  650 kV crista  (BIL)
BT:  200 kV crista  (BIL)
```

**Fator de proteção do BIL em relação à tensão de serviço:**
```
V_fase_AT (pico) = (138.000 / √3) × √2 = 79.674 × 1,4142 = 112.680 V crista

Fator = BIL_AT / V_fase_pico = 650.000 / 112.680 = 5,77×
```

O BIL é 5,77 vezes a tensão de pico de operação — essa é a margem de proteção que o sistema de isolação oferece contra raios.

---

### 4.4 Impulso Onda Cortada *(Chopped Impulse — CI)*

**O que simula:** a atuação de um para-raios ou centelhador que "corta" a onda de impulso ao conduzir, limitando a tensão mas criando uma taxa de variação dV/dt muito alta.

**Forma de onda:**
```
A onda sobe normalmente até o pico e é interrompida abruptamente em ~2–3 µs após o pico,
criando uma queda brusca de tensão (colapso da onda).
```

**Por que exige nível maior que a onda plena?**
A queda brusca distribui a tensão de forma ainda mais irregular nas primeiras espiras do enrolamento. A isolação entre espiras adjacentes fica sob maior estresse por causa do alto dV/dt, tornando o ensaio mais severo que o impulso pleno.

```
AT onda plena:  650 kV crista
AT onda cortada: 715 kV crista = 650 × 1,10 = 715 kV  ✓  (+10% sobre o BIL)

BT onda plena:  200 kV crista
BT onda cortada: 220 kV crista = 200 × 1,10 = 220 kV  ✓  (+10% sobre o BIL)
```

A relação cortada/plena ≈ 1,10 é padronizada pela NBR 5356 para a classe 145 kV.

---

## 5. Relação entre os ensaios e as regiões de isolação

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Região / Ameaça                        │  Ensaio que testa                 │
├──────────────────────────────────────────────────────────────────────────────┤
│  Enrolamento ↔ Terra                    │  Tensão Aplicada (AV)             │
│  Enrolamento ↔ Enrolamento              │  Tensão Aplicada (AV)             │
│  Espira ↔ Espira / Disco ↔ Disco        │  Tensão Induzida (IV)             │
│  Sobretensão de raio (1,2/50 µs)        │  Impulso Onda Plena (LI)          │
│  Atuação de para-raios sobre onda raio  │  Impulso Onda Cortada (CI)        │
│  Sobretensão de manobra (250/2500 µs)   │  Não exigido — Um = 145 kV < 300 kV│
└──────────────────────────────────────────────────────────────────────────────┘
```

> **Nota:** O impulso de onda cortada **não** representa manobras de rede. Ele simula o momento em que um para-raios entra em condução durante um raio e "corta" a onda de tensão — ainda é um evento de lightning, não de switching. As manobras de rede gerariam um impulso de manobra (250/2500 µs), que é um ensaio separado e não exigido nesta classe de tensão.

---

## 6. Confirmação cruzada — Folha 1 L16 vs. Dados_DTDS

| Enrolamento | Classe — Folha 1 L16 | Classe — Dados_DTDS | Confere? |
|---|---|---|---|
| BT1 | 36,2 kV (col D) | 36,2 kV (L34) | ✓ |
| AT1 | 145 kV (col G) | 145 kV (L23) | ✓ |
| AT2 | 145 kV (col J) | — (não listado separado) | ✓ compartilha da AT |

O AT2 (enrolamento de regulação) opera em série com o AT1 e compartilha a mesma classe de isolação 145 kV — faz sentido, pois está sujeito às mesmas sobretensões da rede de 138 kV.

---

*← [[CORE]] | Voltar ao arquivo principal do transformador ADA DATA CENTER*
