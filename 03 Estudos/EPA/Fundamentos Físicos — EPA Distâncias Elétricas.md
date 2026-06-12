# Fundamentos Físicos e Teoria Analítica — EPA Distâncias Elétricas

> Análise baseada na planilha **C19163865** — 32/40 MVA ONAN/ONAF, 138/34,5 kV, Dyn1, cliente ADA DATA CENTER. Norma ABNT NBR 5356/2007.

---

## Abas da planilha e o que cada uma calcula

| Aba | Função |
|-----|--------|
| `Dados_DTDS` | Dados de entrada: tensões, níveis de isolamento, geometria do núcleo |
| `Folha 1` | Dados construtivos dos enrolamentos BT1, AT1, AT2 |
| `Folha 2` | Taps, escalonamento do núcleo, blindagem magnética |
| `Folha 3` | Perdas e impedância de curto-circuito (3 taps extremos + nominal) |
| `Folha 4` | Matriz DDI — diferença dielétrica máxima entre todos os nós |
| `Campo` | Distribuição capacitiva de campo nos canais isolantes |
| `TRANEM-BT / TRANEM-AT` | Verificação de impulso disco a disco nos enrolamentos |
| `FCC` | Esforços de curto-circuito — método de Rabins (NBR 5356-5) |
| `DDI Máx` | Interface EMTP — varredura de todas as condições de ensaio |
| `Vida Útil` | Envelhecimento térmico do isolamento (IEC 60076-7) |
| `Blindagem` | Cálculo da blindagem magnética nas paredes do tanque |
| `Check List` | Verificações finais de conformidade |

---

## 1. Dados_DTDS — A Base de Tudo

### 1.1 O que é a aba Dados_DTDS

É o ponto de entrada único: todos os outros módulos leem daqui. Qualquer erro aqui se propaga para todas as verificações.

### 1.2 Configuração do transformador 19163865

```
Potência:     32.000 kVA (ONAN) / 40.000 kVA (ONAF)
AT:           138.000 V linha → classe 145 kV → NBI 650 kVp → TP 275 kV
              Onda cortada: 715 kVp
BT:           34.500 V linha → classe 36,2 kV → NBI 200 kVp → TP 70 kV
NBT:          classe 36,2 kV → NBI 170 kVp → TP 70 kV
Grupo:        Dyn1 (delta AT, estrela-neutro BT, defasagem 30°)
Taps:         8×1,25% acima e abaixo → 17 posições (151.800 V a 124.200 V)
Comutador:    ABB UZFRT 650 150 17P (OLTC — regulação sob carga)
```

### 1.3 Por que a tensão de classe (Um) define o nível de isolamento

A tensão nominal de linha é 138 kV. O sistema opera em 138 kV, mas pode ter variações permanentes de ±5–10%. A norma então adota a **tensão máxima contínua do sistema Um = 145 kV**, que é o valor de catálogo da classe. A partir de Um, a norma define os pares de ensaio possíveis:

- Um = 145 kV → NBI: 550 ou **650** kVp (escolhido 650) → TP: 230 ou **275** kV (escolhido 275)

O par (650 kVp / 275 kV) é mais exigente e representa um transformador com maior nível de proteção. Essa escolha impacta diretamente todas as dimensões internas.

> [!important] Por que NBI e TP são ensaios diferentes
> O NBI (Nível Básico de Impulso) simula um raio: onda 1,2/50 μs — sobe em 1,2 μs e decai a 50% em 50 μs. O mecanismo de ruptura é **streamer** — propagação de canal ionizado a alta velocidade. O campo precisa ser alto o suficiente para iniciar e propagar o streamer antes que a onda passe.
>
> O TP (tensão de prova a frequência industrial) opera a 60 Hz por 1 minuto. O mecanismo é diferente: **ionização por colisão acumulada**, liberação de gás por descargas parciais, formação de bolhas. O campo admissível é bem menor porque há tempo para os mecanismos de degradação agirem.
>
> Por isso as distâncias calculadas para NBI e TP são independentes — a **maior delas governa** o projeto.

> [!tip] Estudar em paralelo
> - Teoria de streamer em líquidos dielétricos (modelo de Devins-Rzad)
> - Forma de onda normalizada 1,2/50 μs — IEEE Std 4
> - Coordenação de isolamento: IEC 60071-1 e IEC 60071-2

### 1.4 NBT — Por que NBI 170 kVp e não 200 kVp como o BT

O NBT (Neutro de Baixa Tensão) está na bucha X0. Em regime permanente, numa estrela perfeitamente equilibrada, o neutro está no potencial de terra — tensão zero. O isolamento reduzido é uma economia legítima para esse regime.

O problema vem dos **transitórios**:

1. **Transferência capacitiva AT→neutro:** uma frente de onda que entra pela bucha AT se transfere capacitivamente para o enrolamento BT. A tensão no neutro pode ser significativa, proporcional à relação capacitiva entre os enrolamentos.

2. **Ressonância em transitórios de manobra:** o neutro não está no nó de menor tensão durante a frente de onda de impulso — a distribuição de tensão dentro do enrolamento é capacitiva, não uniforme.

Por isso o NBT tem um NBI reduzido (170 kVp) **mas não zero**: o projeto tem que garantir que a tensão que chega ao neutro durante os ensaios de impulso não exceda 170 kVp. Isso é verificado pela **aba Folha 4 (DDI)** e confirmado pelos cálculos EMTP na **aba DDI Máx**.

> [!important] Ponto crítico do NBT
> O nó X0 (NBT) tem na matriz DDI (Folha 4): impulso 200 kVp em relação à terra. Se esse valor exceder o NBI do NBT (170 kVp), o projeto é reprovado dielétrico. Na aba DDI, a linha do nó X0/1 mostra 200 [75] para terra — que corresponde exatamente ao nível do BT (200 kVp) e não ao NBI reduzido do neutro. Isso merece revisão: ou o neutro está sendo ensaiado com o nível do BT (aceitável se há justificativa técnica) ou há conservadorismo intencional.

### 1.5 Núcleo — dados geométricos de entrada

```
Diâmetro da coluna:  582 mm
Altura da janela:    1.350 mm
Entre eixos:         1.130 mm (passo entre colunas)
Indução:             1,7232 T
Seção:               2.356,65 cm²
Tipo:                Core-Type 3 colunas, convencional
Chapa:               M4-0,27 mm WEG TF (grão orientado, GO)
Canais no núcleo:    2 canais de 6 mm cada, no 3º degrau
```

