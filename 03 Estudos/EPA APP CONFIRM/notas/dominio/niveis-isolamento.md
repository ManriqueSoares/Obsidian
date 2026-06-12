---
tags: [dominio, isolamento, BIL, SIL, norma, IEC60076-3]
---

# Níveis de Isolamento — IEC 60076-3 / ABNT NBR 5356-3

Relacionado: [[parametros-eletricos]] | [[distancias-eletricas]] | [[isolamento/isolamento-oleo]]

---

## Conceitos

| Símbolo | Nome completo | Descrição |
|---|---|---|
| `Um` | Tensão máxima do equipamento | Tensão fase-fase máxima sustentável em serviço contínuo |
| `BIL` / `Up` | Basic Insulation Level / Tensão suportável a impulso atmosférico | kVp (valor de pico) |
| `SIL` / `Us` | Switching Impulse Level / Tensão suportável a impulso de manobra | kVp — exigido para Um ≥ 300 kV |
| `ACSD` | Tensão suportável a frequência industrial (short-duration) | kVrms |
| `ACID` | Tensão suportável induzida (induced withstand) | kVrms — ensaio de tensão induzida |

---

## Tabela de Níveis de Isolamento — IEC 60076-3 (Tabela 1 e 2)

### Tensões até 170 kV (Um)

| Um (kV) | BIL (kVp) | ACSD (kVrms) |
|---|---|---|
| 3,6 | 20 / **40** | 10 |
| 7,2 | 40 / **60** | 20 |
| 12 | 60 / 75 / **95** | 28 |
| 17,5 | 75 / **95** | 38 |
| 24 | 95 / **125** | 50 |
| 36 | 145 / **170** | 70 |
| 52 | **250** | 95 |
| 72,5 | 325 / **350** | 140 |
| 123 | 450 / **550** | 230 |
| 145 | 550 / **650** | 275 |
| 170 | 650 / **750** | 325 |

> Negrito = valor mais comum em projetos brasileiros.

### Tensões ≥ 245 kV (Um) — requer SIL também

| Um (kV) | BIL (kVp) | SIL (kVp) | ACSD (kVrms) |
|---|---|---|---|
| 245 | 750 / 850 / 950 / **1050** | 650 / **750** / 850 | 395 / **460** |
| 300 | 850 / 950 / **1050** | 750 / **850** | 395 / **460** |
| 362 | 950 / **1050** / 1175 | 850 / **950** | **510** |
| 420 | 1050 / **1175** / 1300 / 1425 | 850 / 950 / **1050** | 570 / **630** |
| 550 | 1175 / 1300 / **1425** / 1550 | 950 / **1050** | **680** |
| 800 | 1425 / 1550 / **1800** / 1950 | 1175 / 1300 / **1425** | **900** |

---

## Critério de seleção do BIL

O BIL é escolhido em função de:
1. Coordenação de isolamento da subestação (IEC 60071-1)
2. Nível de proteção dos para-raios (SPD)
3. Distância elétrica ao ponto de proteção mais próximo
4. Exigência do cliente / norma do concessionário

$$BIL \geq K_{cord} \cdot U_{residual\_pararraio}$$

Onde `K_cord` ≈ 1,15–1,25 (fator de coordenação)

---

## Impacto do BIL nas distâncias elétricas

As distâncias mínimas em óleo mineral são função principalmente do BIL (impulso atmosférico), pois é o ensaio mais severo para distâncias curtas.

Para distâncias longas (campo quase uniforme, Um ≥ 300 kV), o SIL pode ser determinante.

Ver metodologia de cálculo em [[calculos/metodologia-distancias]].

---

## Isolamento do Neutro

Para AT aterrada, o neutro pode ter BIL reduzido:

| Relação BIL_topo / BIL_neutro | Configuração |
|---|---|
| 1,0 | Isolamento uniforme |
| BIL_topo ≫ BIL_neutro | Isolamento graduado |

Exemplo: Um=145 kV, BIL_topo=650 kVp → BIL_neutro = 95 kVp (neutro aterrado)

---

## Notas do usuário

> _Preencher aqui com os níveis utilizados nos projetos típicos da empresa / projetos referência_
