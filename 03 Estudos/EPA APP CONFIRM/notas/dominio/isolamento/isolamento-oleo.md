---
tags: [dominio, isolamento, oleo, dieletrico]
---

# Isolamento em Óleo Mineral

Relacionado: [[distancias-eletricas]] | [[calculos/metodologia-distancias]] | [[isolamento/pressboard]]

---

## Por que óleo?

- Alta rigidez dielétrica: ~10–15 kV/mm (campo uniforme, limpo)
- Auto-regenerante: arcos se extinguem e o óleo se "cura"
- Resfriamento eficiente: viscosidade baixa, boa condutividade térmica
- Impregnação do papel isolante: eleva a rigidez dielétrica do conjunto

---

## Rigidez Dielétrica do Óleo

| Condição | Rigidez (kV/mm) |
|---|---|
| Campo uniforme, óleo novo degasificado | 40–60 kV/mm |
| Campo uniforme, óleo em serviço | 15–30 kV/mm |
| Campo não uniforme (condutor fino no óleo) | 5–12 kV/mm |
| Valor usado em projeto (conservador) | ~10 kV/mm |

> Em prática, as distâncias em óleo são ditadas por **critérios normativos** (baseados em ensaios estatísticos), não por rigidez elétrica pura.

---

## Sistemas de Isolamento em Óleo

### 1. Óleo puro (oil gap)
- Usado para distâncias curtas entre eletrodos arredondados
- Mais eficiente por mm quando bem dimensionado

### 2. Óleo + pressboard (barreiras)
- Barreiras de pressboard perpendiculares ao campo elétrico
- Interrompem caminhos de descarga em trajetórias longas
- Aumentam significativamente a suportabilidade com pouco material

### 3. Papel impregnado (OIP — Oil Impregnated Paper)
- Condutor isolado com papel Kraft impregnado em óleo
- Base da isolação sólida dos enrolamentos
- Rigidez: ~50 kV/mm (radial ao papel)

---

## Distâncias em Óleo × Tensão de Ensaio

Curvas empíricas para óleo mineral (campo aproximadamente uniforme, eletrodos arredondados):

| BIL (kVp) | d_min em óleo puro (mm) aprox. |
|---|---|
| 95 | 8–12 |
| 170 | 12–18 |
| 325 | 22–30 |
| 550 | 38–50 |
| 750 | 55–70 |
| 950 | 70–90 |
| 1050 | 80–100 |
| 1300 | 100–130 |

> Estes valores são orientativos. O projeto real usa folhas de pressboard e a metodologia de Moser/Küchler para distâncias compostas (óleo + pressboard).

---

## Efeito das Barreiras de Pressboard

Uma barreira de pressboard colocada perpendicularmente ao campo elétrico no meio de um gap de óleo pode aumentar a suportabilidade em ~30–50%.

Arranjo típico: óleo | pressboard | óleo | pressboard | óleo (múltiplas barreiras)

$$U_{withstand,\;total} = \sum_i E_{i,\;max} \cdot d_i$$

Onde `E_i,max` é a rigidez do meio `i` e `d_i` é a espessura desse meio.

---

## Fator de Campo (Field Enhancement Factor)

Geometrias reais têm campo não uniforme. O fator `η`:

$$\eta = \frac{E_{max}}{E_{medio}} = \frac{E_{max}}{U / d}$$

| Geometria | η típico |
|---|---|
| Plano-plano | 1,0 |
| Cilindro-plano (r >> d) | ~1,1–1,3 |
| Condutor fino no óleo (lead) | 2–5+ |
| Ponta afiada | >> 5 |

Para leads de ligação (fios saindo dos enrolamentos), o campo é muito não uniforme → requer distâncias maiores.

---

## Qualidade do Óleo

A qualidade do óleo afeta as distâncias:
- **Umidade** (ppm de água): mais água → menor rigidez dielétrica
- **Partículas sólidas**: podem criar pontes condutoras
- **Gases dissolvidos**: reduzem a tensão disruptiva (especialmente H2)
- **Acidez (nbm)**: degradação por envelhecimento

**Critérios IEC 60422** para óleo em serviço:
- Umidade ≤ 10 ppm (tensão < 170 kV), ≤ 5 ppm (Alta tensão)
- Rigidez dielétrica ≥ 50 kV (IEC 60156)

---

## Outros Fluidos Isolantes

| Fluido | Rigidez dielétrica | Vantagem | Desvantagem |
|---|---|---|---|
| Óleo mineral naftênico | ~10–15 kV/mm (projeto) | Custo baixo, ampla disponibilidade | Inflamável, não biodegradável |
| Óleo mineral parafínico | Similar | Boa estabilidade térmica | Menor capacidade de dissolução de gases |
| Éster natural (Envirotemp FR3) | Similar | Biodegradável, ponto de ignição alto | Custo maior, viscosidade maior |
| Éster sintético | Similar | Estabilidade térmica superior | Custo alto |
| SF6 (trafos secos-pressurizados) | ~50 kV/mm (1 bar) | Alta rigidez | GEE, custo alto |

---

## Notas do usuário

> _Inserir fornecedores de óleo utilizados, tipo de óleo padrão da empresa, critérios internos de aceitação_