> [!important] Por que o núcleo tem degraus
> A coluna não é redonda — ela é aproximada por um polígono inscrito num círculo de 582 mm de diâmetro. São 13 degraus de chapas de diferentes larguras (560, 540, 520... até 220 mm). Cada degrau tem espessura calculada para maximizar a seção transversal dentro do círculo.
>
> A área do círculo de 582 mm é π×291² = 266.225 mm². A seção efetiva das chapas é 2.356,65 cm² = 235.665 mm². O **fator de utilização da seção** é 235.665/266.225 = **88,5%** — valor típico para núcleos de 13 degraus.
>
> A diferença (11,5%) é espaço ocupado pelos canais de resfriamento (2×6mm), pelos arredondamentos e pelo afastamento entre chapas.

> [!tip] Estudar em paralelo
> - Geometria escalonada de colunas: maximização de seção inscrita
> - Chapas de grão orientado (GO): anisotropia magnética, perdas por histerese e correntes de Foucault
> - Indução de projeto vs. indução de saturação (Bsat ≈ 2,03 T para Si-GO)
> - Fator de enchimento de empacotamento (stacking factor) ≈ 0,96–0,97 para 0,27 mm

---

## 2. Folha 1 — Enrolamentos: Construção e Geometria

### 2.1 Os três enrolamentos do transformador 19163865

```
BT1:  Disco (DC)       — 78 discos, 2,5 espiras/disco, CTC WEG
AT1:  Disco interleaved — 16DE + 60DC + 16DE = 92 discos, 14 espiras/disco
AT2:  Hélice Múltipla C — 1 camada, 128 espiras, 8 degraus, 16 espiras/degrau (RAT)
```

A geometria calculada resulta em:

| Enrolamento | Φ interno (mm) | Φ externo (mm) | Altura elétrica (mm) |
|-------------|---------------|----------------|----------------------|
| BT1 | 626 | 748 | 1.120 |
| AT1 | 834 | 992 | 1.080 |
| AT2 (RAT) | 1.072 | 1.094 | 885,5 |

A sequência radial a partir do núcleo é: **Núcleo → Canal → BT1 → Canal → AT1 → AT2(RAT)**

### 2.2 Física dos canais de óleo entre enrolamentos

O canal entre BT1 e o núcleo (raio do núcleo = 291 mm, Φ_int BT = 626 mm → raio interno = 313 mm):

$$e_{canal,núcleo-BT} = 313 - 291 = 22\ \text{mm}$$

Esse canal tem dupla função:

**Função elétrica:** o núcleo está aterrado (potencial zero). A distância de 22 mm precisa suportar a tensão de fase do BT em relação à terra — mas como o núcleo tem blindagem eletrostática (verificado na aba Campo), a tensão real no canal é redistribuída capacitivamente. A aba **Campo** mostra que o campo efetivo no canal é 3,62 kV/mm com margem de segurança de 109% — apenas marginalmente seguro.

**Função térmica:** é por esse canal que o óleo sobe do fundo do tanque para resfriar as faces internas do enrolamento BT. Canais com menos de ~8 mm reduzem drasticamente a vazão de óleo por convecção natural.

O canal entre AT1 e BT1 (Φ_ext BT = 748 mm → raio 374 mm; Φ_int AT = 834 mm → raio 417 mm):

$$e_{canal,BT-AT} = 417 - 374 = 43\ \text{mm}$$

Esse é o **canal principal de isolação** (main insulation duct) — o mais crítico eletricamente. A tensão entre AT e BT pode chegar a 275 kV (TP) ou 650 kVp (NBI). A aba Campo mostra para este canal: TP = 275 kV aplicados, margem mínima encontrada de **24%** (mínima desejada 20%) — situação de relativa tensão no projeto.

> [!important] A não-linearidade do campo elétrico no canal AT-BT
> O campo num canal cilíndrico entre dois cilindros de diâmetros diferentes NÃO é uniforme. Para cilindros coaxiais, o campo é máximo na superfície interna (menor diâmetro):
>
> $$E(r) = \frac{U}{r \cdot \ln(r_{ext}/r_{int})}$$
>
> O campo na superfície do BT (r = 374 mm) é maior que na superfície do AT (r = 417 mm). Por isso o revestimento de papel isolante no BT (camada externa) é dimensionado para suportar o campo mais intenso.
>
> Na aba Campo, os "cilindros" (pressboard barriers) redistribuem o campo. Com múltiplas barreiras, o sistema funciona como capacitores em série — cada barreira impede a propagação de streamers e redistribui a tensão para os canais de óleo. Isso é verificado calculando o campo em cada canal individualmente.

> [!tip] Estudar em paralelo
> - Distribuição de campo em geometria cilíndrica coaxial (Laplace em coordenadas cilíndricas)
> - Efeito de barreiras de pressboard: modelo capacitivo em série
> - Rigidez dielétrica do óleo mineral: curva E_bd = f(distância) — relação não linear!
> - Conceito de canal de óleo "zig-zag" e canal direto no fluxo de óleo dirigido (DOF)

### 2.3 Tipos de enrolamento e por que importam eletricamente

#### BT1 — Enrolamento de disco (DC) com CTC

O CTC (Continuously Transposed Cable) é um cabo formado por múltiplos fios achatados transpostos continuamente. Neste transformador: **13 condutores de 4,7×1,4 mm** reunidos num cabo de 10,545×11,79 mm.

A transposição serve para equalizar o fluxo que envolve cada fio dentro do cabo — sem transposição, correntes circulantes entre os fios aumentariam as perdas parasitas. A nota na planilha indica **Transposição: No** — isso significa que o CTC já tem a transposição interna ao cabo, não precisa de transposição adicional do condutor no enrolamento.

**Disco duplo:** 2 bobinas em série formando um bloco. O espaçador entre discos (4 mm, 66 espaçadores + 4×5 mm + 7×5 mm zig-zag) é o caminho do óleo — se muito estreito, o canal fica bloqueado; se muito largo, aumenta a altura do enrolamento.

#### AT1 — Disco interleaved (DCI): 16DE + 60DC + 16DE

A sigla **DE = Disc Entrelazado (Interleaved)** e **DC = Disc Comum (Standard)**. O interleaving é a técnica mais importante para controle da distribuição de tensão sob impulso.

**Por que fazer interleaving?**

Num enrolamento de disco comum (DC), a distribuição de tensão sob impulso é altamente não uniforme. O capacitor série (entre espiras adjacentes) e o capacitor shunt (entre o disco e a terra/outros enrolamentos) formam um divisor capacitivo. O resultado é que a maior parte da tensão de impulso cai nos primeiros e últimos discos da bobina — os discos nas extremidades ficam com tensão muito mais alta por espira do que os discos no meio.

