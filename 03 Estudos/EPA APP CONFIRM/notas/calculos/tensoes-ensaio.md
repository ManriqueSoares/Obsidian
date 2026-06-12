---
tags: [calculos, ensaios, BIL, SIL, AC, impulso]
---

# Tensões de Ensaio

Relacionado: [[../dominio/niveis-isolamento]] | [[metodologia-distancias]]

---

## Tipos de Ensaio Dielétrico

### 1. Tensão Suportável a Frequência Industrial — Curta Duração (ACSD)
- **Forma de onda**: senoidal, 50 ou 60 Hz
- **Duração**: 60 s (curta duração)
- **Aplicação**: ensaio aplicado (terminais → terra) e ensaio induzido
- **Tensão de referência**: `Uac` da tabela IEC 60076-3

### 2. Ensaio de Tensão Induzida (ACID / IVPD)
- **Forma de onda**: senoidal, frequência aumentada (100–200 Hz) para evitar saturação do núcleo
- **Tensão**: ~2 × Un (ensaio de tensão induzida longa duração: PD test a 1,5 × Un)
- **Propósito**: testar a isolação entre espiras, entre canecos, e AT-BT sob tensão contínua
- **Medição**: correntes de descarga parcial (Partial Discharge — PD)

### 3. Impulso Atmosférico (LI — Lightning Impulse)
- **Forma de onda**: 1,2/50 µs (tempo de frente 1,2 µs, tempo de meia onda 50 µs)
- **Nível**: BIL (kVp)
- **Polaridade**: positiva e negativa (ambas para transformadores de alta tensão)
- **Número de aplicações**: 15 total (1 reduzida + 2 plenas + 10 plenas = ensaio padrão)

### 4. Impulso de Manobra (SI — Switching Impulse)
- **Forma de onda**: 250/2500 µs
- **Nível**: SIL (kVp)
- **Aplicação**: somente para Um ≥ 300 kV
- **Determinante para**: distâncias longas (campo quase uniforme)

### 5. Impulso Cortado (Chopped Wave)
- **Forma de onda**: 1,2/µs, interrompido (cortado) por centelhador a ±2–6 µs
- **Nível**: 1,1–1,15 × BIL
- **Propósito**: simular sobretensão com corte por para-raios
- **Severo para**: isolamento entre espiras (dU/dt elevado)

---

## Sequência de Ensaios (IEC 60076-3)

### Ensaios de Rotina
1. Medição de resistência dos enrolamentos
2. Relação de transformação
3. Medição de impedância e perdas em carga
4. Medição de perdas em vazio e corrente de excitação
5. **Ensaio de tensão induzida (ACSD ou ACID+PD)**
6. **Ensaio de tensão aplicada (ACSD)**

### Ensaios de Tipo
- Impulso atmosférico (LI) — obrigatório por norma
- Impulso de manobra (SI) — Um ≥ 300 kV
- Temperatura
- Ruído

### Ensaios Especiais
- Impulso cortado
- Ensaio de tensão induzida longa duração com medição de PD (LIVPD)
- Ensaio de surto em frente íngreme (VSF — Very Steep Front)

---

## Relação Tensão de Ensaio × Tensão de Serviço

| Nível | Relação aproximada |
|---|---|
| BIL | ≈ 3–5 × Um (fase-terra) |
| SIL | ≈ 2–3 × Um |
| Uac | ≈ 1,5–2 × Um |

---

## Tensão por Caneco sob Impulso

A tensão máxima por caneco sob impulso não é simplesmente BIL/n_canecos.

Para enrolamento de disco, a distribuição é determinada pela rede capacitiva:

**Fator de distribuição não uniforme α:**
$$\alpha = h_{enrol} \sqrt{\frac{C_s'}{C_g'}}$$

- `C_s'` = capacitância série por unidade de comprimento (F/m)
- `C_g'` = capacitância shunt por unidade de comprimento (F/m)
- `h_enrol` = altura do enrolamento (m)

**Tensão no topo do enrolamento** (pior caso, n° de caneco → topo):
$$\Delta U_{1,2} \approx \frac{\alpha}{n_c} \cdot \cosh(\alpha) / \sinh(\alpha) \cdot U_{BIL}$$

Para α ≫ 1 (típico): tensão nos primeiros canecos ≫ BIL/n_canecos

**Objetivo do interleaving**: aumentar `C_s'` → reduzir α → distribuição mais uniforme.

---

## Ensaio de Impulso em Comutadores (IEC 60214)

- O OLTC deve suportar o BIL correspondente à Um do enrolamento ao qual está conectado
- Ensaios realizados com o comutador em posição de extremo (tensão máxima nos terminais)
- Fabricante especifica a suportabilidade: projetista deve garantir as distâncias externas

---

## Notas do usuário

> _Inserir protocolos de ensaio internos, sequências adotadas, equipamentos de laboratório disponíveis_
