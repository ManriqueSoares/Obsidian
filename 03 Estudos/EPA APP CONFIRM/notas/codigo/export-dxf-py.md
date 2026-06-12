---
tags: [codigo, python, dxf, ezdxf, exportador, CAD]
arquivo: export_dxf.py
versao: v0.1
---

# export_dxf.py — Exportador DXF

Relacionado: [[app-py]] | [[../app/arquitetura]] | [[../dominio/distancias-eletricas]]

---

## Responsabilidade

Gera um arquivo `.dxf` (formato R2010) com duas vistas do transformador:
- **Corte Frontal** (Vista A-A): corte longitudinal vertical, todas as fases
- **Vista Superior**: corte horizontal, círculos concêntricos por fase

Compatível com AutoCAD, FreeCAD, BricsCAD, LibreCAD, ZWCAD.

---

## Função Pública

```python
def exportar_dxf(p: dict, filepath: str) -> None
```

- `p`: dicionário de parâmetros (mesmo formato do `app.py` — valores em **mm**)
- `filepath`: caminho completo do arquivo `.dxf` a ser criado

---

## Estrutura do DXF Gerado

### Unidades
```python
doc.header["$INSUNITS"] = 4  # mm
```
Todos os objetos são desenhados em milímetros (1 unidade DXF = 1 mm).

### Camadas (Layers)

| Layer | Cor ACI | Hex equivalente | Conteúdo |
|---|---|---|---|
| `TANQUE` | 7 | branco/preto | Contorno do tanque |
| `AT` | 1 | vermelho | Enrolamento AT (hachura + contorno) |
| `BT` | 5 | azul | Enrolamento BT |
| `NUCLEO` | 8 | cinza | Núcleo magnético |
| `COMUTADOR` | 6 | magenta | Comutador (tap changer) |
| `COTAS` | 3 | verde | Linhas de cota e extensão |
| `TEXTO` | 2 | amarelo | Rótulos e bloco de título |

> A cor ACI (AutoCAD Color Index) define a cor na interface CAD. No modelo de fundo branco as cores podem aparecer diferentes — configurável no CAD.

### Estilo de Cota `EPA`

```python
ds.dxf.dimtxt  = 28   # altura do texto (mm)
ds.dxf.dimasz  = 20   # tamanho da seta
ds.dxf.dimexe  = 12   # extensão da linha de extensão além do ponto
ds.dxf.dimexo  = 8    # offset da linha de extensão até o ponto medido
ds.dxf.dimclrd = 3    # cor da linha de cota = verde (layer COTAS)
ds.dxf.dimclrt = 3    # cor do texto da cota
ds.dxf.dimclre = 3    # cor das linhas de extensão
ds.dxf.dimdec  = 0    # casas decimais = 0 (valores inteiros em mm)
```

### Layout no Model Space

```
x=0                x=L          x=L+400        x=2L+400
│                  │            │              │
│  CORTE FRONTAL   │            │ VISTA SUPER. │
│  (0,0)→(L,H)     │← 400 mm →│ (L+400,0)    │
│                  │            │              │
```

Bloco de título acima de ambas as vistas, na altura `H + 300 mm`.

---

## Funções Internas (Helpers)

### `_rect(msp, x, y, w, h, layer, lw=25)`
Desenha um retângulo como `LWPOLYLINE` fechada. Apenas o contorno (sem preenchimento).

### `_hatch_rect(msp, x, y, w, h, layer, aci_color)`
Desenha retângulo **preenchido** com hachura `SOLID`:
1. Cria entidade `HATCH` com padrão SOLID na cor ACI especificada
2. Chama `_rect()` para o contorno (lineweight 15)

> O padrão SOLID em ezdxf preenche com a cor da layer — compatível com todos os viewers DXF.

### `_hdim(msp, x1, x2, y_pts, y_base, style)`
Cota horizontal entre `x1` e `x2`:
- `y_pts`: altura Y dos pontos medidos (onde as linhas de extensão partem)
- `y_base`: altura Y onde a linha de cota se posiciona (geralmente abaixo do desenho)
- Usa `msp.add_linear_dim()` com `angle=0`
- Envolvida em `try/except` — falha silenciosa se a geometria for inválida

### `_vdim(msp, y1, y2, x_pts, x_base, style)`
Cota vertical entre `y1` e `y2`:
- `x_pts`: posição X dos pontos medidos
- `x_base`: posição X da linha de cota (geralmente à esquerda/direita do desenho)
- `angle=90`