A **distribuição alfa (α)** quantifica isso:

$$\alpha = H \cdot \sqrt{\frac{C_g}{C_s}}$$

Onde:
- $C_g$ = capacitância shunt (disco-terra + disco-outros enrolamentos)
- $C_s$ = capacitância série (entre espiras consecutivas do enrolamento)
- $H$ = altura total do enrolamento

Para α >> 1: a tensão na entrada do enrolamento é quase toda na primeira espira — situação catastrófica.

No interleaving, os discos são bobinados de forma que espiras alternadas pertencem a discos separados. Isso aumenta drasticamente a capacitância série $C_s$ (por um fator de 4 ou mais), reduzindo α e tornando a distribuição de tensão muito mais uniforme.

A estrutura **16DE + 60DC + 16DE** deste transformador usa interleaving apenas nas extremidades (os 16 discos de entrada e saída), onde a distribuição capacitiva é mais crítica. Os 60 discos centrais usam DC porque a tensão lá já é mais uniforme e o interleaving seria custo sem benefício significativo.

> [!important] Verificação disco a disco na aba TRANEM-AT
> A aba TRANEM-AT verifica exatamente essa distribuição. Para cada nó (disco ou par de discos) ela calcula:
> - **Tensão radial** (kV): tensão entre a superfície do disco e os enrolamentos adjacentes
> - **Tensão axial entre discos** (kV): tensão entre discos consecutivos — é o que estou chamando de "entre discos" na coluna 13
> - **Tensão entre espiras** (kV): tensão local que o papel isolante do condutor precisa suportar
>
> Para o AT1: tensão entre espiras máxima = **4 kV** (margem 16,56×) — muito folga. A crítica é o **corner do espaçador** com margem **2,07×** — o ponto mais estressado eletricamente de todo o enrolamento AT. Isso ocorre porque o canto do espaçador concentra o campo elétrico (efeito de borda).

> [!important] Miniângulo
> Na planilha TRANEM, o parâmetro **Miniângulo (S)** ativa um modelo de cálculo que considera o ângulo entre o espaçador e o disco. Quando há miniângulo, o campo no canto é menos concentrado. A planilha confirma o uso de miniângulo em ambos os enrolamentos.

#### AT2 — Hélice Múltipla Tipo C (RAT)

O AT2 é o **enrolamento de regulação** (RAT — Resistência de Amortecimento/Transição? Não — aqui RAT = Regulação em AT). É o enrolamento que o comutador OLTC adiciona ou remove espiras para regular a tensão.

**Hélice Múltipla Tipo C:** cada "camada" tem múltiplos condutores em paralelo que percorrem a altura da bobina em forma de hélice. O tipo C indica a forma construtiva das transições entre degraus.

Com 8 degraus e 16 espiras por degrau, o RAT fornece 128 espiras totais — e como cada tap altera 1.25% da tensão AT (= 1,25% × 1274 espiras AT1 = ~16 espiras por tap), cada degrau do RAT corresponde exatamente a 1 tap.

O RAT fica na posição mais externa (Φ 1.072–1.094 mm) porque:
1. Está em série com o AT1, então tem tensão da ordem de AT (650 kVp de isolação para terra)
2. Por ser externo, facilita o acesso dos leads do comutador
3. A radial de apenas 11 mm indica que este enrolamento tem poucos condutores por camada — confirmado: 1 camada, condutores 4,2×8,5 mm

> [!tip] Estudar em paralelo
> - Distribuição de tensão em enrolamentos de disco sob impulso: método das linhas de transmissão
> - Coeficiente de não-uniformidade α e seu impacto na tensão entre espiras
> - Interleaving (entrelazado): como a construção física muda a capacitância série
> - Tipos de enrolamentos: hélice simples, hélice múltipla, disco, disco entrelazado — critérios de escolha

---

## 3. Folha 2 — Taps, Geometria do Núcleo e Blindagem Magnética

### 3.1 Os 17 taps e o que eles significam para o estudo de distâncias elétricas

```
Tap 1:  151.800 V (138 kV × (1 + 8×1,25%))  — tensão máxima
Tap 9:  138.000 V — tensão nominal
Tap 17: 124.200 V (138 kV × (1 - 8×1,25%)) — tensão mínima
```

O tap que mais estresa o isolamento elétrico **não é necessariamente o nominal**. Em tap 1 (maior tensão), o enrolamento AT tem mais espiras → as espiras do RAT que estão em circuito têm tensão diferencial mais alta em relação às que estão fora. Em tap 17 (menor tensão), o RAT está com parte de suas espiras curto-circuitadas pelo comutador, criando configurações geométricas diferentes.

A planilha verifica as perdas e impedâncias em três taps: 1, 9 e 17. A **Folha 4 (DDI)** faz a varredura completa em todos os 17 taps para encontrar a pior combinação.

### 3.2 Escalonamento do núcleo e o cálculo da seção

A seção efetiva do núcleo determina a tensão por espira:

$$V_{esp} = \frac{U_{nom}}{\sqrt{2} \cdot \pi \cdot f \cdot N} = 4{,}44 \cdot f \cdot N \cdot B \cdot A_{Fe}$$

Para este transformador: $V_{esp} = 108{,}25\ \text{V}$, $f = 60\ \text{Hz}$, $B = 1{,}7232\ \text{T}$, $A_{Fe} = 2.356{,}65\ \text{cm}^2$:

$$N_{AT} = \frac{138.000/\sqrt{3}}{108,25} = \frac{79.674}{108,25} \approx 736\ \text{espiras por fase (estrela)}$$

Mas como o AT está em **delta**, a tensão de fase = tensão de linha = 138.000 V:

$$N_{AT} = \frac{138.000}{108,25} \approx 1.275\ \text{espiras} \quad ✓ \text{(confirma planilha: 1.274–1.402 no range de taps)}$$

> [!important] Indução de trabalho 1,7232 T
> A chapa M4-0,27 mm WEG TF (grão orientado) tem Bsat ≈ 2,03 T. A indução de trabalho de 1,7232 T representa **84,9% da saturação** — alto, mas aceitável. A perda específica desta chapa a 1,7 T/60 Hz é ~1,7 W/kg (confirma planilha: 1,7 W/kg).
>
> Trabalhar com indução alta reduz a seção do núcleo (menos material, menor custo) mas aumenta:
> - Perdas no ferro (proporcional a $B^{1,6}$ a $B^2$ dependendo do regime)
> - Corrente de excitação (crescimento não-linear acima de ~1,5 T)
> - Risco de sobreexcitação acidental (se a tensão subir 10%, a indução vai a ~1,9 T)
>
> A planilha confirma: perdas em vazio crescem de 29.828 W (100% Vn) para 46.109 W (110% Vn) — aumento de 55% para 10% de sobretensão, evidenciando a não-linearidade da curva B×H próxima à saturação.

