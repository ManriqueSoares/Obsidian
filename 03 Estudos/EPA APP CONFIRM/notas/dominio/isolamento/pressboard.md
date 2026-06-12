---
tags: [dominio, isolamento, pressboard, papel, solido]
---

# Pressboard e Papel Isolante

Relacionado: [[isolamento-oleo]] | [[enrolamentos]] | [[distancias-eletricas]]

---

## Tipos de Material Sólido

| Material | Norma | Aplicação |
|---|---|---|
| **Papel Kraft (KP)** | IEC 60554 | Isolação de condutores (OIP) |
| **Pressboard (PB)** | IEC 60641 | Cilindros, espaçadores, anéis, barreiras |
| **Pressboard moldado** | IEC 60641-3 | Peças moldadas complexas |
| **Madeira densificada (Densified wood)** | — | Estruturas de pressagem |

---

## Pressboard — Propriedades

| Propriedade | Valor típico |
|---|---|
| Rigidez dielétrica (AC, óleo, ⊥ lâminas) | 30–50 kV/mm |
| Rigidez dielétrica (AC, seco, ⊥ lâminas) | 15–25 kV/mm |
| Permissividade relativa `εr` | 4,0–4,5 |
| Absorção de umidade | Alta → deve ser secado/impregnado antes do uso |
| Espessuras disponíveis | 0,5 / 1,0 / 2,0 / 3,0 / 4,5 / 6,0 mm (Weidmann, etc.) |

---

## Cilindro Isolante (AT-BT)

O cilindro isolante separa os enrolamentos AT e BT radialmente.

```
        │ BT (ext) │── d_oleo1 ──│ PB1 │── d_oleo2 ──│ PB2 │── d_oleo3 ──│ AT (int) │
```

Composição típica (campo radial):
- Camadas de pressboard intercaladas com canais de óleo
- Canais de óleo radiais mantidos por espaçadores

**Espessura total do cilindro** `t_cil`:

$$t_{cil} = \sum t_{PB,i} + \sum d_{oleo,i}$$

A suportabilidade do conjunto é calculada pelo critério de campo em cada camada.

---

## Papel Kraft nos Condutores

Condutores dos enrolamentos são envoltos em papel Kraft impregnado em óleo (OIP):

| Parâmetro | Valor |
|---|---|
| Espessura por camada | 0,05–0,15 mm |
| Número de camadas | 2–20 (depende da tensão entre espiras) |
| Tensão entre espiras → papel total | `n_camadas × t_papel × E_papel` |

A isolação de papel é projetada para suportar:
- Tensão entre espiras adjacentes (campo radial)
- Tensão impulso (distribuição capacitiva)

---

## Espaçadores e Blocos

- **Espaçadores axiais (key spacers)**: mantêm os canais de óleo entre canecos
  - Espessura = `d_entre_canecos`
  - Colocados radialmente ao longo do diâmetro médio do disco
- **Anéis terminais (end rings)**: reforçam o isolamento nos extremos do enrolamento
- **Ângulos de canto (corner blocks)**: proteção nas arestas vivas das bobinas

---

## Envelhecimento

O papel Kraft envelhece pelo calor → degradação celulósica (hidrólise):
- Temperatura: cada +6°C dobra a taxa de envelhecimento (regra de Montsinger)
- Produto de degradação: furfuraldeído (indicador de envelhecimento no óleo)
- Vida útil projetada: 25–40 anos em temperatura ≤ 98°C no ponto mais quente

---

## Notas do usuário

> _Fornecedores utilizados (Weidmann, Delekta, Ekomax), espessuras padrão de projeto_
