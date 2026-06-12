"""
Exportador HTML 3D — Visualização interativa via Three.js.
Gera um arquivo .html autocontido que abre em qualquer browser moderno.
Requer conexão à internet para carregar Three.js (CDN).
"""
import json


def exportar_html3d(p: dict, filepath: str):
    S = 0.001  # mm → metros

    # Parâmetros da cena (tudo em metros)
    scene = {
        "L": p["tanque_comprimento"] * S,
        "W": p["tanque_largura"] * S,
        "H": p["tanque_altura"] * S,
        "d_AT_tanque": p["d_AT_tanque"] * S,
        "d_fundo": p["d_fundo"] * S,
        "d_topo":  p["d_topo"] * S,
        "H_PA":    p["altura_PA"] * S,
        "r_AT":    p["diametro_AT_ext"] * S / 2,
        "r_BT":    p["diametro_BT_ext"] * S / 2,
        "r_nucleo": p["diametro_nucleo"] * S / 2,
        "n_fases":  int(p["n_fases"]),
        "n_canecos": int(p["n_canecos"]),
        "h_caneco":       p["h_caneco"] * S,
        "d_entre_canecos": p["d_entre_canecos"] * S,
        "tem_comutador":  bool(p["tem_comutador"]),
        "h_comutador":    p["altura_comutador"] * S,
        "d_comut_AT":     p["d_comut_AT"] * S,
        "d_comut_tanque": p["d_comut_tanque"] * S,
    }

    # Painel de informações (valores em mm para exibição)
    info_rows = [
        ("d_AT_tanque",     f"{p['d_AT_tanque']:.0f} mm"),
        ("d_fundo",         f"{p['d_fundo']:.0f} mm"),
        ("d_topo",          f"{p['d_topo']:.0f} mm"),
        ("H_PA",            f"{p['altura_PA']:.0f} mm"),
        ("D_AT_ext",        f"{p['diametro_AT_ext']:.0f} mm"),
        ("D_BT_ext",        f"{p['diametro_BT_ext']:.0f} mm"),
        ("n_canecos",       f"{int(p['n_canecos'])}"),
        ("h_caneco",        f"{p['h_caneco']:.0f} mm"),
        ("d_entre_canecos", f"{p['d_entre_canecos']:.0f} mm"),
    ]
    if p["tem_comutador"]:
        info_rows += [
            ("d_comut_AT",     f"{p['d_comut_AT']:.0f} mm"),
            ("d_comut_tanque", f"{p['d_comut_tanque']:.0f} mm"),
        ]

    info_html = "".join(
        f'<div class="info-row"><span class="info-label">{k}</span>'
        f'<span class="info-val">{v}</span></div>'
        for k, v in info_rows
    )

    html = _HTML_TEMPLATE \
        .replace("__SCENE_PARAMS__", json.dumps(scene, indent=2)) \
        .replace("__INFO_HTML__", info_html) \
        .replace("__N_FASES__", str(int(p["n_fases"]))) \
        .replace("__TEM_COMUT__", "Sim" if p["tem_comutador"] else "Não")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)


# ─── Template HTML ───────────────────────────────────────────────────────────

_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Transformador 3D — EPA</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #0d1117; overflow: hidden; font-family: 'Consolas', monospace; }
  canvas { display: block; }

  .panel {
    position: fixed; background: rgba(10,15,25,0.88);
    border: 1px solid #2a3a4a; border-radius: 8px;
    padding: 14px 16px; color: #cdd9e5; font-size: 12px;
    backdrop-filter: blur(4px);
  }

  #legend { top: 18px; right: 18px; min-width: 170px; }
  #legend h3 { color: #f0c040; font-size: 13px; margin-bottom: 10px; }
  .leg-row { display: flex; align-items: center; gap: 8px; margin: 4px 0; }
  .leg-box { width: 14px; height: 14px; border-radius: 3px; flex-shrink: 0; }
  #legend hr { border-color: #2a3a4a; margin: 10px 0; }
  #legend .hint { color: #7a8a9a; font-size: 11px; line-height: 1.7; }

  #info { top: 18px; left: 18px; min-width: 230px; }
  #info h3 { color: #f0c040; font-size: 13px; margin-bottom: 10px; }
  .info-row { display: flex; justify-content: space-between; gap: 16px;
               margin: 3px 0; }
  .info-label { color: #8aabcc; }
  .info-val { color: #e6edf3; font-weight: bold; }

  #title-bar { bottom: 18px; left: 50%; transform: translateX(-50%);
               padding: 8px 22px; font-size: 13px; color: #8aabcc;
               white-space: nowrap; }
</style>
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
  }
}
</script>
</head>
<body>