### 3.3 Blindagem magnética: S1, S3, S4 — mas não S2

A planilha registra:
```
S1 (lateral): Sim — blindagem magnética (E=10mm, H=1450mm)
S2 (BT):      Não
S3 (AT):      Sim
S4 (lateral): Sim
```

**Por que blindagem magnética nas paredes do tanque?**

O fluxo de dispersão dos enrolamentos (que não passa pelo núcleo) percorre o caminho de retorno pelo óleo e pelo tanque. Quando esse fluxo entra nas paredes de aço do tanque, induz correntes parasitas que geram perdas — estas são as **perdas por dispersão** (parte do Wtot = 188.325 W calculados na Folha 3, onde $k = 1,9$ na linha "Perdas por Dispersão" para o tap nominal).

A blindagem magnética é uma lâmina condutora (alumínio ou cobre) que, pelo efeito pele, impede o fluxo de penetrar na parede de aço. A blindagem mesma aquece — mas muito menos do que aqueceria o aço.

**Por que não em S2?** O lado S2 fica oposto às buchas BT. As correntes de BT (669,4 A máx) geram campo magnético intenso na região das buchas — mas na parede S2 oposta a esse campo (o lado do tanque que não tem buchas) o fluxo é menor. A decisão de não blindar S2 é um compromisso custo×perdas: os engenheiros avaliaram que as perdas em S2 sem blindagem são aceitáveis para o contrato deste transformador.

> [!tip] Estudar em paralelo
> - Fluxo de dispersão em transformadores: conceito de "leakage flux path"
> - Efeito pele em condutores planos: profundidade de penetração δ = √(ρ/πfμ)
> - Perdas por dispersão na tampa e paredes: método de imagens e FEM

---

## 4. Folha 3 — Perdas e Impedância de Curto-Circuito

### 4.1 Decomposição das perdas em curto-circuito

Para tap 9 (nominal), as perdas totais calculadas são 196.857 W (garantidas 240.000 W). A decomposição revela:

```
BT1:  Ôhmica 67.737 W + Axial 1.316 W + Radial 430 W + Dispersão 8.096 W
AT1:  Ôhmica 85.637 W + Axial 3.061 W + Radial 703 W
AT2:  Ôhmica 0 W (short-circuited no tap 9) + Axial 37 W + Radial 12 W
```

**Perdas ôhmicas** = $I^2 \cdot R$ nas resistências dos condutores a 75°C.

**Perdas parasitas axiais** surgem do campo magnético radial na região das extremidades dos enrolamentos. O campo radial (que não é puramente axial como no centro) induz correntes nos condutores numa direção que gera aquecimento extra. Para enrolamentos de disco, estas perdas são maiores nos discos das extremidades — por isso o fator K (K=2 para tap 9, K=4 considerado na nota da planilha) é aplicado para amplificar as perdas nas extremidades ao verificar o hot-spot.

**Perdas parasitas radiais** surgem do campo axial que penetra pelos condutores na direção radial. Essencialmente $P_{rad} \propto (t_{radial})^2 \cdot B_{ax}^2$, onde $t_{radial}$ é a espessura radial do condutor. Por isso o CTC (fios finos) tem perdas radiais muito menores que um condutor retangular maciço de mesma seção.

**Perdas por dispersão** = perdas nas paredes do tanque, tampas, suportes metálicos e estruturas condutoras dentro e ao redor do campo de dispersão. O fator $k$ (entre 1,9 e 2,1 dependendo do tap) é um coeficiente empírico que multiplica a perda de dispersão calculada para abranger geometrias reais.

> [!important] Por que a impedância varia com o tap
> Tap 1: Z = 10,52% — mais espiras no RAT → distância AT-BT maior (mais espiras na janela) → menor acoplamento → maior reatância de dispersão
> Tap 17: Z = 9,92% — menos espiras → menor distância efetiva → maior acoplamento → menor reatância
>
> Essa variação importa para o sistema elétrico: em tap 17 a corrente de curto-circuito pode ser ~6% maior do que em tap 9. A Folha 3 calcula a impedância nos três taps extremos exatamente para garantir que o transformador cumpre o valor garantido (Z = 10%) no tap nominal.

> [!tip] Estudar em paralelo
> - Perdas em correntes parasitas em condutores retangulares: fórmulas de Rogowski e Dowell
> - Fator de hot-spot: relação entre gradiente de temperatura e perdas parasitas locais
> - Reatância de dispersão: modelo de transformador ideal + reatância série — cálculo por energia armazenada no campo de dispersão

---

## 5. Folha 4 (DDI) — Matriz de Tensões Internas Máximas

### 5.1 O que é o DDI e por que é o coração do EPA

**DDI = Distância Dielétrica Interna** (também referido como tensão dielétrica máxima entre nós).

A ideia fundamental: cada ponto no interior do transformador que está conectado eletricamente a algum componente tem um **potencial elétrico** durante cada condição de ensaio. A distância física entre dois pontos precisa ser suficiente para suportar a **diferença de potencial** entre eles — não o potencial absoluto de cada um.

A Folha 4 constrói uma **matriz quadrada** onde cada elemento (i,j) é a máxima diferença de potencial entre o nó i e o nó j, considerando **todos os taps e todas as condições de ensaio**.

### 5.2 Os nós do transformador 19163865

```
Nó 88 = H1    — terminal AT fase 1 (ponto de entrada do impulso)
Nó 41 = H3    — terminal AT fase 3
Nó 65 = CDC-12 — contato do comutador, posição 12
Nó 64 = CDC-15 — contato do comutador, posição 15
Nó 90 = RAT+   — terminal positivo do enrolamento de regulação
Nó 97 = RAT-   — terminal negativo do enrolamento de regulação
Nó 40 = X1    — terminal BT fase 1
Nó 1  = X0    — terminal BT neutro (NBT)
Terra  = 0    — tanque, núcleo, blindagem
```

### 5.3 Leitura da matriz DDI

