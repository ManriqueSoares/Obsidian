---
tags: [dominio, comutador, tap-changer, OLTC, DETC, regulacao]
---

# Comutadores (Tap Changers)

Relacionado: [[parametros-eletricos]] | [[distancias-eletricas]] | [[parte-ativa]] | [[enrolamentos]]

---

## Função

Permitem ajustar a relação de transformação variando o número de espiras ativas do enrolamento de regulação (geralmente AT), compensando variações de tensão na rede.

---

## Tipos

### DETC — De-Energized Tap Changer
- Operação **somente com o transformador desligado**
- Construção simples, sem câmara de comutação
- Posicionado geralmente dentro do tanque principal, no topo do enrolamento AT
- Faixas típicas: ±2×2,5%, ±2×5%
- Norma: IEC 60214-2

### OLTC — On-Load Tap Changer
- Operação **em carga, sem interrupção do serviço**
- Possui câmara de comutação com arco elétrico → óleo separado ou vácuo
- Pode ser **intank** (dentro do tanque principal) ou **external** (câmara externa)
- Faixas típicas: ±8×1,25%, ±9×1,67%, ±10×1,5%, ±16×0,625%
- Norma: IEC 60214-1
- Principais fabricantes: Reinhausen (MR), ABB (VZTA), Maschinenfabrik

---

## Posicionamento

| Posição | Descrição | Impacto nas distâncias |
|---|---|---|
| **Topo (in-tank)** | Mais comum, sobre o enrolamento AT | Define `d_topo` e `d_comut_AT` |
| **Lateral externo** | OLTC com câmara separada montada na parede do tanque | Define `d_comut_tanque_lateral` |
| **Separado (external)** | Câmara completamente externa, conectada por tubo | Não afeta dimensões internas do tanque |

---

## Parâmetros do Comutador

| Símbolo | Descrição |
|---|---|
| `tipo_comut` | DETC / OLTC-intank / OLTC-externo |
| `n_posicoes` | Número de posições (degraus + posição nominal) |
| `tap_range_pct` | Faixa total em % (ex: 20% = ±10%) |
| `degrau_kV` | Tensão por degrau em kV |
| `I_comut` | Corrente nominal do comutador (A) |
| `Um_comut` | Tensão máxima do comutador (kV) — determina BIL_comut |
| `h_comut` | Altura do conjunto do comutador (mm) |
| `D_comut` | Diâmetro do comutador (mm) |
| `n_comutadores` | Número de comutadores (1 por fase ou 1 para as 3 fases) |

---

## Número de Comutadores

| Configuração | n_comutadores | Descrição |
|---|---|---|
| 1 DETC (3 fases em paralelo) | 1 | Comutador único operando as 3 fases simultaneamente |
| 3 DETC independentes | 3 | Raros, usados quando fases são separadas fisicamente |
| 1 OLTC 3φ | 1 | OLTC único para transformador trifásico |
| 3 OLTC 1φ | 3 | Bancos de monofásicos ou transformadores com OLTCs independentes |

---

## Tensão nos Terminais do Comutador

A tensão máxima nos terminais do comutador define o BIL exigido.

Para **regulação linear**:
$$U_{tap} = U_{AT,max} - U_{AT,min} = U_{AT,nom} \cdot tap\_range\_pct$$

Para **OLTC com posição de avanço (advance)**:
$$U_{tap,max} = U_{AT} \cdot \frac{tap\_range}{2}$$ (tensão máxima entre terminais extremos)

A tensão de um degrau:
$$\Delta U = \frac{U_{tap,max}}{n\_posicoes / 2}$$

O BIL dos terminais do comutador é definido pela Um do enrolamento de regulação.

---

## Distâncias Elétricas do Comutador

### d_comut_AT
Distância entre as partes vivas do comutador e o enrolamento AT.

- Determinada pelo BIL_AT e pela geometria (campo não uniforme nas conexões)
- Deve considerar a tensão nos terminais de tap sob impulso

### d_comut_tanque
Distância entre as partes vivas do comutador e o tanque (aterrado).

- Para OLTC in-tank: distância à tampa do tanque (d_topo_comut)
- Para OLTC externo: distância na câmara externa (especificação do fabricante)

### Leads de regulação (tap leads)
As ligações entre o enrolamento de regulação e o comutador atravessam o óleo — são os elementos mais críticos:
- Estão à tensão AT + variação de tap
- Condutores em campo não uniforme → requerem maior clearance que eletrodo cilíndrico
- Espaçamento entre leads de fases diferentes

---

## Câmara do OLTC (intank)

Para OLTC in-tank, a câmara de comutação é separada do tanque principal por uma barreira de pressboard ou metal, contendo óleo próprio.

- Dimensão da câmara: fornecida pelo fabricante (ex: Reinhausen OILTAP M, VACUTAP)
- A câmara tem suas próprias distâncias dielétricas internas (responsabilidade do fabricante)
- As distâncias externas (câmara → tanque, câmara → AT) são responsabilidade do projetista

---

## Regulação — Tipos de Circuito

| Tipo | Descrição | Impacto |
|---|---|---|
| **Linear** | Adição/remoção de espiras progressiva | Mais simples, campo em toda a faixa |
| **±** (reversível) | Chave de seleção + chave de reversão | Dobra a faixa com mesmo n_posicoes |
| **Coarse/Fine** | Dois enrolamentos: grosso + fino | Mais posições com comutador menor |

---

## Notas do usuário

> _Inserir fabricantes utilizados, modelos preferidos, faixas típicas de regulação nos projetos_