<div class="panel" id="legend">
  <h3>Legenda</h3>
  <div class="leg-row"><div class="leg-box" style="background:#888"></div>Núcleo</div>
  <div class="leg-row"><div class="leg-box" style="background:#3a7ebf"></div>Enrolamento BT</div>
  <div class="leg-row"><div class="leg-box" style="background:#c0392b"></div>Canecos AT</div>
  <div class="leg-row"><div class="leg-box" style="background:#8e44ad"></div>Comutador</div>
  <div class="leg-row"><div class="leg-box" style="border:1px solid #555;background:rgba(100,100,100,0.15)"></div>Tanque</div>
  <hr>
  <div class="hint">
    Arrastar: orbitar<br>
    Scroll: zoom<br>
    Botão dir.: mover<br>
    Fases: __N_FASES__ | Comutador: __TEM_COMUT__
  </div>
</div>

<div class="panel" id="info">
  <h3>Distâncias Elétricas</h3>
  __INFO_HTML__
</div>

<div class="panel" id="title-bar">
  EPA — Visualização 3D Interativa de Distâncias Elétricas
</div>

<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// ── Parâmetros injetados pelo Python ────────────────────────────────────────
const p = __SCENE_PARAMS__;

// ── Cena ────────────────────────────────────────────────────────────────────
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0d1117);
scene.fog = new THREE.Fog(0x0d1117, 8, 25);

const W = window.innerWidth, H = window.innerHeight;
const camera = new THREE.PerspectiveCamera(40, W / H, 0.01, 50);
const maxDim = Math.max(p.L, p.H, p.W);
camera.position.set(maxDim * 1.4, maxDim * 1.1, maxDim * 1.8);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(W, H);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.06;
controls.minDistance = 0.3;
controls.maxDistance = 20;

// ── Iluminação ──────────────────────────────────────────────────────────────
scene.add(new THREE.AmbientLight(0xffffff, 0.55));

const sun = new THREE.DirectionalLight(0xffffff, 0.9);
sun.position.set(4, 8, 5);
sun.castShadow = true;
scene.add(sun);

const fill = new THREE.DirectionalLight(0x4466aa, 0.35);
fill.position.set(-4, -4, -4);
scene.add(fill);

// ── Materiais ────────────────────────────────────────────────────────────────
const matTankFace = new THREE.MeshPhongMaterial({
  color: 0x445566, transparent: true, opacity: 0.07,
  side: THREE.DoubleSide, depthWrite: false
});
const matTankEdge = new THREE.LineBasicMaterial({ color: 0x4a8fa0, linewidth: 1.5 });
const matCore = new THREE.MeshPhongMaterial({ color: 0x778899, shininess: 40 });
const matBT   = new THREE.MeshPhongMaterial({
  color: 0x2a6eaf, transparent: true, opacity: 0.80, depthWrite: false, shininess: 60
});
const matAT   = new THREE.MeshPhongMaterial({
  color: 0xb03020, transparent: true, opacity: 0.88, depthWrite: false, shininess: 60
});
const matComut = new THREE.MeshPhongMaterial({
  color: 0x7e34ad, transparent: true, opacity: 0.85, depthWrite: false, shininess: 50
});
const matGrid  = new THREE.MeshBasicMaterial({ color: 0x1a2a3a });

// ── Helpers ──────────────────────────────────────────────────────────────────
function cylinder(r, h, mat, segs=40) {
  return new THREE.Mesh(new THREE.CylinderGeometry(r, r, h, segs), mat);
}

function boxWire(lx, ly, lz) {
  const geo = new THREE.BoxGeometry(lx, ly, lz);
  const face = new THREE.Mesh(geo, matTankFace);
  const edge = new THREE.LineSegments(new THREE.EdgesGeometry(geo), matTankEdge);
  face.add(edge);
  return face;
}

// ── Posições das fases ───────────────────────────────────────────────────────
function phasePositions() {
  if (p.n_fases === 1) return [0];
  const x0 = -p.L/2 + p.d_AT_tanque + p.r_AT;
  const x1 =  p.L/2 - p.d_AT_tanque - p.r_AT;
  const pos = [];
  for (let i = 0; i < p.n_fases; i++)
    pos.push(x0 + i * (x1 - x0) / (p.n_fases - 1));
  return pos;
}

// ── Construção da cena ───────────────────────────────────────────────────────
const yBottom = -p.H / 2;

// Tanque
scene.add(boxWire(p.L, p.H, p.W));

