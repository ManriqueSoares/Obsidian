---
tags: [app, arquitetura, python, tkinter, matplotlib]
---

# Arquitetura do App

Relacionado: [[versoes]]

## Stack

| Camada | Tecnologia |
|---|---|
| Interface de entrada | `tkinter` + `ttk` (nativo Python, sem instalação extra) |
| Visualização | `matplotlib` (embutido via `FigureCanvasTkAgg`) |
| Cálculos | `numpy` |
| Exportação (futuro) | `reportlab` ou `openpyxl` |

## Estrutura de arquivos

```
app.py              ← aplicação monolítica (v0.1)
requirements.txt    ← dependências pip
```

## Vistas geradas pelo app

1. **Corte Frontal (Vista A-A)**: tanque em corte, parte ativa centralizada, distâncias laterais e de fundo/topo anotadas
2. **Vista Superior (corte horizontal)**: fase única ou trifásico, distância entre fases, parte ativa → tanque
3. **Detalhe dos Canecos**: zoom no enrolamento, mostrando seções, canais e distâncias
4. **Detalhe do Comutador**: posicionamento e distâncias do tap changer

## Entradas do usuário (v0.1)

Todas as distâncias são inseridas manualmente pelo usuário (sem cálculo normativo ainda).

### Seção: Geometria Geral
- Largura interna do tanque
- Comprimento interno do tanque
- Altura interna do tanque
- Número de fases

### Seção: Parte Ativa
- Altura da parte ativa
- Diâmetro externo do enrolamento AT
- Folga fundo (d_fundo)
- Folga topo (d_topo)
- Folga lateral AT → tanque (d_AT_tanque)

### Seção: Canecos
- Número de canecos
- Altura de cada caneco
- Distância entre canecos
- Diâmetro interno / externo

### Seção: Comutador
- Tipo (DETC / OLTC / Nenhum)
- Posição (topo)
- Altura do comutador
- d_comut_AT
- d_comut_tanque

## Saída

- Janela dividida em quadrantes com as 4 vistas
- Cotas desenhadas com setas e valores
- Legenda de cores (AT, BT, núcleo, tanque, comutador)