```
       Terra   H1       H3      CDC-12  CDC-15  RAT+    RAT-    X1
H1     650[275]  —
H3     650[275] 650[275]  —
CDC-12 442[275] 575[217] 580[219]  —
CDC-15 442[275] 580[219] 575[217] 131[49]  —
RAT+   457[275] 555[210] 580[219] 133[50] 133[50]  —
RAT-   457[275] 580[219] 556[210] 133[50] 133[50] 133[50]  —
X1     200[75]  650[275] 650[275] 442[275] 442[275] 457[275] 457[275]  —
X0/NBT 200[75]  650[275] 650[275] 442[275] 442[275] 457[275] 457[275] 200[75]
```

Notação: `impulso kVp [freq. industrial kV ef]`

**Interpretação linha por linha:**

**H1 para terra: 650 [275]** — o terminal AT fase 1 é ensaiado com 650 kVp de impulso em relação ao tanque (aterrado). Isso é o NBI do AT. Define a distância mínima de H1 (e de todo o enrolamento AT1) ao tanque.

**CDC-12 para terra: 442 [275]** — O contato 12 do comutador está a 442 kVp do terra em algum tap. Como o comutador tem 17 posições entre 124,2 kV e 151,8 kV, nos taps extremos parte do RAT está em circuito e parte está flutuando — o nó CDC-12 assume uma tensão intermediária calculada pela EMTP.

**CDC-12 para H1: 575 [217]** — A diferença entre o nó CDC-12 e o terminal AT H1 é de 575 kVp. Isso significa que entre o contato do comutador e o terminal AT principal existe uma diferença de potencial de 575 kVp durante o ensaio de impulso. **Essa distância governa o espaçamento interno do comutador ao enrolamento AT.**

**RAT+ para terra: 457 [275]** — O enrolamento de regulação, no extremo "mais" do degrau atual, fica a 457 kVp da terra. Note que 457 > 200 (BT) mas < 650 (AT) — o RAT está elétrica e fisicamente entre BT e AT, sendo parte do enrolamento AT.

**X1 para H1: 650 [275]** — O terminal BT (X1) em relação ao terminal AT (H1) tem diferença de 650 kVp. Isso define a isolação entre AT e BT — o canal principal de 43 mm com as barreiras de pressboard precisa suportar esse valor.

**X0 para H1: 650 [275]** — O NBT também precisa suportar 650 kVp em relação ao AT. Mesmo sendo neutro, durante o ensaio de impulso aplicado na bucha AT, a tensão no neutro pode atingir valores próximos ao nível AT (dependendo da distribuição capacitiva AT→BT→X0). Isso é contraintuitivo e é o motivo pelo qual o isolamento do NBT não pode ser simplesmente zero.

> [!important] Por que a EMTP é necessária para calcular os nós CDC e RAT
> Os nós do comutador (CDC-12, CDC-15) e do RAT não têm um potencial definido diretamente pela tensão nominal. Eles dependem de:
> 1. Qual tap está selecionado (de 1 a 17)
> 2. A topologia do circuito do comutador naquele tap (quais contatos estão fechados)
> 3. A distribuição capacitiva dentro do enrolamento durante a frente de impulso (transitório)
>
> Calcular isso analiticamente é impraticável para 17 taps × múltiplas condições de ensaio × múltiplos nós. A solução é modelar o transformador no EMTP (Electromagnetic Transients Program) e simular cada condição. A aba **DDI Máx** contém exatamente os scripts de entrada do EMTP para cada caso, e a Folha 4 consolida os máximos encontrados.

> [!tip] Estudar em paralelo
> - Modelagem de transformadores no EMTP: modelo de Bergeron, modelo detalhado com capacitâncias
> - Distribuição de tensão em transitórios: frente de onda vs. regime distribuído
> - Comutadores OLTC: princípio de operação do ABB UZFRT, circuito de transição com resistências

---

## 6. Aba Campo — Distribuição Capacitiva de Campo Elétrico

### 6.1 O problema físico resolvido

Dois cilindros coaxiais (enrolamentos) com diferentes permissividades no espaço entre eles (camadas de óleo, papel kraft, pressboard/TIV). A tensão aplicada entre eles distribui-se proporcionalmente às **impedâncias capacitivas** de cada camada:

$$U_i = U_{total} \cdot \frac{C_{equiv}}{C_i}$$

Onde $C_i$ é a capacitância da camada $i$ e $C_{equiv}$ é a capacitância total em série.

Para um cilindro de diâmetro interno $d_1$ e externo $d_2$ com permissividade $\varepsilon$:

$$C = \frac{2\pi\varepsilon L}{\ln(d_2/d_1)}$$

O campo elétrico médio em cada camada é:

$$E_i = \frac{U_i}{(d_{2,i} - d_{1,i})/2}$$

A planilha usa $\varepsilon_{óleo} = 2{,}2$, $\varepsilon_{kraft} = 3{,}2$, $\varepsilon_{pressboard/TIV} = 4{,}4$.

### 6.2 Seção 1: Canal entre núcleo (blindagem) e BT1

```
Tensão aplicada:     70 kV (TP do BT)
Composição do canal:
  Núcleo (terra) → 2 mm kraft → 22 mm óleo → 3 mm TIV → BT1
Diâmetros: 582 → 592 → 608 → 626 → 626 mm
```

Resultado: margem de segurança **109%** (mínima desejada 60%). Canal seguro com bastante folga para a tensão aplicada de BT.

O campo médio de 3,18 kV/mm no canal de óleo está bem abaixo do campo de ruptura do óleo limpo (tipicamente >15 kV/mm para campos uniformes, mas considerando a geometria cilíndrica e o tamanho do gap, o critério de projeto é bem mais conservador — ~5–8 kV/mm para óleo em serviço com longos gaps).

### 6.3 Seção 2: Canal entre BT1 e AT1 — o canal crítico

```
Tensão aplicada:     275 kV (TP do AT)
Composição do canal:
  BT1 → [barreiras e canais de óleo] → AT1
Margem mínima encontrada: 24% (mínima desejada 20%)
```

Esta margem de apenas **24%** (desejada 20%, portanto passa — mas por pouco) é o ponto mais crítico eletricamente do projeto. Se a tensão de ensaio fosse 1,25× maior, o canal falharia.

A margem é calculada como:

$$\text{Margem} = \frac{E_{admissível} - E_{calculado}}{E_{calculado}} \times 100\%$$

O campo admissível é determinado a partir de curvas experimentais (Krämer curves) que relacionam a tensão de ruptura com a geometria e as condições do óleo (temperatura, umidade, gases dissolvidos).