### `_label(msp, text, x, y, height=30, layer="TEXTO")`
Insere entidade `TEXT` simples. Ancoragem no canto inferior esquerdo.

### `_phase_centers(p) → list[float]`
Calcula centros X de cada fase (em mm, coordenadas do model space):

```python
# Para n_fases = 1:
return [L / 2]

# Para n_fases = 3:
esp = (L - 2*d_lat - n_f*D_AT) / (n_f - 1) + D_AT
x0 = d_lat + D_AT / 2
return [x0 + i * esp for i in range(n_f)]
```

> Mesma lógica usada em `vista_superior()` do `app.py` — necessário manter sincronizado se a lógica mudar.

---

## Vista: Corte Frontal — `_desenhar_corte(msp, p, ox, oy, style)`

Desenha com origem em `(ox, oy)` (permite posicionamento no model space).

### Elementos desenhados por fase:

Para cada `cx` em `_phase_centers(p)`:

```
ax = ox + cx          ← centro X absoluto da fase

Núcleo:
  x: ax - D_n/2  →  ax + D_n/2
  y: oy + d_fundo  →  oy + d_fundo + H_PA

BT (duas faixas, uma de cada lado do núcleo):
  Largura de cada faixa: bw = D_BT/2 - D_n/2
  Esquerda: ax - D_BT/2  →  ax - D_n/2
  Direita:  ax + D_n/2   →  ax + D_BT/2

AT (duas faixas externas ao BT):
  Largura de cada faixa: aw = D_AT/2 - D_BT/2
  Esquerda: ax - D_AT/2  →  ax - D_BT/2
  Direita:  ax + D_BT/2  →  ax + D_AT/2
```

### Comutador (se `tem_comutador`):
- Largura: `D_AT + 40 mm` (margem de 20 mm de cada lado)
- Y início: `oy + d_fundo + H_PA + d_comut_AT`

### Cotas no corte frontal:
| Cota | Direção | Posição |
|---|---|---|
| `d_AT_tanque` | horizontal | abaixo do desenho, margem `-60` |
| `L_tanque` | horizontal | abaixo, margem `-120` |
| `d_fundo` | vertical | à esquerda, margem `-60` |
| `H_PA` | vertical | à direita, margem `+60` |
| `d_topo` ou `d_comut_topo` | vertical | à esquerda, margem `-60` |
| `H_tanque` | vertical | à direita, margem `+120` |
| `d_entre_fases` | horizontal | acima do desenho, margem `+60` |

---

## Vista: Superior — `_desenhar_superior(msp, p, ox, oy, style)`

### Elementos por fase:
- `CIRCLE` com raio `D_AT/2` na layer `AT`
- `CIRCLE` com raio `D_BT/2` na layer `BT`
- `CIRCLE` com raio `D_n/2` na layer `NUCLEO`
- Linhas de centro (linetype `CENTER`, layer `TEXTO`)

### Cotas na vista superior:
| Cota | Posição |
|---|---|
| `d_AT_tanque` esquerdo | horizontal abaixo |
| `L_tanque` | horizontal abaixo |
| `W_tanque` | vertical à direita |
| `d_AT_tanque` superior | vertical acima da fase |
| `d_entre_fases` | horizontal acima (só trifásico) |

---

## Bloco de Título

Retângulo com rótulo e linha de dados:
```python
f"Sn: {p.get('Sn_MVA', '—')} MVA  |  Un_AT: ... kV  |  Un_BT: ... kV  |  Fases: ..."
```

> `Sn_MVA`, `Un_AT_kV`, `Un_BT_kV` ainda não existem no formulário (v0.1). Mostram `—`. Serão adicionados na v0.2 com os parâmetros elétricos.

---

## Limitações Conhecidas (v0.1)

| # | Limitação | Prioridade fix |
|---|---|---|
| 1 | Sem detalhe de canecos na vista DXF | v0.2 |
| 2 | Sem detalhe do comutador em vista separada | v0.2 |
| 3 | `Sn`, `Un_AT`, `Un_BT` ainda não passados | v0.2 (junto com campos elétricos) |
| 4 | Sem paperspace / layouts nomeados | v0.2 |
| 5 | Linetype CENTER pode não aparecer em todos os viewers | Cosmético |

---

## Dependência

```python
import ezdxf              # pip install ezdxf
from ezdxf import colors  # (importado mas não usado diretamente)
from ezdxf.enums import TextEntityAlignment  # (importado, reservado)
```

> **Versão pinada**: `ezdxf==1.4.4` (ver `requirements.txt` e `.venv`)
