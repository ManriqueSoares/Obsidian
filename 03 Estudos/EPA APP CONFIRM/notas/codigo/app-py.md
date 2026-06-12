---
tags: [codigo, python, tkinter, matplotlib, app-principal]
arquivo: app.py
versao: v0.1
---

# app.py — Aplicação Principal

Relacionado: [[export-dxf-py]] | [[export-html3d-py]] | [[../app/arquitetura]] | [[../app/versoes]]

---

## Responsabilidade

Ponto de entrada da aplicação. Contém:
1. **Paleta de cores** e constantes visuais
2. **Helpers de desenho** matplotlib (cotas, retângulos)
3. **Quatro vistas** matplotlib (corte frontal, superior, canecos, comutador)
4. **Classe `App`** — janela tkinter com formulário de entrada e painel de visualização

---

## Constantes Globais

```python
COR = {
    "tanque":    "#4a4a4a",
    "oleo":      "#f5e6c8",   # fundo amarelado (cor do óleo)
    "nucleo":    "#7f7f7f",
    "bobina_BT": "#3a7ebf",
    "bobina_AT": "#c0392b",
    "comutador": "#8e44ad",
    "cota":      "#2c3e50",
    "fundo_app": "#f0f0f0",
}

ESPESSURA_TANQUE = 0.05  # metros — só visual, não usado no cálculo
```

---

## Conversão de Unidades

```python
def mm(v) -> float:
    """Converte mm → metros para uso nos eixos matplotlib."""
    return v / 1000.0
```

> Todas as entradas do usuário estão em **mm**. O matplotlib plota em **metros**. A função `mm()` é chamada em toda a camada de desenho.

---

## Helpers de Desenho

### `_cota_horizontal(ax, x1, x2, y, valor, unidade, cor)`
- Desenha seta dupla `↔` horizontal entre `x1` e `x2` na altura `y`
- Rótulo centralizado: `"<valor> <unidade>"`
- Usa `ax.annotate` com `arrowstyle="<->"`

### `_cota_vertical(ax, x, y1, y2, valor, unidade, cor)`
- Igual, mas vertical (entre `y1` e `y2` na posição `x`)

### `_retangulo(ax, x, y, w, h, cor_face, cor_borda, alpha, lw, label)`
- Wrapper de `patches.Rectangle`
- Retorna o patch (permite adicionar à legenda)

---

## Vistas Matplotlib

Todas recebem `(ax, p)` onde `p` é o dicionário de parâmetros coletados do formulário.

### `vista_corte_frontal(ax, p)` — subplot `[0][0]`

**O que desenha:**
- Tanque (contorno)
- Fase central: núcleo (cinza), BT (azul, duas faixas), AT (vermelho, duas faixas)
- Comutador acima da parte ativa (se `tem_comutador`)
- Cotas: `d_fundo`, `d_topo`, `d_AT_tanque`, `H_PA`, `H_tanque`, `d_comut_AT`, `d_comut_tanque`

**Simplificação atual:**
- Só desenha a fase central (`x_centro = L / 2`) — não as 3 fases lado a lado
- A largura visual de AT e BT é fixa em `15 mm` e `10 mm` respectivamente (não proporcional)
- → **TODO v0.2**: calcular faixas proporcionais a partir de `D_AT`, `D_BT`, `D_nucleo`

### `vista_superior(ax, p)` — subplot `[0][1]`

**O que desenha:**
- Tanque (contorno)
- Para cada fase: círculos concêntricos AT (vermelho), BT (azul), núcleo (cinza)
- Rótulos "Fase A/B/C" no centro
- Cotas: `d_AT_tanque` lateral, `d_entre_fases`, largura do tanque

**Cálculo de posição das fases:**
```python
espacamento = (L - 2*d_AT_tanque - n_f*D_AT) / (n_f - 1) + D_AT
x0 = d_AT_tanque + D_AT/2
centros_x = [x0 + i * espacamento for i in range(n_f)]
```

### `vista_canecos(ax, p)` — subplot `[1][0]`

**O que desenha:**
- Stack vertical de `n_canecos` retângulos representando seções AT
- Rótulo "C1, C2, ... Cn" em cada caneco
- Cotas: `d_entre_canecos` (entre todos os pares), `h_caneco`, largura radial

**Simplificação atual:**
- Mostra apenas a metade radial do caneco (largura = `(D_AT - D_BT) / 2`)
- Não mostra canecos de extremidade diferenciados (end discs)

### `vista_comutador(ax, p)` — subplot `[1][1]`

**O que desenha:**
- Vista de detalhe vertical: tanque (altura calculada = H_PA + folgas + comutador), AT, comutador
- Cotas: `d_comut_AT`, `d_comut_tanque`
- Se `tem_comutador = False`: exibe mensagem "Sem comutador configurado"

**Nota:** A altura do tanque nesta vista é **local** (só considera as folgas do comutador), diferente do tanque real.

