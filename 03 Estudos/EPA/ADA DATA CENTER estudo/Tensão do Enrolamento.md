
## Tensão do Enrolamento

> **Fonte:** `Folha 1`, linha 15 (L15) — colunas D, G e J

| Enrolamento | Tensão do Enrolamento (V) | Tipo de Ligação | Fonte |
|---|---|---|---|
| BT1 | **19.918,58** | Estrela (YN) | Folha 1, L15 col D |
| AT1 | **138.000** | Delta | Folha 1, L15 col G |
| AT2 *(regulação)* | **13.800** | Delta | Folha 1, L15 col J |

### O que é a tensão do enrolamento?

A **tensão do enrolamento** é a tensão elétrica que cada bobina individualmente precisa suportar entre seus terminais — é a tensão de **fase**, não necessariamente a tensão de **linha** que aparece nas especificações de placa.

A diferença entre tensão de linha e tensão de fase depende diretamente do tipo de ligação:

```
Ligação DELTA (AT):  V_enrolamento = V_linha         (a bobina está conectada entre duas linhas)
Ligação ESTRELA (BT): V_enrolamento = V_linha / √3   (a bobina está entre uma linha e o neutro)
```

### É uma estimativa ou um cálculo exato?

**É um cálculo exato**, derivado diretamente da tensão de linha e do tipo de ligação:

```
BT1 (Estrela):  V_enrol = 34.500 / √3 = 34.500 / 1,732050808 = 19.918,58 V  ✓
AT1 (Delta):    V_enrol = 138.000 V  (igual à tensão de linha)              ✓
AT2 (Delta):    V_enrol = 138.000 × 10% = 13.800 V  (faixa total de regulação) ✓
```

O valor de BT1 = **19.918,58 V** usa todos os decimais de √3, por isso difere levemente do arredondamento 34.500 / 1,732 = 19.919 V usado anteriormente.

### Para que serve saber a tensão do enrolamento?

A tensão do enrolamento é o **ponto de partida de todo o projeto elétrico da bobina**. A partir dela derivam-se diretamente:

**1. Número de espiras (confirma o calculado em 4.3):**

```
N = V_enrolamento / (V/espira)

N_BT1 = 19.918,58 / 108,25 = 184,0 esp  ← Folha 1, L23 col D: 184  ✓
N_AT1 = 138.000  / 108,25 = 1.274,9 esp ← Folha 1, L23 col G: 1275  ✓
N_AT2 =  13.800  / 108,25 = 127,5 esp   ← Folha 1, L23 col J:  128  ✓
```

O volt/espira (108,25 V) é o parâmetro de projeto do núcleo; todas as contagens de espiras são consequência direta dele. O número exato de espiras é arredondado para inteiro, e a pequena diferença é absorvida pelo ajuste fino do núcleo.

**2. Dimensionamento da isolação:** a isolação entre espiras, entre camadas e entre a bobina e o núcleo/tanque é projetada para suportar a tensão de fase, não a de linha. Para a BT1, a bobina vê 19.919 V em operação normal — e o ensaio de tensão induzida (69 kV) testa esse isolamento a 3,5× o valor nominal.

**3. Corrente de fase do condutor:** a corrente que passa pelo condutor é a corrente de fase, que também depende da ligação:

```
Ligação ESTRELA (BT1): I_fase = I_linha = 669,4 A     ← Folha 1, L21 col D: 669,4 ✓
Ligação DELTA  (AT1):  I_fase = I_linha / √3 = 185,9 / √3 = 107,4 A ← Folha 1, L21 col G: 107,4 ✓
```

### O que é o enrolamento AT2?

AT2 é o **enrolamento de regulação** (tap winding). Enquanto AT1 é o enrolamento principal com 1.275 espiras e 138 kV, AT2 é um enrolamento separado, menor, de apenas 128 espiras e 13.800 V, dedicado exclusivamente a prover a variação de ±10% da tensão.

```
Faixa total de regulação = 138.000 × 10% = 13.800 V  → tensão máxima do AT2
Cada tap representa: 1,25% × 138.000 = 1.725 V  → 13.800 / 8 taps = 1.725 V/tap
Espiras por tap: 128 / 8 degraus = 16 espiras/degrau  ← Folha 1, L29 col J: 16  ✓
```

O comutador de taps (DETC/OLTC) conecta ou desconecta as espiras do AT2 em série com AT1:

```
Tap 1  (máximo): AT1 + AT2 completo = 138.000 + 13.800 = 151.800 V  ✓
Tap 9  (nominal): AT1 apenas        = 138.000            = 138.000 V  ✓
Tap 17 (mínimo): AT1 − AT2 completo = 138.000 − 13.800  = 124.200 V  ✓
```

O AT2 é do tipo **Hélice Múltipla tipo "C"** (Folha 1, L17 col J) — uma construção em que o condutor percorre o enrolamento em múltiplos degraus helicoidais, facilitando a derivação de taps em posições intermediárias sem comprometer o balanceamento do campo magnético.