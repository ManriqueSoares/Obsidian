---
tags: [calculos, metodologia, distancias, dieletrico]
---

# Metodologia de Cálculo das Distâncias Elétricas

Relacionado: [[../dominio/distancias-eletricas]] | [[../dominio/niveis-isolamento]] | [[../dominio/isolamento/isolamento-oleo]] | [[tensoes-ensaio]]

---

## Princípio Geral

As distâncias elétricas mínimas são determinadas pela tensão de ensaio mais severa para cada par de eletrodos, levando em conta:

1. **Qual par de eletrodos** (AT→tanque, AT→BT, lead→lead, caneco→prensa...)
2. **Qual tensão** (AC, BIL, SIL — qual é a mais severa?)
3. **Qual meio isolante** (óleo puro, óleo+pressboard, papel impregnado)
4. **Qual geometria do campo** (uniforme, cilíndrico, pontual)
5. **Fator de segurança** (margem de projeto)

---

## Fluxo de Cálculo

```
Dados de entrada
    │
    ├── Un_AT, Un_BT → Um_AT, Um_BT (tabela IEC 60038)
    │
    ├── Um → BIL, SIL, Uac (tabela IEC 60076-3) → [[niveis-isolamento]]
    │
    ├── Geometria dos enrolamentos (D_AT, D_BT, h, n_canecos...)
    │
    └── Tipo de isolamento (óleo puro / com barreiras)
                │
                ▼
    Cálculo de distâncias por par de eletrodos
                │
                ├── d_AT_tanque (AT externo → parede do tanque)
                ├── d_fundo (AT inferior → fundo do tanque)
                ├── d_topo (AT superior → tampa, sem comutador)
                ├── d_AT_BT (cilindro isolante)
                ├── d_entre_canecos (dentro do enrolamento)
                ├── d_comut_AT (comutador → AT)
                ├── d_comut_tanque (comutador → tanque)
                └── d_entre_fases (entre colunas adjacentes)
                │
                ▼
    Dimensões do tanque
```

---

## 1. d_AT_tanque — Parte Ativa Lateral ao Tanque

**Par de eletrodos**: Enrolamento AT externo (cilindro) → parede do tanque (plano aterrado)

**Geometria**: Cilindro-plano → campo levemente não uniforme → fator η ≈ 1,1–1,2

**Meio**: Óleo puro (ou óleo com barreiras de pressboard)

**Tensão determinante**: BIL_AT (geralmente) ou SIL_AT (para Um ≥ 300 kV, campo longo)

### Abordagem simplificada (campo uniforme equivalente):

$$d_{AT\_tanque} \geq \frac{U_{ensaio}}{E_{oleo}} \cdot \eta \cdot K_{seg}$$

Onde:
- `U_ensaio` = BIL_AT (kVp) ou SIL_AT
- `E_oleo` ≈ 10–15 kVp/mm (valor de projeto conservador)
- `η` = fator de campo
- `K_seg` = fator de segurança (1,1–1,3)

### Abordagem normativa (tabela empírica):

> A ser preenchida com os valores extraídos da IEC 60076-3 / prática do projetista

| BIL_AT (kVp) | d_AT_tanque mínimo (mm) — óleo |
|---|---|
| 95 | 15–20 |
| 170 | 20–28 |
| 325 | 30–40 |
| 550 | 50–65 |
| 750 | 70–90 |
| 950 | 90–110 |
| 1050 | 100–125 |

---

## 2. d_fundo — AT Inferior ao Fundo do Tanque

**Par de eletrodos**: Extremo inferior do enrolamento AT (pé) → fundo do tanque

**Tensão determinante**: BIL do extremo inferior (se graduado → menor BIL do neutro)

- Isolamento uniforme: BIL_AT pleno
- Isolamento graduado: BIL_neutro (pode ser muito menor)

$$d_{fundo} \approx d_{AT\_tanque} \cdot \frac{BIL_{neutro}}{BIL_{AT}}$$ (se graduado)

---

## 3. d_topo — AT Superior à Tampa (sem comutador)

**Par de eletrodos**: Extremo superior do enrolamento AT (linha, à BIL_AT pleno) → tampa do tanque

**Tensão determinante**: BIL_AT

Geralmente `d_topo ≈ d_AT_tanque` ou ligeiramente maior (pois o campo é mais desfavorável na direção vertical com geometria mais crítica).

---

## 4. d_entre_canecos

**Par de eletrodos**: Face superior caneco `n` → face inferior caneco `n+1`

**Tensão determinante**: Tensão entre canecos adjacentes sob impulso

Para enrolamento de disco contínuo, a tensão entre discos adjacentes no **topo do enrolamento** (distribuição não uniforme de impulso):

$$\Delta U_{caneco,impulso} = \alpha_{dist} \cdot \frac{BIL_{AT}}{n_c}$$

Onde `α_dist` ≥ 1 é o fator de distribuição não uniforme (depende de α, capacitâncias).

Para canecos extremos: `α_dist` pode ser 2–5× o valor médio.

$$d_{entre\_canecos} \geq \frac{\Delta U_{caneco,impulso}}{E_{oleo}} \cdot K_{seg}$$

---

## 5. d_AT_BT — Cilindro Isolante

**Par de eletrodos**: Superfície externa BT → superfície interna AT (campo radial)

**Tensão determinante**: 
- AC: tensão de ensaio induzida (≈ 2× Un_AT para ensaio de tensão induzida)
- Impulso: BIL_AT − BIL_BT (diferença de nível entre AT e BT)

O cilindro é projetado com múltiplas camadas de pressboard e canais de óleo:

$$t_{cil} = n_{PB} \cdot t_{PB} + (n_{PB}+1) \cdot d_{oleo\_canal}$$

---

## 6. d_comut_AT

**Par de eletrodos**: Terminal vivo do comutador → enrolamento AT

**Tensão determinante**: BIL dos terminais de regulação (função de Um_AT e ΔU_tap)

---

## 7. d_entre_fases (trifásico)

**Par de eletrodos**: AT fase A (externo) → AT fase B (externo)

**Tensão determinante**: Tensão fase-fase sob impulso

Para transformador aterrado solidamente (YN):
$$U_{fase-fase,impulso} \approx \sqrt{3} \cdot BIL_{AT}$$ (envoltória das duas fases)

Para isolamento fase-fase específico — a norma IEC 60076-3 fornece requisitos para ensaio de impulso entre fases.

---

## Fatores de Segurança Recomendados

| Ensaio | K_seg típico |
|---|---|
| BIL (impulso atmosférico) | 1,10–1,20 |
| SIL (impulso de manobra) | 1,10–1,15 |
| AC (frequência industrial) | 1,15–1,25 |

---

## Notas do usuário

> _Inserir metodologia adotada internamente, fatores de campo usados, tabelas de projeto calibradas com resultados experimentais_