---

## Orquestrador das Vistas

```python
def gerar_visualizacao(p: dict, frame_canvas: ttk.Frame):
```
- Destroi widgets anteriores do `frame_canvas`
- Cria figura `2×2` (figsize `14×10`)
- Chama as 4 vistas
- Embute o canvas matplotlib no frame tkinter via `FigureCanvasTkAgg`
- Fecha a figura com `plt.close(fig)` para liberar memória

---

## Classe `App(tk.Tk)`

### Layout
```
┌──────────────────────────────────────────────────────┐
│ frame_esq (340px fixo)    │  frame_canvas (expansível)│
│  ┌─────────────────────┐  │                           │
│  │ canvas_scroll        │  │   matplotlib 2×2         │
│  │  └─ frame_entradas   │  │                           │
│  │     ├─ LabelFrame    │  │                           │
│  │     └─ ...           │  │                           │
│  ├─ [⬇ DXF][⬇ 3D HTML]  │  │                           │
│  └─ [▶ Gerar]           │  │                           │
└──────────────────────────────────────────────────────┘
```

> **Detalhe de layout**: os botões são empacotados com `side="bottom"` **antes** do `canvas_scroll` para garantir que o tkinter reserve espaço para eles antes de expandir o scroll.

### Métodos de UI

| Método | Descrição |
|---|---|
| `_secao(titulo)` | Cria `LabelFrame` e empacota em `frame_entradas` |
| `_campo(frame, label, chave, default, unidade)` | Campo numérico: `Label + Entry (DoubleVar) + Label unidade` |
| `_check(frame, label, chave, default)` | Checkbox: `BooleanVar` |
| `_combo(frame, label, chave, opcoes, default)` | Combobox com lista de inteiros |
| `_build_secoes()` | Constrói todos os campos nas 4 seções |

### Seções do Formulário

| Seção | Campos |
|---|---|
| **Tanque** | comprimento, largura, altura, n_fases |
| **Parte Ativa** | altura_PA, D_AT_ext, D_BT_ext, D_nucleo, folga_AT_BT, d_AT_tanque, d_fundo, d_topo, d_entre_fases |
| **Canecos** | n_canecos, h_caneco, d_entre_canecos |
| **Comutador** | tem_comutador (bool), altura_comutador, d_comut_AT, d_comut_tanque |

### `_coletar() → dict`

Lê todas as `tk.Var` e retorna dicionário com coerções de tipo:
- `n_canecos` → `int`
- `n_fases` → `int`
- `tem_comutador` → `bool`

### Métodos de Exportação

```python
def _exportar_dxf(self)       # abre filedialog → chama exportar_dxf(p, path)
def _exportar_html3d(self)    # abre filedialog → chama exportar_html3d(p, path)
```

---

## Dicionário de Parâmetros `p`

Todas as chaves e tipos esperados:

```python
p = {
    # Tanque
    "tanque_comprimento": float,  # mm
    "tanque_largura":     float,  # mm
    "tanque_altura":      float,  # mm
    "n_fases":            int,    # 1 ou 3

    # Parte Ativa
    "altura_PA":          float,  # mm
    "diametro_AT_ext":    float,  # mm
    "diametro_BT_ext":    float,  # mm
    "diametro_nucleo":    float,  # mm
    "folga_AT_BT":        float,  # mm
    "d_AT_tanque":        float,  # mm
    "d_fundo":            float,  # mm
    "d_topo":             float,  # mm
    "d_entre_fases":      float,  # mm

    # Canecos
    "n_canecos":          int,
    "h_caneco":           float,  # mm
    "d_entre_canecos":    float,  # mm

    # Comutador
    "tem_comutador":      bool,
    "altura_comutador":   float,  # mm
    "d_comut_AT":         float,  # mm
    "d_comut_tanque":     float,  # mm
}
```

---

## Limitações Conhecidas (v0.1)

| # | Limitação | Impacto | Prioridade fix |
|---|---|---|---|
| 1 | Corte frontal mostra só fase central, não as 3 fases | Visual incompleto para 3φ | v0.2 |
| 2 | Largura das faixas AT/BT no corte frontal é fixa (15/10 mm) | Não proporcional a D_AT/D_BT reais | v0.2 |
| 3 | Não existe validação de entradas (ex: D_BT > D_AT) | App pode gerar geometria inválida | v0.2 |
| 4 | Sem salvar/carregar configuração (JSON) | Perde parâmetros ao fechar | v0.2 |
| 5 | Sem campos elétricos (Sn, Un, BIL) | Não calcula distâncias automaticamente | v1.0 |

---

## Dependências

```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from export_dxf import exportar_dxf      # local
from export_html3d import exportar_html3d  # local
```

> `numpy` importado mas ainda não utilizado diretamente nas vistas (reservado para v0.2 com cálculos).
