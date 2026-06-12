---
tags: [dominio, nucleo, core, magnetico]
---

# Núcleo Magnético

Relacionado: [[parametros-mecanicos]] | [[parte-ativa]] | [[enrolamentos]]

---

## Tipos de Núcleo

### Por geometria
| Tipo | Descrição | Aplicação |
|---|---|---|
| **Núcleo de coluna (core type)** | Bobinas envolvem as colunas | Transformadores de potência (maioria) |
| **Núcleo de manto (shell type)** | Núcleo envolve as bobinas | Alguns trafos especiais / tração |

### Por número de colunas
| Configuração | Fases | Observação |
|---|---|---|
| 1 coluna | Monofásico | Banco de monofásicos para 3φ |
| 3 colunas | Trifásico | Mais comum |
| 5 colunas | Trifásico | Permite transporte com altura reduzida (retira 2 colunas do jugo) |
| 3 colunas + 2 colunas de retorno | Trifásico | Shell type 3φ |

---

## Escalonamento da Coluna

A coluna é formada por camadas de chapas com larguras decrescentes, formando aproximação de seção circular.

```
    ████████████████     ← camada mais larga (w1)
  ████████████████████
████████████████████████ ← centro (wmáx)
  ████████████████████
    ████████████████     ← camada mais larga (w1)
```

- **Diâmetro inscrito `D_col`**: diâmetro do maior círculo que cabe nas chapas
- **Fator de corte (cutting factor)**: ≈ 0,785 para aproximação de 4 degraus
- Quanto mais degraus → maior fator de corte → menor perda de área → mais eficiente

**Graus de escalonamento típicos**: 4, 6, 8, 10, 12 degraus

---

## Indução Máxima

$$E = 4,44 \cdot f \cdot N \cdot A_{col} \cdot B_{max}$$

- `E`: tensão de fase (V)
- `f`: frequência (Hz)
- `N`: número de espiras
- `A_col`: seção da coluna (m²)
- `B_max`: indução de pico (T)

**Valores típicos de Bmax**:
| Material | Bmax típico |
|---|---|
| Aço silício GO (grain oriented) convencional | 1,55–1,70 T |
| Aço silício GO hi-B (HiB, Domain Refined) | 1,65–1,80 T |
| Aço amorfo | 1,25–1,35 T |

Bmax mais alto → núcleo menor → menor custo/massa, mas maiores perdas em vazio e corrente de magnetização.

---

## Material — Graus de Aço

Notação IEC (ex: `27ZH95`):
- `27` = espessura em décimos de mm (0,27 mm)
- `Z` = grão orientado (G = grano normale, Z = alto grau)
- `H` = alta permeabilidade (hi-B)
- `95` = perdas específicas máx em W/kg a 1,7 T

Graus comuns no mercado: 23ZDKH90, 27ZH95, 30ZH105, 30ZDKH95 (NSC), M4/M5/M6 (ASTM)

---

## Jugo (Yoke)

O jugo superior e inferior conecta as colunas e fecha o circuito magnético.

- `h_jugo`: altura do jugo (geralmente ≈ dimensão da camada mais larga da coluna)
- A prensagem do jugo é feita por tirantes ou estrutura metálica
- **Atenção**: partes metálicas do jugo são aterradas → distâncias elétricas em relação ao enrolamento AT!

---

## Distâncias do Núcleo para o App

| Grandeza | Descrição |
|---|---|
| `d_col_BT` | Distância da coluna para o enrolamento BT interno (canal de óleo + pressboard) |
| `d_BT_AT` | → ver [[enrolamentos]] e [[distancias-eletricas]] |

`d_col_BT` é determinado por:
1. Tensão fase-terra da BT (critério dielétrico)
2. Requisito de resfriamento (canal de óleo mínimo)
3. Montagem / tolerâncias mecânicas
