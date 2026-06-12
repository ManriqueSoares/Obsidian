---
tags: [codigo, python, javascript, three-js, html, 3d, exportador]
arquivo: export_html3d.py
versao: v0.1
---

# export_html3d.py — Exportador HTML 3D

Relacionado: [[app-py]] | [[../app/arquitetura]]

---

## Responsabilidade

Gera um arquivo `.html` **autocontido** com uma visualização 3D interativa do transformador usando **Three.js** (WebGL). Abre em qualquer browser moderno (Chrome, Edge, Firefox).

**Requer**: conexão à internet para carregar Three.js via CDN (jsdelivr).

---

## Função Pública

```python
def exportar_html3d(p: dict, filepath: str) -> None
```

- `p`: dicionário de parâmetros em mm (mesmo do `app.py`)
- `filepath`: caminho do arquivo `.html` a salvar

---

## Fluxo Python

```
p (mm)
  │
  ├─ S = 0.001  (fator mm→metros)
  │
  ├─ scene = { L, W, H, d_AT_tanque, ..., r_AT, r_BT, r_nucleo, ... }
  │                  (tudo em metros — unidades do Three.js)
  │
  ├─ info_rows = [("d_AT_tanque", "120 mm"), ...]
  │                  (strings para o painel HTML lateral)
  │
  └─ html = _HTML_TEMPLATE
              .replace("__SCENE_PARAMS__", json.dumps(scene))
              .replace("__INFO_HTML__", info_html)
              .replace("__N_FASES__", "3")
              .replace("__TEM_COMUT__", "Sim")
```

### Parâmetros da Cena (`scene` dict)

| Chave | Descrição | Derivado de |
|---|---|---|
| `L` | Comprimento do tanque (m) | `tanque_comprimento * 0.001` |
| `W` | Largura do tanque (m) | `tanque_largura * 0.001` |
| `H` | Altura do tanque (m) | `tanque_altura * 0.001` |
| `d_AT_tanque` | Folga lateral AT→tanque (m) | |
| `d_fundo` | Folga fundo (m) | |
| `d_topo` | Folga topo (m) | |
| `H_PA` | Altura da parte ativa (m) | `altura_PA * 0.001` |
| `r_AT` | Raio externo AT (m) | `diametro_AT_ext * 0.001 / 2` |
| `r_BT` | Raio externo BT (m) | `diametro_BT_ext * 0.001 / 2` |
| `r_nucleo` | Raio do núcleo (m) | `diametro_nucleo * 0.001 / 2` |
| `n_fases` | Número de fases | `int(p["n_fases"])` |
| `n_canecos` | Número de canecos | `int(p["n_canecos"])` |
| `h_caneco` | Altura de cada caneco (m) | |
| `d_entre_canecos` | Canal entre canecos (m) | |
| `tem_comutador` | Boolean | |
| `h_comutador` | Altura do comutador (m) | |
| `d_comut_AT` | Folga comutador→AT (m) | |
| `d_comut_tanque` | Folga comutador→topo tanque (m) | |

---

## Template HTML — Estrutura

```
<head>
  styles (dark engineering theme)
  importmap → Three.js 0.160.0 (jsdelivr CDN)
</head>
<body>
  #legend         → painel direito (legenda de cores + dicas de controle)
  #info           → painel esquerdo (tabela de distâncias em mm)
  #title-bar      → rodapé centralizado
  <canvas>        → renderizado pelo Three.js
  <script module>  → toda a lógica 3D
</body>
```

---

## Three.js — Cena 3D

### Versão e Carregamento

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
  }
}
</script>
```

Usa **ES Modules** (`import * as THREE from 'three'`) — requer browser moderno (Chrome 89+, Edge 89+, Firefox 108+).

### Sistema de Coordenadas

```
Y↑
│   Z (profundidade — largura do tanque)
│  /
│ /
└──── X (comprimento do tanque, eixo das fases)
```

- **Origem**: centro geométrico do tanque
- Tanque ocupa: `[-L/2, L/2]` em X, `[-H/2, H/2]` em Y, `[-W/2, W/2]` em Z
- Parte ativa sobe de `y_bottom = -H/2`, com offset `d_fundo`

### Câmera

```javascript
const maxDim = Math.max(p.L, p.H, p.W);
camera.position.set(maxDim * 1.4, maxDim * 1.1, maxDim * 1.8);
```

FOV 40°, perspectiva. Distância proporcional à maior dimensão do transformador.

### Iluminação

| Luz | Tipo | Cor | Intensidade | Posição |
|---|---|---|---|---|
| Ambiente | `AmbientLight` | branco | 0.55 | — |
| Principal | `DirectionalLight` | branco | 0.90 | `(4, 8, 5)` |
| Preenchimento | `DirectionalLight` | azul-escuro | 0.35 | `(-4, -4, -4)` |

### Materiais

| Material | Cor hex | Opacidade | `depthWrite` | Uso |
|---|---|---|---|---|
| `matTankFace` | `0x445566` | 0.07 | false | Faces do tanque |
| `matTankEdge` | `0x4a8fa0` | — | — | Arestas do tanque |
| `matCore` | `0x778899` | 1.0 | true | Núcleo magnético |
| `matBT` | `0x2a6eaf` | 0.80 | false | Enrolamento BT |
| `matAT` | `0xb03020` | 0.88 | false | Canecos AT |
| `matComut` | `0x7e34ad` | 0.85 | false | Comutador |

> `depthWrite: false` nos materiais transparentes evita artefatos de Z-fighting entre cilindros concêntricos.

---

## Geometria por Elemento

### Tanque — `boxWire(L, H, W)`

```javascript
const geo  = new THREE.BoxGeometry(L, H, W);
const face = new THREE.Mesh(geo, matTankFace);        // faces transparentes
const edge = new THREE.LineSegments(
               new THREE.EdgesGeometry(geo), matTankEdge  // arestas visíveis
             );