> [!important] Campo efetivo vs. campo médio
> A planilha reporta dois campos: **Campo médio** (3,18 kV/mm) e **Campo efetivo** (3,62 kV/mm) para o canal BT-núcleo. A diferença (fator ~1,14) é o **fator de não-uniformidade** do campo elétrico nessa geometria cilíndrica. Para a verificação de ruptura, usa-se o **campo máximo** — que ocorre na superfície do cilindro de menor raio (BT1 interno, raio 313 mm).
>
> Para geometria cilíndrica: $E_{max}/E_{med} = \ln(r_2/r_1) / (1 - r_1/r_2)$

> [!tip] Estudar em paralelo
> - Curvas de Krämer (Krämer curves): tensão de ruptura do óleo em função da distância e da uniformidade do campo
> - Fator de não-uniformidade η = E_max / E_med e sua influência no dimensionamento
> - Efeito da temperatura e da umidade na rigidez dielétrica do óleo: IEC 60156
> - Descargas parciais em canais de óleo: limiar de inception e propagação para ruptura

---

## 7. TRANEM-BT e TRANEM-AT — Verificação de Impulso Disco a Disco

### 7.1 O que o TRANEM calcula

Para cada disco (ou par de discos) do enrolamento, calcula a tensão que aparece:
- **Entre espiras** do mesmo disco
- **No espaçador** (entre discos consecutivos)
- **No corner do espaçador** (concentração de campo na aresta)

### 7.2 Resultados para BT1

```
NBI aplicado:        200 kVp
Tensão entre espiras: 13 kV → margem 5,51×
Tensão no espaçador:  32 kV → margem 4,95×
Corner do espaçador:  — → margem 4,77×
```

Margens confortáveis. O BT opera com corrente alta (669 A) mas tensão modesta (36,2 kV classe) — os condutores são grandes, a isolação é relativamente pouco exigida eletricamente.

### 7.3 Resultados para AT1

```
NBI aplicado:        650 kVp
Tensão entre espiras: 4 kV → margem 16,56×  (muita folga)
Tensão no espaçador:  60 kV → margem 2,65×
Corner do espaçador:  — → margem 2,07×
```

O corner com 2,07× é o ponto mais crítico. A tensão no espaçador de 60 kV não é a tensão total entre os dois discos — é a tensão axial que aparece localmente entre duas espiras de discos adjacentes durante a frente de onda de impulso.

### 7.4 Por que a distribuição de tensão ao longo do AT1 não é uniforme

A tabela de nós do TRANEM-AT mostra, coluna 3 (tensão radial kV em cada nó):

```
Nó 1  (disco 92, topo):   650 kVp
Nó 5  (disco 90):          616 kVp  (cai apenas 34 kV em 4 discos = 8,5 kV/disco)
Nó 47 (disco 69):          650 kVp  (volta a subir — efeito da reflexão)
Nó 33 (meio do enrolamento): ~461 kVp (tensão mais baixa)
```

Essa distribuição não é linear porque a impedância do enrolamento para a frente de onda de impulso é **capacitiva, não indutiva**. A frente de onda "vê" uma rede de capacitores: capacitâncias série entre espiras e capacitâncias shunt para terra. A tensão oscila ao longo do comprimento — é literalmente uma onda estacionária numa linha de transmissão de parâmetros distribuídos.

A estrutura 16DE (interleaved) nos primeiros e últimos 16 discos serve exatamente para achatar a curva nessas regiões onde a tensão seria mais alta num DC convencional.

> [!important] Tensão entre espiras vs. tensão entre discos
> - **Entre espiras** (coluna 14, "kV/espira"): no AT1, máx 25 kV entre espiras consecutivas nos discos interleaved da extremidade. Com papel HD TU de 0,84 mm bi-espessura (Is = 1,37 mm), a rigidez é ~250–300 kV/mm × 1,37 mm ≈ 340 kV → margem confortável de 340/25 ≈ 13×.
> - **Entre discos** (coluna 13, "kV entre discos"): máx 72 kV entre discos adjacentes no AT1. O espaçador de 4–6 mm precisa suportar essa tensão. Para 6 mm e 72 kV: campo = 12 kV/mm no espaçador, que é pressboard — margem OK mas não excessiva.

> [!tip] Estudar em paralelo
> - Modelo de linha de transmissão para enrolamentos de transformador: Rudenberg, de Leon
> - Distribuição de tensão em enrolamentos de disco: coeficiente de redistribuição γ
> - Papel Kraft TU (Thermally Upgraded): diferença do Kraft convencional — resistência ao envelhecimento térmico, menor redução de DP sob temperatura

---

## 8. FCC — Esforços de Curto-Circuito (Método de Rabins)

### 8.1 O que é o método de Rabins

O método analítico de Rabins resolve as equações de campo magnético num transformador de núcleo toroidal de revolução (cilíndrico), obtendo a distribuição completa do fluxo de dispersão e calculando as forças sobre cada elemento de condutor.

É mais preciso que o método simples (força axial = BxI na extremidade, força radial = LxBxI no centro) porque considera:
1. A variação axial do campo magnético
2. O desequilíbrio de ampere-voltas entre posições axiais (que gera forças axiais internas)
3. A contribuição de múltiplos enrolamentos

A norma usada: **NBR 5356-5:2007** — ensaios de suportabilidade a curto-circuito.

### 8.2 Resultados e seu significado

```
Corrente de curto-circuito (fator complexivo 658,49 A pico)
Potência base: 40.000 kVA, tap 17 (pior caso — maior corrente de CC)
Impedância: 9,92%
```

**Forças radiais:**

| Região | Tração de expansão | Flambagem dinâmica |
|--------|-------------------|-------------------|
| BT1 | — / — (compressão) | 56,7/63,8 N/mm² |
| AT1 | **78,9/108,0** N/mm² | — |
| AT2 | 15,0/81,0 N/mm² | — |

O AT1 está sob **tração de expansão** de 78,9 N/mm² (limite 108 N/mm²) — o curto-circuito tende a expandir o enrolamento AT para fora. Com resistência de 0,2% de deformação (Rp0,2) do cobre = 120 N/mm², a margem é 108/78,9 ≈ 1,37× — adequada mas não excessiva.

O BT1 está sob **compressão** (o curto-circuito tende a colapsar o enrolamento BT para dentro, pois os campos magnéticos do AT e BT são opostos). O critério é flambagem dinâmica: 56,7/63,8 N/mm² — margem mais apertada (1,12×).

**Forças axiais:**

| Região | Compressão anéis | Compressão espaçadores | Flexão entre espaçadores |
|--------|-----------------|----------------------|--------------------------|
| BT1 | 10,3/80,0 | 22,4/80,0 | 26,9/108,0 |
| AT1 | 9,9/80,0 | 26,5/80,0 | **63,8/108,0** |
| AT2 | 4,3/80,0 | 4,3/35,0 | — |