// Plano de fundo (piso do tanque — óleo)
const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(p.L - 0.01, p.W - 0.01),
  new THREE.MeshPhongMaterial({ color: 0x1a2d1a, transparent: true, opacity: 0.6 })
);
floor.rotation.x = -Math.PI / 2;
floor.position.y = yBottom + 0.001;
scene.add(floor);

// Grelha de referência abaixo do tanque
const gridSize = Math.ceil(Math.max(p.L, p.W) * 2 / 0.5) * 0.5;
const grid = new THREE.GridHelper(gridSize, Math.ceil(gridSize / 0.1), 0x1a3a2a, 0x152a1a);
grid.position.y = yBottom - 0.05;
scene.add(grid);

// Parte ativa por fase
const phases = phasePositions();
for (const px of phases) {
  const yPA = yBottom + p.d_fundo + p.H_PA / 2;

  // Núcleo
  const core = cylinder(p.r_nucleo, p.H_PA, matCore);
  core.position.set(px, yPA, 0);
  scene.add(core);

  // BT
  const bt = cylinder(p.r_BT, p.H_PA, matBT);
  bt.position.set(px, yPA, 0);
  scene.add(bt);

  // AT — canecos empilhados
  const hc = p.h_caneco;
  const dec = p.d_entre_canecos;
  for (let i = 0; i < p.n_canecos; i++) {
    const yc = yBottom + p.d_fundo + i * (hc + dec) + hc / 2;
    const caneco = cylinder(p.r_AT, hc, matAT);
    caneco.position.set(px, yc, 0);
    scene.add(caneco);
  }

  // Comutador
  if (p.tem_comutador) {
    const yComut = yBottom + p.d_fundo + p.H_PA + p.d_comut_AT + p.h_comutador / 2;
    const comut = cylinder(p.r_AT * 0.82, p.h_comutador, matComut);
    comut.position.set(px, yComut, 0);
    scene.add(comut);
  }
}

// ── Linhas de cota 3D ────────────────────────────────────────────────────────
function cotaLine(a, b, color=0xf0c040) {
  const geo = new THREE.BufferGeometry().setFromPoints([
    new THREE.Vector3(...a), new THREE.Vector3(...b)
  ]);
  return new THREE.Line(geo, new THREE.LineBasicMaterial({ color }));
}

function makeSprite(text, color='#f0c040') {
  const canvas = document.createElement('canvas');
  canvas.width = 256; canvas.height = 64;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = 'rgba(10,15,25,0.75)';
  ctx.fillRect(0, 0, 256, 64);
  ctx.font = 'bold 22px Consolas, monospace';
  ctx.fillStyle = color;
  ctx.textAlign = 'center';
  ctx.fillText(text, 128, 40);
  const tex = new THREE.CanvasTexture(canvas);
  const mat = new THREE.SpriteMaterial({ map: tex, depthTest: false });
  const spr = new THREE.Sprite(mat);
  spr.scale.set(0.45, 0.11, 1);
  return spr;
}

// d_AT_tanque (lateral esquerdo da primeira fase)
const px0 = phases[0];
const xEdgeAT = px0 - p.r_AT;
const xTankL  = -p.L / 2;
const yCota1  = yBottom + p.d_fundo + p.H_PA / 2;
scene.add(cotaLine([xTankL, yCota1, 0], [xEdgeAT, yCota1, 0]));
const spr1 = makeSprite(`d_AT_tank: ${(p.d_AT_tanque*1000).toFixed(0)}mm`);
spr1.position.set((xTankL + xEdgeAT)/2, yCota1 + 0.06, 0.01);
scene.add(spr1);

// d_fundo
const xCotaV = phases[phases.length-1] + p.r_AT + 0.12;
scene.add(cotaLine([xCotaV, yBottom, 0], [xCotaV, yBottom + p.d_fundo, 0]));
const spr2 = makeSprite(`d_fundo: ${(p.d_fundo*1000).toFixed(0)}mm`);
spr2.position.set(xCotaV + 0.28, yBottom + p.d_fundo/2, 0);
scene.add(spr2);

// d_topo
const yTopPA = yBottom + p.d_fundo + p.H_PA;
const yTopTank = p.H / 2;
scene.add(cotaLine([xCotaV, yTopPA, 0], [xCotaV, yTopTank, 0]));
const spr3 = makeSprite(`d_topo: ${(p.d_topo*1000).toFixed(0)}mm`);
spr3.position.set(xCotaV + 0.28, (yTopPA + yTopTank)/2, 0);
scene.add(spr3);

// ── Resize ───────────────────────────────────────────────────────────────────
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// ── Loop de renderização ─────────────────────────────────────────────────────
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();
</script>
</body>
</html>
"""
