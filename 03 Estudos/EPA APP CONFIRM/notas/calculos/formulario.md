---
tags: [calculos, formulas, equacoes, referencia-rapida]
---

# Formulário — Referência Rápida

Relacionado: [[metodologia-distancias]] | [[tensoes-ensaio]]

---

## Tensões e Correntes

$$I_n = \frac{S_n}{\sqrt{3} \cdot U_n}$$ (trifásico, A, MVA, kV)

$$E = 4{,}44 \cdot f \cdot N \cdot A_{col} \cdot B_{max}$$ (V, Hz, —, m², T)

$$U_{degrau} = \frac{U_{AT,nom} \cdot tap\%}{n_{pos}/2}$$ (kV por degrau)

---

## Geometria do Enrolamento

$$h_{enrol} = n_c \cdot h_c + (n_c - 1) \cdot d_{ec}$$ (altura do enrolamento)

$$b_{enrol} = \frac{D_{ext} - D_{int}}{2}$$ (largura radial)

$$A_{col} = K_f \cdot D_{col}^2 \cdot sf$$ (seção do núcleo)

---

## Dimensões do Tanque

$$L_{tank} = L_{PA} + 2 \cdot d_{AT\_tanque}$$

$$W_{tank} = D_{AT\_ext} + 2 \cdot d_{AT\_tanque}$$

$$H_{tank} = H_{PA} + d_{fundo} + d_{topo}$$ (sem comutador)

$$H_{tank} = H_{PA} + d_{fundo} + d_{comut\_AT} + h_{comut} + d_{comut\_tanque}$$ (com comutador)

---

## Distâncias Elétricas (estimativa de campo uniforme)

$$d_{min} = \frac{U_{ensaio}}{E_{oleo}} \cdot \eta \cdot K_{seg}$$

| Símbolo | Valor típico de projeto |
|---|---|
| `E_oleo` | 10–15 kVp/mm (projeto conservador) |
| `η` (cilindro-plano) | 1,1–1,2 |
| `η` (lead-plano) | 2–4 |
| `K_seg` | 1,1–1,2 |

---

## Distribuição de Tensão sob Impulso (Canecos)

$$\alpha = h_{enrol} \sqrt{\frac{C_s'}{C_g'}}$$

$$u(x) = U_{BIL} \cdot \frac{\sinh(\alpha \cdot x/h)}{\sinh(\alpha)}$$ (distribuição capacitiva inicial)

$$\Delta U_{c,max} \approx \frac{\alpha \cdot U_{BIL}}{n_c \cdot \tanh(\alpha / 2)}$$ (tensão máx entre canecos adjacentes do topo)

---

## Fator de Forma do Núcleo

| n° degraus | Kf (fator de área) |
|---|---|
| 4 | 0,785 |
| 6 | 0,825 |
| 8 | 0,850 |
| 10 | 0,866 |
| 12 | 0,876 |

$$A_{col,real} = K_f \cdot D_{col}^2 \cdot sf$$

---

## Perdas (estimativa)

$$P_0 \approx p_0 \cdot B_{max}^{1,6} \cdot G_{nucleo}$$ (W, W/kg, T, kg)

$$P_k \approx \rho_{Cu} \cdot J^2 \cdot Vol_{Cu} + P_{eddy}$$ (W — perdas ôhmicas + parasitas)

---

## Forças de Curto-Circuito (estimativa radial)

$$F_{rad} = \frac{\mu_0}{2\pi} \cdot \frac{N \cdot I_{cc}^2}{h_{enrol}} \cdot \ln\left(\frac{D_{AT}}{D_{BT}}\right)$$

---

## Volume de Óleo (aproximação)

$$V_{oleo} = V_{tanque,int} - V_{PA} - V_{estrutura}$$

$$V_{PA} \approx \frac{\pi}{4} \cdot D_{AT\_ext}^2 \cdot H_{PA} \cdot n_{fases}$$ (cilindro equivalente)

---

## Conversão de Unidades

| De | Para | Fator |
|---|---|---|
| kV (rms) → kV (pico) | × √2 | |
| kVp → kVrms | / √2 | |
| mm² → m² | × 10⁻⁶ | |
| MVA, kV → kA | Sn / (√3 · Un) | |