A flexão entre espaçadores do AT1 (63,8/108,0 N/mm²) é o critério mais exigido axialmente — o condutor do disco se curva como uma viga apoiada nos espaçadores sob a força axial de curto-circuito. Margem: 1,69×.

**Força axial total para a armadura (iógo):** 34,9 toneladas. Esta força comprime o conjunto núcleo+enrolamentos na direção vertical — as armaduras (clamps) e o sistema de prensagem devem suportar essa carga sem deformar, o que definiria dano permanente ao transformador após um curto-circuito.

> [!important] Por que o tap 17 é o pior para curto-circuito
> No tap 17 (mínima tensão = 124,2 kV), a impedância é 9,92% — a menor dentre os taps. A corrente de curto-circuito é inversamente proporcional à impedância: $I_{cc} \propto 1/Z\%$. Comparando: no tap 1 Z=10,52% → Icc menor; no tap 17 Z=9,92% → Icc **6% maior** que no nominal. Por isso o FCC usa o tap 17 como caso mais crítico.

> [!tip] Estudar em paralelo
> - Método de Rabins: paper original (Rabins, 1956, AIEE Transactions)
> - Critérios de resistência de condutores de transformador sob CC: IEC 60076-5
> - Flambagem de cilindros de cobre: teoria de Euler para cascas cilíndricas
> - Fator de assimetria em curtos-circuitos: por que Ip = √2 × Irms × kfator

---

## 9. DDI Máx — Interface EMTP para Varredura de Todos os Casos

### 9.1 O que essa aba faz

Contém os scripts de entrada do EMTP para cada combinação de tap × condição de ensaio. Cada caso define:

```
APLICA:  qual nó recebe o impulso (88=H1, 41=H3, 40=X1, 1=X0)
LIn:     tensão do impulso (650 kVp para AT, 200 kVp para BT)
ATERRA:  quais nós estão aterrados durante o ensaio
LIGA:    topologia dos contatos do comutador naquele tap
```

A aba mostra 17 taps × 2 terminais de AT (H1, H3) + BT (X1, X0) = 17×4 = 68 cenários de ensaio. Para cada cenário, o EMTP simula a frente de onda e registra a tensão de pico em cada nó.

A aba **Folha 4** consolida o máximo de todos os 68 cenários — essa é a **DDI Máxima**, que determina a distância física mínima entre cada par de pontos dentro do transformador.

### 9.2 Por que o EMTP e não cálculo estático

A distribuição de tensão durante a frente de onda de impulso (1,2 μs de subida) é essencialmente **capacitiva** — as indutâncias dos enrolamentos têm impedância muito alta a essa frequência equivalente (centenas de kHz) e não conduzem corrente apreciável. O transformador nesse instante é uma rede de capacitâncias.

Mas à medida que a onda decai (após os primeiros microssegundos), os enrolamentos entram em ressonância — tensões locais podem superar a tensão aplicada em alguns nós por fenômenos de oscilação. Esses picos internos só aparecem na simulação temporal completa.

> [!important] Tensão interna maior que a aplicada
> Observe que CDC-12 para H3 = 580 kVp, enquanto a tensão aplicada em H1 é 650 kVp e a tensão entre H1 e H3 seria 0 (ambos os terminais AT em operação simultânea). Mas no ensaio, H3 pode estar aterrado enquanto H1 recebe o impulso — e a tensão que aparece no nó CDC-12 é 580 kVp para terra, enquanto H1 tem 650 kVp. A diferença (650 - 580 = 70 kVp) é a tensão admitida entre H1 e CDC-12, o que define o espaço livre entre o terminal AT e o contato do comutador mais próximo.

---

## 10. Vida Útil — Envelhecimento Térmico do Isolamento

### 10.1 A equação de Arrhenius aplicada ao papel isolante

O mecanismo de envelhecimento do papel kraft (celulose) é uma **reação química** — hidrólise ácida e oxidação das cadeias de celulose — cuja velocidade dobra a cada ~6–8°C de aumento de temperatura (Regra de Montsinger / aproximação da equação de Arrhenius).

A equação de envelhecimento relativo (IEC 60076-7:2005):

$$V_{envelhecimento} = e^{\frac{E_A}{k_B}\left(\frac{1}{T_{ref}+273} - \frac{1}{T_{hs}+273}\right)}$$

Onde:
- $T_{ref} = 98°C$ (temperatura de referência para vida nominal de 180.000 horas ≈ 20,5 anos)
- $T_{hs}$ = temperatura do hot-spot em °C
- $E_A/k_B \approx 15.000 K$ para papel convencional (13.000–17.000 para papel TU)

Para este transformador (papel **termoestabilizado/TU**), a temperatura de referência é **110°C** com vida nominal de 200.000 horas (~22,8 anos), resultando na vida esperada de **40,12 anos** calculada.

### 10.2 Perfil de carga e consumo de vida

O perfil de carga simulado:
```
720 min a 1,0 pu  (12h em carga nominal)
240 min a 1,2 pu  (4h em sobrecarga 20%)
30  min a 1,4 pu  (0,5h em sobrecarga 40%)
450 min a 1,0 pu  (7,5h retorno à nominal)
```

Hot-spot do BT: **126,91°C** a 990 min de simulação.

Vida consumida neste ciclo de 24h: **0,43 dias** equivalentes de envelhecimento à temperatura de referência. Taxa de envelhecimento: **0,427** — ou seja, o transformador neste perfil envelhece 0,427 vezes mais rápido do que a taxa nominal, resultando em vida esperada de ~40 anos.

> [!important] Hot-spot no BT, não no AT
> Apesar do AT ter NBI maior e tensão maior, o hot-spot máximo está no BT (126,91°C vs. 125,32°C AT). Isso ocorre porque o BT tem **corrente muito maior** (669,4 A vs. 107,4 A por fase no AT), e as perdas ôhmicas ($I^2R$) geram mais calor no BT. Além disso, o BT é o enrolamento **mais interno** (mais próximo do núcleo), com pior acesso ao óleo de resfriamento.

> [!important] Papel TU vs. papel convencional
> O papel termoestabilizado (TU — Thermally Upgraded) tem energia de ativação maior e vida mais longa à mesma temperatura. A temperatura de envelhecimento de referência sobe de 98°C para 110°C. Isso permite projeto com hot-spot mais alto ou vida útil mais longa com o mesmo perfil. A planilha usa "Papel termoestabilizado" explicitamente na aba Vida Útil — confirma que é papel TU.