face.add(edge);
```

### Piso do Tanque

`PlaneGeometry` horizontal em `y = yBottom + 0.001`, cor verde-escuro semitransparente — simula a superfície de fundo do tanque com óleo.

### Grelha de Referência

`GridHelper` abaixo do tanque (`y = yBottom - 0.05`). Tamanho proporcional à maior dimensão horizontal.

### Posições das Fases — `phasePositions()`

```javascript
// n_fases = 1
return [0];

// n_fases = 3
x0 = -p.L/2 + p.d_AT_tanque + p.r_AT   // posição da fase A
x1 =  p.L/2 - p.d_AT_tanque - p.r_AT   // posição da fase C
// fases igualmente espaçadas entre x0 e x1
```

### Por Fase (cilindros concêntricos)

```
yPA = yBottom + d_fundo + H_PA/2     ← centro vertical da parte ativa

Núcleo:   CylinderGeometry(r_nucleo, r_nucleo, H_PA, 24)  — sólido
BT:       CylinderGeometry(r_BT,     r_BT,     H_PA, 32)  — semi-transparente
AT:       n_canecos × CylinderGeometry(r_AT, r_AT, h_caneco, 32)
          posicionados em: y = yBottom + d_fundo + i*(h_caneco + d_ec) + h_caneco/2
Comutador: CylinderGeometry(r_AT*0.82, r_AT*0.82, h_comutador, 32)
           y = yBottom + d_fundo + H_PA + d_comut_AT + h_comutador/2
```

> O AT é renderizado como **canecos individuais** (discos empilhados), não como um cilindro único — visualiza os canais entre canecos.

---

## Cotas 3D

### `cotaLine(a, b, color)` — linhas de cota

`BufferGeometry` com 2 pontos → `THREE.Line` amarelo.

### `makeSprite(text, color)` — rótulos flutuantes

Canvas 2D (`256×64 px`) desenhado no CPU → `THREE.CanvasTexture` → `THREE.Sprite`.

- `depthTest: false` → sempre visível à frente da geometria
- Escala: `0.45 × 0.11` metros

### Cotas desenhadas

| Cota | Linha de / até | Sprite |
|---|---|---|
| `d_AT_tanque` | `xTankL → xEdgeAT` na altura do meio da PA | `"d_AT_tank: Xmm"` |
| `d_fundo` | `yBottom → yBottom+d_fundo` em X externo | `"d_fundo: Xmm"` |
| `d_topo` | `yTopPA → yTopTank` em X externo | `"d_topo: Xmm"` |

---

## OrbitControls

```javascript
controls.enableDamping = true;
controls.dampingFactor = 0.06;
controls.minDistance   = 0.3;
controls.maxDistance   = 20;
```

Navegação: arrastar (orbitar), scroll (zoom), botão direito (pan).

---

## Painel de Informações (HTML overlay)

Gerado em Python como string HTML:

```python
info_rows = [
    ("d_AT_tanque", "120 mm"),
    ("d_fundo", "180 mm"),
    ...
]
info_html = "".join(
    f'<div class="info-row"><span class="info-label">{k}</span>'
    f'<span class="info-val">{v}</span></div>'
    for k, v in info_rows
)
```

Injetado no template via `.replace("__INFO_HTML__", info_html)`.

---

## Limitações Conhecidas (v0.1)

| # | Limitação | Prioridade fix |
|---|---|---|
| 1 | Requer internet (Three.js via CDN) | v0.2 — opção de bundle offline |
| 2 | Apenas 3 cotas 3D (d_AT_tanque, d_fundo, d_topo) | v0.2 — adicionar d_comut_AT, d_entre_fases |
| 3 | Não mostra leads/ligações | v0.2 |
| 4 | Cilindro BT sobrepõe visualmente o núcleo (layers transparentes) | Cosmético — ajustar z-order |
| 5 | Sem animação de "explosão" (exploded view) | v0.3 |
| 6 | n_fases = 5 não contemplado | Não planejado |

---

## Dependências

```python
import json  # biblioteca padrão Python
```

JavaScript (CDN):
```
three@0.160.0 — https://cdn.jsdelivr.net/npm/three@0.160.0/
OrbitControls — three/examples/jsm/controls/OrbitControls.js
```
