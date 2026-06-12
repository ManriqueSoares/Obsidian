# Fundamentos Eletromagnéticos — Transformadores de Potência

> Referência teórica para projetos EPA | Todas as leis, equações e definições essenciais
> Organizado da física fundamental até as equações de projeto direto

---

## Índice

1. [[#1. Grandezas Magnéticas Fundamentais]]
2. [[#2. As Equações de Maxwell]]
3. [[#3. Lei de Faraday — FEM Induzida]]
4. [[#4. Circuito Magnético — A "Lei de Ohm" do Magnetismo]]
5. [[#5. Fluxo Concatenado e Indutância]]
6. [[#6. Campo de Dispersão (Leakage Field)]]
7. [[#7. Perdas Magnéticas no Núcleo]]
8. [[#8. Equações Fundamentais do Transformador]]
9. [[#9. Circuito Equivalente]]
10. [[#10. Impedância de Curto-Circuito — Origem Física]]
11. [[#11. Força Eletrodinâmica nos Enrolamentos]]
12. [[#12. Notas de Estudo — Pontos Críticos]]

---

## 1. Grandezas Magnéticas Fundamentais

### 1.1 Fluxo Magnético Φ

O fluxo magnético é a quantidade de "linhas de campo" que atravessam uma superfície S:

$$\Phi = \int\!\!\int_S \vec{B} \cdot d\vec{A} \qquad [\text{Wb} = \text{V·s}]$$

Para campo uniforme perpendicular à seção:
$$\Phi = B \times A$$

> **Nota de estudo:** O fluxo é uma grandeza escalar, mas depende da orientação da superfície. No núcleo do transformador, a seção $A$ é a seção transversal da coluna (ex.: 2356,65 cm² neste projeto).

### 1.2 Densidade de Fluxo Magnético B

$$B = \frac{\Phi}{A} \qquad [\text{T} = \text{Wb/m}^2]$$

B é o campo que "existe" no material — resultado do campo H e da resposta do material (permeabilidade).

### 1.3 Campo Magnético H

$$H = \frac{B}{\mu} = \frac{B}{\mu_0 \mu_r} \qquad [\text{A/m}]$$

Onde:
- $\mu_0 = 4\pi \times 10^{-7}$ H/m — permeabilidade do vácuo
- $\mu_r$ — permeabilidade relativa do material (aço-silício: $\mu_r \approx 1.000$ a $10.000$, depende de B)

> **Nota crítica:** H é o campo "aplicado" (depende da corrente e geometria); B é o campo "resultante" (depende de H e do material). A relação B×H é **não linear** para o aço-silício — a curva B-H (curva de magnetização) é o que define o comportamento real do núcleo.

### 1.4 Curva B-H e Permeabilidade Diferencial

```
B (T)
2,0 ├─────────────────────────── saturação
1,8 │                      ╭────
1,6 │                   ╭──
1,4 │                ╭──              ← região linear (μr alto, constante)
1,2 │             ╭──
1,0 │          ╭──
0,5 │       ╭──
0,0 └──────────────────────── H (A/m)
         região linear    saturação
```

Na saturação, $\mu_r$ cai drasticamente — é por isso que as perdas em vazio crescem desproporcionalmente acima de 100% Vn.

Permeabilidade diferencial: $\mu_{dif} = \frac{dB}{dH}$ — é ela que governa o comportamento dinâmico.

### 1.5 Força Magnetomotriz (FMM ou MMF)

$$\mathcal{F} = N \times I \qquad [\text{A·esp} = \text{A (amperturns)}]$$

É o "motor" que cria o campo H ao longo de um caminho magnético. Analogia com tensão no circuito elétrico.

---

## 2. As Equações de Maxwell

As quatro equações que governam todos os fenômenos eletromagnéticos:

### 2.1 Lei de Gauss para o Campo Elétrico

$$\oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\varepsilon_0}$$

*Linhas de campo elétrico nascem em cargas positivas e terminam em negativas.*

### 2.2 Lei de Gauss para o Campo Magnético

$$\oint_S \vec{B} \cdot d\vec{A} = 0$$

**Não existem monopólos magnéticos.** Todo fluxo que entra em uma superfície fechada sai por outro lado — o fluxo magnético se fecha em laços. Consequência direta: o fluxo que entra pelo núcleo tem que sair pelo núcleo (salvo dispersão).

### 2.3 Lei de Faraday (forma diferencial de Maxwell)

$$\oint_C \vec{E} \cdot d\vec{l} = -\frac{d}{dt} \int\!\!\int_S \vec{B} \cdot d\vec{A} = -\frac{d\Phi}{dt}$$

*Um fluxo magnético variando no tempo cria um campo elétrico rotacional — a base da FEM induzida.*

### 2.4 Lei de Ampère-Maxwell

$$\oint_C \vec{H} \cdot d\vec{l} = I_{enc} + \varepsilon_0 \frac{d\Phi_E}{dt}$$

Para baixas frequências (60 Hz), o segundo termo (corrente de deslocamento) é desprezível. Fica:

$$\oint_C \vec{H} \cdot d\vec{l} = N \times I = \mathcal{F}$$

**Essa é a equação mais usada em projeto de transformadores:** a integral de H ao longo de qualquer contorno fechado é igual à corrente total que atravessa a superfície delimitada por esse contorno.

> **Nota de estudo:** As equações de Maxwell na forma integral são mais úteis para projeto de transformadores do que a forma diferencial (que exige $\nabla$). Memorize as formas integrais.

---

## 3. Lei de Faraday — FEM Induzida

### 3.1 Forma Básica

$$e = -\frac{d\Phi}{dt} \qquad \text{(1 espira)}$$

$$e = -N\frac{d\Phi}{dt} = -\frac{d\lambda}{dt} \qquad \text{(N espiras)}$$

O sinal negativo é a Lei de Lenz: a FEM induzida se opõe à variação que a causou.

### 3.2 Para Fluxo Senoidal

Se $\Phi(t) = \Phi_{max} \sin(\omega t)$:

$$e(t) = -N \frac{d\Phi}{dt} = -N \omega \Phi_{max} \cos(\omega t) = E_{max} \sin\left(\omega t - 90°\right)$$

O valor de pico:
$$E_{max} = N \omega \Phi_{max} = N \times 2\pi f \times \Phi_{max}$$

O valor eficaz:
$$\boxed{E = \frac{E_{max}}{\sqrt{2}} = \frac{N \times 2\pi f \times \Phi_{max}}{\sqrt{2}} = 4{,}44 \times f \times N \times \Phi_{max}}$$

**Esta é a equação da FEM do transformador** — a mais fundamental de todas.

### 3.3 Equação do Volt por Espira

Reorganizando para o volt/espira:

$$\frac{E}{N} = 4{,}44 \times f \times \Phi_{max}$$

E para a indução (substituindo $\Phi_{max} = B_{max} \times A_{nucleo}$):

$$\boxed{\frac{E}{N} = 4{,}44 \times f \times B_{max} \times A_{nucleo}}$$

**Aplicação direta (ADA DATA CENTER):**
```
108,25 = 4,44 × 60 × B_max × 0,235665 m²
B_max = 108,25 / (4,44 × 60 × 0,235665) = 1,723 T  ✓
```

> **Nota de estudo:** O volt/espira é o parâmetro de projeto do núcleo — ele conecta a tensão, a frequência, a geometria do núcleo e a indução em uma única equação. Todo o restante do projeto (número de espiras, seção do condutor, perdas) deriva dele.

### 3.4 A FEM está 90° atrasada do fluxo

Isso tem consequências diretas:
- A corrente de magnetização $I_{mag}$ está **em fase com o fluxo** (cria o fluxo)
- A FEM está **90° adiantada em relação a $I_{mag}$**
- Portanto $I_{mag}$ está **90° atrasada da tensão** → é puramente reativa (não consome potência ativa — ideal)
- A corrente de excitação real tem uma pequena componente ativa (perdas no ferro)

---

## 4. Circuito Magnético — A "Lei de Ohm" do Magnetismo

### 4.1 Relutância

A relutância é a "resistência" ao fluxo magnético:

$$\mathcal{R} = \frac{l}{\mu \times A} = \frac{l}{\mu_0 \mu_r A} \qquad [\text{A/Wb} = \text{H}^{-1}]$$

Onde $l$ é o comprimento do caminho magnético e $A$ é a seção transversal.

### 4.2 Lei de Hopkinson (Ohm magnético)

$$\mathcal{F} = \Phi \times \mathcal{R}$$

Analogia completa com o circuito elétrico:

| Circuito Elétrico | Circuito Magnético |
|---|---|
| Tensão V (V) | MMF $\mathcal{F}$ = NI (A) |
| Corrente I (A) | Fluxo Φ (Wb) |
| Resistência R (Ω) | Relutância $\mathcal{R}$ (A/Wb) |
| Lei de Ohm: V = IR | Hopkinson: $\mathcal{F} = \Phi \mathcal{R}$ |
| Condutância G = 1/R | Permeância P = 1/$\mathcal{R}$ |

### 4.3 Relutâncias em série e em paralelo

Em série (caminho único): $\mathcal{R}_{total} = \mathcal{R}_1 + \mathcal{R}_2 + \cdots$

Em paralelo (caminhos alternativos): $\frac{1}{\mathcal{R}_{total}} = \frac{1}{\mathcal{R}_1} + \frac{1}{\mathcal{R}_2} + \cdots$

### 4.4 Relutância de um entreferro (gap)

$$\mathcal{R}_{gap} = \frac{l_{gap}}{\mu_0 \times A} \qquad (\mu_r = 1 \text{ no ar})$$

Como $\mu_r$ do aço é milhares de vezes maior que o do ar, **um entreferro pequeno pode dominar a relutância total** do circuito. Em transformadores de potência, evita-se qualquer gap no núcleo (juntas são intercaladas para minimizar).

> **Nota de estudo:** A relutância das juntas das chapas é o motivo pelo qual W/kg projeto > W/kg base da chapa. Nas juntas, o fluxo "salta" para o ar brevemente — isso aumenta H local, aumenta a corrente de excitação e as perdas.

---

## 5. Fluxo Concatenado e Indutância

### 5.1 Fluxo Concatenado λ (Flux Linkage)

$$\lambda = N \times \Phi = N \times B \times A \qquad [\text{Wb·esp} = \text{V·s}]$$

O fluxo concatenado é o "produto" do fluxo pelo número de espiras que ele atravessa. É a grandeza que aparece na lei de Faraday: $e = -d\lambda/dt$.

**Quando nem todas as espiras são atravessadas pelo mesmo fluxo** (caso real com fluxo de dispersão):

$$\lambda = \sum_{k=1}^{N} \Phi_k$$

Onde $\Phi_k$ é o fluxo que atravessa a k-ésima espira. Na prática divide-se em:

$$\lambda_{total} = \lambda_{principal} + \lambda_{dispersão}$$

### 5.2 Indutância Própria L

$$L = \frac{\lambda}{I} = \frac{N\Phi}{I} = \frac{N^2}{\mathcal{R}} \qquad [\text{H}]$$

A indutância cresce com $N^2$ — dobrar o número de espiras quadruplica a indutância.

**Componentes da indutância em um transformador:**

$$L_{total} = L_m + L_{\sigma}$$

- $L_m$: indutância de magnetização (fluxo no núcleo — alta, desejável)
- $L_{\sigma}$: indutância de dispersão (fluxo fora do núcleo — parasita, causa queda de tensão)

### 5.3 Indutância Mútua M

$$M = \frac{\lambda_{21}}{I_1} = \frac{N_2 \Phi_{21}}{I_1} \qquad [\text{H}]$$

Onde $\Phi_{21}$ é o fluxo criado por $I_1$ que atravessa o enrolamento 2.

Para transformador ideal (todo fluxo do primário atravessa o secundário):

$$M = \sqrt{L_1 L_2} \qquad \text{(acoplamento perfeito, k = 1)}$$

No transformador real: $M = k\sqrt{L_1 L_2}$ onde $0 < k < 1$ (k próximo de 1 para bom acoplamento).

### 5.4 Coeficiente de Dispersão σ

$$\sigma = 1 - \frac{M^2}{L_1 L_2} = 1 - k^2$$

Em transformadores de potência: $k \approx 0{,}995$ a $0{,}999$ → $\sigma \approx 0{,}001$ a $0{,}01$ (muito pequeno, mas é o que determina a impedância de curto-circuito).

---

## 6. Campo de Dispersão (Leakage Field)

O campo de dispersão é o componente do campo magnético que **não se fecha pelo núcleo** — percorre o óleo e os enrolamentos. É a origem da reatância de curto-circuito $X_{cc}$.

### 6.1 Origem física

Cada espira conduz uma corrente que cria um campo ao seu redor pela Lei de Ampère. O campo que se fecha pelo núcleo de alta permeabilidade é o **fluxo principal** $\Phi_m$. O campo que se fecha pelo caminho de menor permeância (óleo/ar entre os enrolamentos) é o **fluxo de dispersão** $\Phi_\sigma$.

```
Seção axial do transformador (vista de cima da coluna):

NÚCLEO │ gap │ BT1 │ gap │ AT1 │ gap │ AT2
  ↑↑↑   →→→   ↑↑↑   →→→   ↓↓↓   →→→   ↑↑↑
fluxo   disp   fluxo  disp  fluxo  disp  fluxo
princ.  BT-N   BT    AT-BT   AT   AT-AT2  AT2

→→→ : fluxo de dispersão (percorre o óleo entre os enrolamentos)
```

### 6.2 Distribuição axial do campo de dispersão

Para dois enrolamentos coaxiais de mesma altura, pela Lei de Ampère ao longo de um contorno axial:

Na região dentro do enrolamento BT (entre núcleo e BT):
$$H(r) = \frac{N_{BT} \times I_{BT}}{h_{BT}} \times \frac{r - r_0}{a_{BT}} \qquad \text{(cresce linearmente)}$$

Na região do gap entre BT e AT:
$$H = \frac{N_{BT} \times I_{BT}}{h} = \text{constante}$$

Na região dentro do enrolamento AT:
$$H(r) = \frac{N_{BT} \times I_{BT}}{h} \times \left(1 - \frac{r - r_{AT,int}}{a_{AT}}\right) \qquad \text{(decresce linearmente)}$$

Onde $h$ é a altura comum dos enrolamentos, $a$ a espessura radial e $r_0$ o raio interno.

> **Nota de estudo:** O campo de dispersão é máximo no gap entre os enrolamentos e zero no centro de cada enrolamento (se NI dos dois enrolamentos se equilibram perfeitamente). Qualquer desequilíbrio de NI (como a soma −18 A·esp do tap 17 do ADA) cria um campo residual que penetra no núcleo — é o campo radial Hr do cálculo do último pacote.

### 6.3 Fator de Rogowski

Na prática, os enrolamentos **não têm a mesma altura** — o campo de dispersão se "derrama" nas extremidades. O fator de Rogowski corrige isso:

$$K_R = 1 - \frac{a_{BT} + a_{AT} + a_{gap}}{\pi \times h_{médio}} \times \left(1 - e^{-\pi h_{médio}/(a_{BT} + a_{AT} + a_{gap})}\right)$$

Simplificado:
$$K_R \approx 1 - \frac{a}{\pi \times h} \left(1 - e^{-\pi h/a}\right)$$

Onde $a = a_{BT} + a_{gap} + a_{AT}$ e $h$ é a altura média. Para transformadores de potência, $K_R \approx 0{,}95$ a $0{,}99$.

**Aplicação (ADA DATA CENTER):**
```
a = 61 + 43 + 79 = 183 mm (BT + gap + AT1)
h_médio ≈ (1120 + 1080)/2 = 1100 mm
K_R ≈ 1 − (183/(π×1100)) × (1 − e^(−π×1100/183))
    ≈ 1 − 0,053 × (1 − e^(−18,8))
    ≈ 1 − 0,053 × 1,0 ≈ 0,947
```

### 6.4 Indutância de Dispersão — Fórmula de Projeto

$$L_{\sigma} = \mu_0 \times K_R \times \frac{N^2 \times h_{eq}}{l_m} \times \left(\frac{a_{BT}}{3} + a_{gap} + \frac{a_{AT}}{3}\right)$$

Onde $l_m = 2\pi r_m$ é o comprimento médio da trajetória do fluxo de dispersão e $h_{eq}$ é a altura equivalente dos enrolamentos.

> Os termos $a/3$ dos enrolamentos (e não $a$ inteiro) surgem porque o campo dentro do enrolamento **cresce linearmente** de 0 a $H_{max}$ — a contribuição efetiva ao fluxo concatenado é 1/3 da que seria se H fosse constante.

---

## 7. Perdas Magnéticas no Núcleo

### 7.1 Perdas por Histerese

Cada ciclo completo de magnetização percorre o laço de histerese B-H. A área desse laço representa a energia dissipada por unidade de volume a cada ciclo:

$$w_h = \oint H \, dB \qquad [\text{J/m}^3\text{/ciclo}]$$

A potência dissipada por histerese:

$$\boxed{P_h = K_h \times f \times B_{max}^n \times V_{nucleo}}$$

Onde:
- $K_h$: constante do material (depende do aço-silício)
- $n$: expoente de Steinmetz, tipicamente **1,6–2,0** para aço-silício de grão orientado
- $f$: frequência
- $V_{nucleo}$: volume do núcleo

**Equação de Steinmetz (1892):** $P_h \propto f \times B_{max}^{1,6}$ (expoente original de Steinmetz para aço comum)

Para grão orientado moderno: $n \approx 1,8$ a $2,0$.

> **Nota física:** A histerese ocorre porque os domínios magnéticos do aço resistem à reversão — as "paredes de domínio" se movem com atrito. Quanto mais puro e orientado o cristal, menor a área do laço e menor $K_h$. É por isso que chapas M4 de grão orientado têm perdas muito menores que chapas comuns.

### 7.2 Perdas por Correntes Parasitas (Foucault)

O fluxo variável no núcleo induz tensões (Lei de Faraday) que circulam como correntes no próprio aço — as correntes de Foucault. A potência dissipada:

$$\boxed{P_e = K_e \times f^2 \times B_{max}^2 \times t^2 \times V_{nucleo}}$$

Onde $t$ é a espessura da chapa.

**Origem:** $P_e \propto t^2$ → chapas mais finas reduzem quadraticamente as perdas por Foucault. Por isso as chapas M4-0,27 mm são usadas em vez de chapas mais espessas: $0{,}27^2 = 0{,}073$ vs. $0{,}35^2 = 0{,}123$ → **41% menos perdas de Foucault** com a chapa mais fina.

A tensão induzida em uma faixa de largura $w$ e espessura $t$:
$$e_{Foucault} \approx \pi f B_{max} w t$$

A corrente de Foucault e a potência dissipada crescem com $w^2 t^2$ — por isso dividir o último pacote (reduzir $w$) reduz drasticamente as perdas: cortar ao meio reduz para $1/4$ das perdas por Foucault naquele pacote.

### 7.3 Perdas Totais no Núcleo (Ferro)

$$\boxed{P_{Fe} = P_h + P_e = \left(K_h f B_{max}^n + K_e f^2 B_{max}^2 t^2\right) \times V_{nucleo}}$$

Em termos de W/kg (como na planilha):
$$p_{Fe} = K_h f B_{max}^n + K_e f^2 B_{max}^2 t^2 \qquad [\text{W/kg}]$$

**Identificação dos termos na planilha (ADA DATA CENTER):**

A 100% Vn, f = 60 Hz:
```
p_base = 1,54 W/kg    (da curva da chapa, termo puro da chapa M4-0,27mm)
p_projeto = 1,69 W/kg  (com fatores construtivos: juntas, corte, etc.)

P_Fe = 1,69 × 17.597 = 29.740 W ≈ 29.786 W declarado  ✓
```

### 7.4 Separação de Histerese e Foucault pela frequência

Para separar $K_h$ e $K_e$ experimentalmente, divide-se por $f \times B_{max}^2$:

$$\frac{P_{Fe}}{f \times B_{max}^2} = K_h \times B_{max}^{n-2} + K_e \times f \times t^2$$

Plotando o lado esquerdo vs. $f$ para B constante: intercepto = $K_h B^{n-2}$, inclinação = $K_e t^2$.

### 7.5 Ângulo de Perda δ e Fator de Potência do Ferro

A corrente de excitação tem duas componentes:

$$\vec{I_0} = \vec{I_{mag}} + \vec{I_{Fe}}$$

- $I_{Fe}$ (em fase com V): supre as perdas no ferro → $P_{Fe} = V \times I_{Fe}$
- $I_{mag}$ (90° atrasado de V): cria o fluxo → reativa

$$\cos\delta_{Fe} = \frac{I_{Fe}}{I_0} = \frac{P_{Fe}}{V \times I_0}$$

Para este transformador a 100% Vn, ONAF:
```
I_0 = 0,30% × I_n,AT = 0,30% × 167,4 = 0,502 A
P_Fe = 29.828 W (garantido)
V_AT = 138.000 / √3 = 79.674 V (fase)

I_Fe = P_Fe / (3 × V_AT) = 29.828 / (3 × 79.674) = 0,125 A/fase  (AT)
I_mag = √(I_0² − I_Fe²) = √(0,502² − 0,125²) = √(0,252 − 0,016) = 0,486 A

cos δ_Fe = 0,125 / 0,502 = 0,249  → ângulo de perda δ = 75,6°
```

---

## 8. Equações Fundamentais do Transformador

### 8.1 Transformador Ideal

**Relação de tensões:**
$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = a$$

**Relação de correntes:**
$$\frac{I_1}{I_2} = \frac{N_2}{N_1} = \frac{1}{a}$$

**Conservação de potência:**
$$V_1 I_1 = V_2 I_2 \implies S_1 = S_2$$

**Reflexão de impedâncias:**
$$Z_1 = a^2 \times Z_2$$

Uma impedância no secundário vista do primário é multiplicada por $a^2$.

### 8.2 Equação da FEM (repetição com foco em projeto)

$$\boxed{E = 4{,}44 \times f \times N \times B_{max} \times A_{nucleo}}$$

Esta equação permite calcular qualquer uma das grandezas se as outras são conhecidas:

```
Dado E, f, N, A  →  B_max = E / (4,44 × f × N × A)         [verificar saturação]
Dado E, f, B, A  →  N = E / (4,44 × f × B × A)              [número de espiras]
Dado E, f, B, N  →  A = E / (4,44 × f × B × N)              [seção do núcleo]
Dado N, f, B, A  →  E = 4,44 × f × N × B × A               [tensão induzida]
```

### 8.3 Balanço de Ampère-Espiras (NI)

Em regime permanente, a Lei de Ampère aplicada ao núcleo:

$$N_1 I_1 - N_2 I_2 = N_1 I_0$$

Onde $I_0$ é a corrente de excitação. Como $I_0 \ll I_1$, na prática:

$$N_1 I_1 \approx N_2 I_2 \implies I_1 N_1 = I_2 N_2$$

**Interpretação física:** o enrolamento primário fornece os ampère-espiras que o secundário consome. O núcleo é apenas o "mediador" — não armazena NI em regime permanente (toda a MMF aplicada cai na relutância do núcleo, que é muito baixa).

> **Nota de estudo:** O desequilíbrio de NI (como os −18 A·esp do tap 17 no cálculo do último pacote) representa o "excesso" de NI que não se cancela entre primário e secundário — esse excesso cria campo de dispersão externo ao núcleo.

### 8.4 Potência Aparente, Ativa e Reativa

$$S = \sqrt{3} \times V_L \times I_L \qquad [\text{VA ou kVA ou MVA}]$$
$$P = S \cos\varphi \qquad [\text{W}]$$
$$Q = S \sin\varphi \qquad [\text{VAr}]$$

**Para o transformador em si (perdas):**
$$P_{total} = P_{Fe} + P_{Cu} = P_{vazio} + P_{carga}$$

Onde $P_{Cu} = 3 I^2 R$ (perdas resistivas nos enrolamentos).

---

## 9. Circuito Equivalente

### 9.1 Circuito Equivalente Completo (Modelo T)

```
   R1       jX1         jXm  R_Fe       R2'      jX2'
───┤├───────┤├──────┬──┤├──┤├──┬─────┤├────────┤├───
  (prim.)  (disp.) │ (mag.) (Fe)│  (resist.)  (disp.)
  (AT)      (AT)   │           │     (BT ref.)  (BT ref.)
                  ─┴─         ─┴─
                  GND         GND
```

Onde:
- $R_1, R_2'$: resistências dos enrolamentos AT e BT (referidas ao AT)
- $jX_1, jX_2'$: reatâncias de dispersão AT e BT
- $jX_m$: reatância de magnetização (alto valor — corrente de excitação pequena)
- $R_{Fe}$: resistência equivalente das perdas no ferro

### 9.2 Circuito Simplificado (para cálculos de carga)

Como $X_m \gg X_1 + X_2'$, o ramo de magnetização pode ser deslocado para os terminais de entrada:

```
   R_cc = R1+R2'    jX_cc = j(X1+X2')
───────┤├──────────────┤├───────────────
   (impedância de curto-circuito total)
```

Impedância de curto-circuito total referida ao AT:
$$Z_{cc} = R_{cc} + jX_{cc}$$

$$Z\% = \frac{Z_{cc} \times I_n}{V_n/\sqrt{3}} \times 100 = \frac{Z_{cc}}{Z_{base}} \times 100$$

### 9.3 Parâmetros do Circuito a partir de Ensaios

**Ensaio em vazio** → determina o ramo de magnetização:
$$R_{Fe} = \frac{V_0^2}{P_0} \qquad X_m = \frac{V_0^2}{Q_0} = \frac{V_0^2}{\sqrt{S_0^2 - P_0^2}}$$

**Ensaio de curto-circuito** → determina a impedância série:
$$Z_{cc} = \frac{V_{cc}}{I_n} \qquad R_{cc} = \frac{P_{cc}}{I_n^2} \qquad X_{cc} = \sqrt{Z_{cc}^2 - R_{cc}^2}$$

**Aplicação (ADA DATA CENTER, tap nominal, ONAF):**
```
Z_cc = Z% × V_base / (√3 × I_n,AT) = 10,0% × (138.000/√3) / 167,4 = 47,61 Ω
R_cc = R% × Z_base = 0,525% × 475,6 = 2,50 Ω  (com perdas garantidas 210 kW)
X_cc = √(Z_cc² − R_cc²) = √(47,61² − 2,50²) = 47,54 Ω  →  X% = 9,99%
```

---

## 10. Impedância de Curto-Circuito — Origem Física

### 10.1 A impedância é o fluxo de dispersão armazenado

$$X_{cc} = \omega (L_{\sigma,AT} + L_{\sigma,BT}) = 2\pi f \times L_{\sigma,total}$$

A reatância de dispersão armazena energia no campo magnético do óleo entre os enrolamentos. Esta energia é o que limita a corrente de curto-circuito.

### 10.2 Fórmula de Projeto da Reatância de Dispersão

$$\boxed{X_{cc}\% = \frac{2\pi f \mu_0 K_R (NI)^2}{S_n} \times \frac{1}{h_{eq}} \times \left(\frac{a_{BT}}{3} + a_{gap} + \frac{a_{AT}}{3}\right) \times l_m}$$

Onde:
- $(NI)^2 = (N_1 I_1)^2$ = produto de ampère-espiras ao quadrado
- $h_{eq}$ = altura equivalente dos enrolamentos
- $a_{BT}, a_{AT}$ = espessuras radiais dos enrolamentos
- $a_{gap}$ = largura do gap entre enrolamentos
- $l_m$ = comprimento médio da trajetória de dispersão
- $K_R$ = fator de Rogowski

**Implicações de projeto:**
- Aumentar $a_{gap}$ → aumenta X% (mais fluxo de dispersão)
- Aumentar $h_{eq}$ → diminui X% (campo distribuído em maior altura)
- Aumentar N → aumenta X% proporcionalmente a $N^2$

### 10.3 Por que X% = 10% para este transformador?

É uma especificação normativa/contratual para sistemas de 138 kV. Um X% maior:
- **Vantagem:** limita mais a corrente de curto-circuito
- **Desvantagem:** maior queda de tensão em carga, maior regulação de tensão

Um X% menor:
- **Vantagem:** menor queda de tensão, melhor regulação
- **Desvantagem:** corrente de curto-circuito maior → equipamentos de proteção mais caros

Para data centers, X% ≈ 10% é típico: equilibra proteção do sistema com qualidade de tensão para as cargas de TI sensíveis.

---

## 11. Força Eletrodinâmica nos Enrolamentos

### 11.1 Força sobre um condutor

$$d\vec{F} = I \, d\vec{l} \times \vec{B}$$

Para um condutor de comprimento $l$ em campo uniforme $B$:
$$F = B \times I \times l \qquad [\text{N}]$$

### 11.2 Forças em curto-circuito

Em curto-circuito, $I_{cc} = I_n / (Z\% / 100)$. As forças crescem com $I^2$:

$$F_{cc} \propto I_{cc}^2 = \left(\frac{I_n}{Z\%/100}\right)^2 = \left(\frac{100}{Z\%}\right)^2 \times I_n^2$$

Para Z% = 10%: $F_{cc} = 100 \times F_{nominal}$

**Forças axiais** (tendem a comprimir/expandir os enrolamentos axialmente):
$$F_{axial} \propto I^2 \times B_{r}$$

Surgem do produto da corrente pelo campo radial $B_r$ de dispersão. São as mais perigosas mecanicamente — tendem a "empurrar" um enrolamento contra o outro ou contra as culatras.

**Forças radiais** (tendem a expandir o enrolamento externo e comprimir o interno):
$$F_{radial} \propto I^2 \times B_{a}$$

Surgem do produto da corrente pelo campo axial $B_a$ de dispersão.

**Aplicação (ADA DATA CENTER):**
```
I_cc,BT = I_n,BT / (Z%/100) = 669,4 / 0,10 = 6.694 A
F relativa = I_cc² / I_n² = (1/0,10)² = 100×  →  forças 100× maiores que em regime
```

> **Nota de estudo:** É por isso que os enrolamentos são rigidamente prensados e os condutores têm alta resistência mecânica (Rp02 = 120 N/mm² para o cobre dos enrolamentos AT e BT deste projeto). O cobre recozido comum tem Rp02 ≈ 70 N/mm² — insuficiente para transformadores de potência.

---

## 12. Notas de Estudo — Pontos Críticos

### ⚠️ Relações que devem ser memorizadas

```
E = 4,44 × f × N × Φ_max = 4,44 × f × N × B_max × A   ← equação-mãe
Φ = B × A                                                ← definição
H = B / (μ₀ μᵣ)                                          ← propriedade do material
F = N × I                                                ← MMF
R = l / (μ × A)                                          ← relutância
F = Φ × R                                                ← Hopkinson
λ = N × Φ                                                ← fluxo concatenado
L = λ / I = N² / R                                       ← indutância
Z% = √(R%² + X%²)                                        ← impedância
R% = Pcc / S × 100                                       ← componente resistiva
X% = √(Z%² - R%²)                                        ← componente reativa
```

### ⚠️ Relações entre domínios que confundem no início

| O que muda | O que sobe | O que cai | Por quê |
|---|---|---|---|
| Aumentar N (espiras) | V induzida, L, Z_cc | I (para mesma S) | E ∝ N; I ∝ 1/N |
| Aumentar B_max | Perdas no ferro | N necessário | P_Fe ∝ B^1,8; N = E/(4,44×f×B×A) |
| Aumentar a_gap (dist. AT-BT) | X%, fluxo dispersão | — | X% ∝ a_gap |
| Aumentar h (altura bobina) | — | X% | X% ∝ 1/h_eq |
| Aumentar espessura chapa t | Perdas Foucault | — | P_e ∝ t² |
| Aumentar frequência | X_cc, P_e | N necessário | X = ωL; P_e ∝ f²; N = E/(4,44×f×B×A) |
| Tap negativo (menos espiras AT) | I_AT, P_cc_AT | V_BT (se não compensado) | I = S/(√3×V); P ∝ I² |

### ⚠️ Armadilhas comuns em projeto

**1. Confundir tensão de linha com tensão de fase em delta/estrela:**
- Delta: $V_{fase} = V_{linha}$, $I_{fase} = I_{linha}/\sqrt{3}$
- Estrela: $V_{fase} = V_{linha}/\sqrt{3}$, $I_{fase} = I_{linha}$
- O número de espiras é calculado com a **tensão de fase** (tensão que cada bobina vê)

**2. Usar corrente nominal em vez de corrente máxima para o condutor:**
- O condutor AT deve ser dimensionado para a corrente no **tap de menor tensão** (máxima corrente), não no tap nominal

**3. Aplicar a equação E = 4,44fNΦ no valor de linha:**
- A equação se aplica à tensão **por fase** e ao fluxo **por coluna** do núcleo

**4. Esquecer o fator de Rogowski:**
- A reatância de dispersão calculada sem $K_R$ é superestimada em 3–10%

**5. Assumir μᵣ constante:**
- $\mu_r$ do aço-silício varia de ~10.000 (campo baixo) a ~1.000 (campo alto/saturação) — qualquer cálculo de relutância ou indutância que usa $\mu_r$ fixo é válido apenas em uma faixa estreita de B

**6. Confundir perdas em vazio com perdas em carga:**
- Perdas em vazio ($P_{Fe}$): constantes, existem sempre que energizado, independem da carga
- Perdas em carga ($P_{Cu}$): variam com $I^2$, zero sem carga

### ⚠️ Ligações entre os tópicos deste arquivo e o projeto ADA DATA CENTER

| Equação / conceito | Onde aparece no projeto |
|---|---|
| $E = 4,44fNB_{max}A$ | Volt/espira = 108,25 V → B = 1,723 T, A = 2356,65 cm² |
| Curva B-H (saturação) | Perdas vazio crescem 2,7× de 90% para 110% Vn |
| $P_e \propto t^2$ | Chapa M4-0,27 mm escolhida para minimizar Foucault |
| Campo radial Hr | Cálculo do último pacote → NÃO é necessário dividir |
| Fluxo concatenado λ | Base da indutância de dispersão → X% = 10,11% |
| Fator de Rogowski $K_R$ | Correção do X% na EPA |
| $F_{cc} \propto I^2$ | Rp02 = 120 N/mm² dos condutores (resistência mecânica) |
| $X\% = \sqrt{Z\%^2 - R\%^2}$ | X% = 9,99% garantido a partir de Z%=10%, P_cc=210kW |
| $I_{max} = S/(\sqrt{3} \times V_{min})$ | Corrente máxima AT = 185,9 A no tap 17 (não 167,4 A nominal) |
| Desequilíbrio NI | −18 A·esp no tap 17 → Hr → verificação do último pacote |

---

*Arquivo de referência — pasta `03 Estudos/EPA/`*
*Ver também: [[ADA DATA CENTER estudo/CORE]] | [[ADA DATA CENTER estudo/Níveis de Isolação]] | [[ADA DATA CENTER estudo/Núcleo — Último Pacote e Curvas de Perda]]*