> [!tip] Estudar em paralelo
> - IEC 60076-7: Guia de carregamento de transformadores de potência
> - Modelo térmico do transformador: constante de tempo térmica (112,5 min neste caso), equações exponenciais vs. equações com calor específico
> - Degradação do grau de polimerização (DP) do papel: relação DP × resistência mecânica × vida útil
> - Gás CO e CO₂ como indicadores de degradação do papel — cromatografia (DGA)

---

## 11. Síntese — Como tudo se conecta nas dimensões do tanque

### 11.1 Cadeia de causalidade completa

```
Potência + Tensões + Norma
        ↓
   NBI e TP  (Dados_DTDS)
        ↓
DDI máxima entre cada par de nós  (Folha 4 + DDI Máx via EMTP)
        ↓
Distâncias mínimas em óleo por par de componentes  (Campo)
        ↓
Núcleo (diâm, passo, janela) + Enrolamentos (Φ, altura)  (Folha 1, Folha 2)
        ↓
Verifica impulso disco a disco  (TRANEM)
Verifica campo nos canais  (Campo)
Verifica esforços de CC  (FCC)
        ↓
Vista Superior → comprimento e largura do tanque
Vista Lateral → altura do tanque  (+TCs, +OLTC)
        ↓
Dimensões limite: L=2820mm × H=2470mm  (Folha 2, canto direito)
```

### 11.2 As dimensões finais deste transformador

Da Folha 2:
```
L  = 2.820 mm  (comprimento interno do tanque)
H  = 2.470 mm  (altura interna)
EE = 1.130 mm  (entre eixos = passo entre colunas)
HJ = 1.350 mm  (altura da janela do núcleo)
E1 = 560 mm    (largura da chapa do 1º degrau do núcleo)
L1 = 570 mm    (largura interna transversal — lado S2/S3)
```

A largura L1=570 mm é o valor que define o lado curto do tanque oblongo. Com Φ_ext_AT = 992 mm (raio 496 mm), a distância do enrolamento AT à parede seria:

$$d_{AT\_parede} = \frac{570}{2} - 496 = 285 - 496 = -211\ \text{mm ???}$$

Isso seria negativo — impossível. Isso indica que **L1 não é a largura transversal do tanque no sentido de S2-S3**, mas possivelmente outra medida (talvez a largura de um componente ou a folga lateral do núcleo). A largura do tanque no eixo S2-S3 deve ser ao menos 992 mm (diâmetro externo AT) + 2 × distância AT-parede. Para NBI 650 kVp, a distância AT-parede em óleo é tipicamente ~140–160 mm, portanto a largura mínima seria ~992 + 280 = 1.272 mm.

> [!important] Conferir as definições de L, H, L1 na aba Folha 2
> Os valores L=2820 mm, H=2470 mm, L1=570 mm precisam ser conferidos na planilha com suas definições exatas. L1=570 mm pode ser o **afastamento entre o enrolamento BT e a parede** em algum sentido específico, não a largura total.

---

## 12. TCs — Transformadores de Corrente Internos *(ausentes da planilha — análise complementar)*

### 12.1 Por que os TCs impactam o EPA

Os TCs de bucha são instalados dentro do tanque, ensartados nas passagens das buchas (terminais AT e BT). Cada TC tem:
- **Diâmetro interno** que deve ser ≥ diâmetro do terminal passante da bucha
- **Diâmetro externo** que determina o espaço livre necessário
- **Altura** que se acumula com os outros TCs na mesma fase

A altura total dos TCs na fase AT define a **folga superior mínima** — a distância entre o topo do enrolamento e o tampo do tanque.

### 12.2 Distâncias elétricas dos TCs

O núcleo do TC está aterrado (núcleo toroidal metálico). Portanto:
- **TC ao terminal AT:** distância ≥ d_FT_AT (para NBI 650 kVp, tipicamente ~140 mm)
- **TC ao tampo (aterrado):** distância ≥ dependente do NBI do terminal sobre o qual está instalado
- **TC de fase diferente:** distância ≥ d_FF

Para este transformador (AT = 650 kVp), os TCs de AT são os mais críticos dimensionalmente. Um TC típico para 138 kV / 185 A pode ter diâmetro externo de 400–500 mm e altura de núcleo de 100–180 mm por núcleo.

### 12.3 O que deveria existir na planilha

Uma aba de TCs deveria calcular:

| Parâmetro | Símbolo | Impacto |
|-----------|---------|---------|
| Número de núcleos por fase AT | $n_{TC,AT}$ | Altura empilhada |
| Número de núcleos por fase BT | $n_{TC,BT}$ | Pode governa folga superior |
| Altura de um núcleo | $h_{TC}$ | Entra direto na folga superior |
| Distância TC ao tampo | $d_{TC,tampo}$ | Distância elétrica |
| Distância TC ao terminal AT | $d_{TC,H}$ | Distância elétrica |
| Altura total empilhada | $H_{TC} = n \cdot h_{TC}$ | **Determina mínimo de H_tanque** |

---

## 13. Check List — As verificações finais

A aba Check List consolida todos os critérios de aprovação/reprovação. Tipicamente verifica:

- [ ] NBI e TP corretos para a classe de tensão (NBR 5356-3)
- [ ] Canal BT-AT com margem ≥ mínima (aba Campo)
- [ ] Todas as tensões DDI dentro dos limites de cada nó (Folha 4)
- [ ] Margens de impulso disco a disco ≥ 1,3× em todos os nós (TRANEM)
- [ ] Esforços de CC dentro dos limites de resistência mecânica (FCC)
- [ ] Hot-spot ≤ 140°C (papel TU), vida útil calculada ≥ vida contratada (Vida Útil)
- [ ] Perdas e impedância dentro das garantias contratuais (Folha 3)
- [ ] Blindagem magnética dimensionada para as paredes com maior fluxo de dispersão (Blindagem)

---

## Referências

- ABNT NBR 5356-1:2007 — Transformadores de potência: Generalidades
- ABNT NBR 5356-3:2007 — Níveis de isolamento e ensaios dielétricos
- ABNT NBR 5356-5:2007 — Suportabilidade a curto-circuito
- IEC 60076-7:2005 — Guia de carregamento de transformadores imersos em óleo
- WPR-7583 PT.3 — Procedimento interno WEG: distâncias elétricas em parte ativa
- Rabins, L. (1956). "A new method for calculating magnetic field distribution in transformers." AIEE Transactions.
- [[Estudo de Parte Ativa — Distâncias Elétricas]] — Nota de referência rápida e tabelas
