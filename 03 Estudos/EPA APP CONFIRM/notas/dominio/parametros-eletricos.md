---
tags: [dominio, eletrico, parametros, entrada]
---

# Parâmetros Elétricos do Transformador

Relacionado: [[niveis-isolamento]] | [[distancias-eletricas]] | [[enrolamentos]] | [[comutadores]]

---

## 1. Potência e Tensões Nominais

| Símbolo | Descrição | Unidade |
|---|---|---|
| `Sn` | Potência nominal | MVA |
| `Un_AT` | Tensão nominal AT | kV |
| `Un_BT` | Tensão nominal BT | kV |
| `Un_TV` | Tensão nominal Terciário (se houver) | kV |
| `fn` | Frequência nominal | Hz (50 / 60) |

> **Um** (tensão máxima do equipamento) é o parâmetro normativo que define a classe de isolamento.  
> Derivado de `Un` pelas tabelas IEC 60038 → ver [[niveis-isolamento]].

---

## 2. Correntes Nominais

$$I_n = \frac{S_n}{\sqrt{3} \cdot U_n}$$ (trifásico)

$$I_n = \frac{S_n}{U_n}$$ (monofásico)

| Símbolo | Descrição |
|---|---|
| `In_AT` | Corrente nominal AT (A) |
| `In_BT` | Corrente nominal BT (A) |

---

## 3. Impedâncias e Perdas

| Símbolo | Descrição | Valor típico |
|---|---|---|
| `uk%` | Tensão de curto-circuito (impedância %) | 5–12% (distribuição), 10–18% (transmissão) |
| `P0` | Perdas em vazio (no-load losses) | W |
| `Pk` | Perdas em carga (load losses) | W |
| `I0%` | Corrente de excitação em vazio | % |
| `Bmax` | Indução máxima no núcleo | T (1,5–1,8 T típico) |

---

## 4. Grupo de Ligação (Vector Group)

Exemplos comuns:

| Grupo | Aplicação |
|---|---|
| `YNyn0` | AT/BT ambos aterrados, defasagem 0° |
| `YNd11` | AT aterrado, BT triângulo, 30° |
| `Dyn11` | AT triângulo, BT aterrado, 330° |
| `YNyn0d11` | Três enrolamentos |

O grupo de ligação influencia:
- A distribuição de tensão entre fases para cálculo de `d_entre_fases`
- Os ensaios de tensão induzida
- A necessidade de neutro e isolamento do neutro

---

## 5. Nível de Isolamento — Entradas do App

Ver tabela completa em [[niveis-isolamento]].

| Símbolo | Descrição |
|---|---|
| `Um_AT` | Tensão máxima AT (kV) |
| `BIL_AT` | Nível básico de isolamento AT (kVp) |
| `SIL_AT` | Nível de impulso de manobra AT (kVp) — Um ≥ 300 kV |
| `Uac_AT` | Tensão de ensaio AC AT (kVrms) |
| `Um_BT` | Tensão máxima BT (kV) |
| `BIL_BT` | Nível básico de isolamento BT (kVp) |
| `Uac_BT` | Tensão de ensaio AC BT (kVrms) |
| `Um_TV` | Tensão máxima Terciário (kV) |

---

## 6. Classe de Neutro

O neutro AT pode ter nível reduzido de isolamento (graded insulation):

- **Isolamento uniforme**: toda a bobina ao mesmo nível BIL
- **Isolamento graduado**: topo ao BIL nominal, neutro a nível reduzido

Impacta diretamente a distância `d_fundo` e o isolamento da prensagem inferior.

---

## 7. Tap Range e Regulação

| Símbolo | Descrição |
|---|---|
| `tap_range` | Faixa de regulação (ex: ±10%, ±15%) |
| `n_posicoes` | Número de posições do comutador |
| `degrau` | Tensão por degrau (kV) |
| `tipo_regulacao` | Linear / ±/ reversível |

A tensão máxima nos terminais do comutador é:
$$U_{comut} = U_{AT} \cdot \frac{tap\_range}{n\_posicoes}$$ (aproximado)

Essa tensão define o `BIL_comutador` e consequentemente as distâncias do comutador.
Ver [[comutadores]].

---

## Perguntas em aberto

- [ ] Existe terciário de estabilização?
- [ ] O neutro AT é aterrado direto ou via resistência/reator?
- [ ] Qual o nível de isolamento do neutro (uniforme ou graduado)?
- [ ] Tipo de ensaio dielétrico requerido: rotina / especial / tipo?
