"""
Exportador DXF — Distâncias Elétricas do Transformador
Gera corte frontal + vista superior com cotas em formato DXF (abre em AutoCAD, FreeCAD, BricsCAD).
"""
import ezdxf
from ezdxf import colors
from ezdxf.enums import TextEntityAlignment


# ─── Helpers ────────────────────────────────────────────────────────────────

def _rect(msp, x, y, w, h, layer, lw=25):
    pts = [(x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)]
    msp.add_lwpolyline(pts, dxfattribs={"layer": layer, "lineweight": lw})


def _hatch_rect(msp, x, y, w, h, layer, aci_color):
    """Retângulo com hachura SOLID (preenchido)."""
    hatch = msp.add_hatch(color=aci_color, dxfattribs={"layer": layer})
    hatch.paths.add_polyline_path(
        [(x, y), (x+w, y), (x+w, y+h), (x, y+h)], is_closed=True
    )
    _rect(msp, x, y, w, h, layer, lw=15)


def _hdim(msp, x1, x2, y_pts, y_base, style):
    """Cota horizontal entre x1 e x2 (pontos medidos na altura y_pts, linha de cota em y_base)."""
    try:
        dim = msp.add_linear_dim(
            base=((x1 + x2) / 2, y_base),
            p1=(x1, y_pts), p2=(x2, y_pts),
            angle=0, dimstyle=style,
        )
        dim.render()
    except Exception:
        pass


def _vdim(msp, y1, y2, x_pts, x_base, style):
    """Cota vertical entre y1 e y2 (pontos medidos em x_pts, linha de cota em x_base)."""
    try:
        dim = msp.add_linear_dim(
            base=(x_base, (y1 + y2) / 2),
            p1=(x_pts, y1), p2=(x_pts, y2),
            angle=90, dimstyle=style,
        )
        dim.render()
    except Exception:
        pass


def _label(msp, text, x, y, height=30, layer="TEXTO"):
    msp.add_text(text, dxfattribs={"layer": layer, "height": height,
                                   "insert": (x, y)})


def _phase_centers(p):
    """Retorna lista de centros X de cada fase no corte frontal."""
    L = p["tanque_comprimento"]
    D_AT = p["diametro_AT_ext"]
    d_lat = p["d_AT_tanque"]
    n_f = int(p["n_fases"])
    if n_f == 1:
        return [L / 2]
    esp = (L - 2 * d_lat - n_f * D_AT) / (n_f - 1) + D_AT
    x0 = d_lat + D_AT / 2
    return [x0 + i * esp for i in range(n_f)]


# ─── Vista: Corte Frontal ────────────────────────────────────────────────────

def _desenhar_corte(msp, p, ox, oy, style):
    L   = p["tanque_comprimento"]
    H   = p["tanque_altura"]
    H_PA = p["altura_PA"]
    d_f  = p["d_fundo"]
    d_t  = p["d_topo"]
    d_lat = p["d_AT_tanque"]
    D_AT = p["diametro_AT_ext"]
    D_BT = p["diametro_BT_ext"]
    D_n  = p["diametro_nucleo"]

    # Tanque (contorno grosso)
    _rect(msp, ox, oy, L, H, "TANQUE", lw=50)

    centros_x = _phase_centers(p)

    for cx in centros_x:
        ax = ox + cx
        y0 = oy + d_f

        # Corte do núcleo (cinza preenchido)
        _hatch_rect(msp, ax - D_n/2, y0, D_n, H_PA, "NUCLEO", 8)

        # Corte do enrolamento BT (duas faixas verticais)
        bw = D_BT/2 - D_n/2
        _hatch_rect(msp, ax - D_BT/2, y0, bw, H_PA, "BT", 5)
        _hatch_rect(msp, ax + D_n/2,  y0, bw, H_PA, "BT", 5)

        # Corte do enrolamento AT (duas faixas externas)
        aw = D_AT/2 - D_BT/2
        _hatch_rect(msp, ax - D_AT/2, y0, aw, H_PA, "AT", 1)
        _hatch_rect(msp, ax + D_BT/2, y0, aw, H_PA, "AT", 1)

    # Comutador
    if p["tem_comutador"]:
        h_c = p["altura_comutador"]
        d_cAT = p["d_comut_AT"]
        for cx in centros_x:
            ax = ox + cx
            wc = D_AT + 40
            yc = oy + d_f + H_PA + d_cAT
            _hatch_rect(msp, ax - wc/2, yc, wc, h_c, "COMUTADOR", 6)
            _label(msp, "COMUT.", ax - 15, yc + h_c/2 - 10, height=20, layer="COMUTADOR")

    # ── Cotas ──
    m = 60   # margem das cotas
    m2 = 120

    # d_AT_tanque esquerdo (horizontal)
    first_cx = centros_x[0]
    _hdim(msp, ox, ox + first_cx - D_AT/2, oy + d_f/2, oy - m, style)
    _label(msp, "d_AT_tanque", ox + (first_cx - D_AT/2)/2 - 60, oy - m - 45, height=25)

    # Comprimento total do tanque
    _hdim(msp, ox, ox + L, oy, oy - m2, style)
    _label(msp, f"L_tanque = {L:.0f} mm", ox + L/2 - 120, oy - m2 - 45, height=25)

    # d_fundo (vertical esquerdo)
    _vdim(msp, oy, oy + d_f, ox, ox - m, style)
    _label(msp, "d_fundo", ox - m - 80, oy + d_f/2 - 10, height=25)

    # H_PA (vertical direito)
    _vdim(msp, oy + d_f, oy + d_f + H_PA, ox + L, ox + L + m, style)
    _label(msp, "H_PA", ox + L + m + 10, oy + d_f + H_PA/2 - 10, height=25)

    # d_topo (vertical esquerdo)
    _vdim(msp, oy + d_f + H_PA, oy + H, ox, ox - m, style)
    _label(msp, "d_topo" if not p["tem_comutador"] else "d_comut_topo",
           ox - m - 80, oy + d_f + H_PA + (d_t)/2 - 10, height=25)

    # H_tanque total (vertical, ainda mais à direita)
    _vdim(msp, oy, oy + H, ox + L, ox + L + m2, style)
    _label(msp, f"H_tanque = {H:.0f} mm", ox + L + m2 + 10, oy + H/2, height=25)

    # d_entre_fases (se trifásico)
    if len(centros_x) > 1:
        x1 = ox + centros_x[0] + D_AT/2
        x2 = ox + centros_x[1] - D_AT/2
        _hdim(msp, x1, x2, oy + d_f + H_PA, oy + H + m, style)
        _label(msp, "d_entre_fases", x1 + (x2-x1)/2 - 70, oy + H + m + 10, height=25)

    # Rótulo da vista
    _label(msp, "CORTE FRONTAL — VISTA A-A", ox + L/2 - 180, oy - m2 - 100, height=35, layer="TEXTO")


# ─── Vista: Superior ────────────────────────────────────────────────────────

def _desenhar_superior(msp, p, ox, oy, style):
    L   = p["tanque_comprimento"]
    W   = p["tanque_largura"]
    D_AT = p["diametro_AT_ext"]
    D_BT = p["diametro_BT_ext"]
    D_n  = p["diametro_nucleo"]
    d_lat = p["d_AT_tanque"]

    _rect(msp, ox, oy, L, W, "TANQUE", lw=50)

    centros_x = _phase_centers(p)
    cy = oy + W / 2

    for cx in centros_x:
        ax = ox + cx
        msp.add_circle((ax, cy), D_AT/2, dxfattribs={"layer": "AT", "lineweight": 30})
        msp.add_circle((ax, cy), D_BT/2, dxfattribs={"layer": "BT", "lineweight": 20})
        msp.add_circle((ax, cy), D_n/2,  dxfattribs={"layer": "NUCLEO", "lineweight": 20})

        # Linhas de centro
        ext = 30
        msp.add_line((ax - D_AT/2 - ext, cy), (ax + D_AT/2 + ext, cy),
                     dxfattribs={"layer": "TEXTO", "lineweight": 5, "linetype": "CENTER"})
        msp.add_line((ax, cy - D_AT/2 - ext), (ax, cy + D_AT/2 + ext),
                     dxfattribs={"layer": "TEXTO", "lineweight": 5, "linetype": "CENTER"})

    m = 60

    # d_AT_tanque lateral esquerdo
    first_cx = centros_x[0]
    _hdim(msp, ox, ox + first_cx - D_AT/2, oy, oy - m, style)
    _label(msp, "d_AT_tanque", ox + (first_cx - D_AT/2)/2 - 60, oy - m - 45, height=25)

    # L_tanque
    _hdim(msp, ox, ox + L, oy, oy - 2*m, style)

    # W_tanque
    _vdim(msp, oy, oy + W, ox + L, ox + L + m, style)
    _label(msp, f"W_tanque = {W:.0f} mm", ox + L + m + 10, oy + W/2, height=25)

    # d_AT_tanque superior
    _vdim(msp, cy + D_AT/2, oy + W, ox + first_cx, ox + first_cx + m, style)
    _label(msp, "d_AT_tan.", ox + first_cx + m + 10, cy + D_AT/2 + (oy + W - cy - D_AT/2)/2, height=22)

    # d_entre_fases
    if len(centros_x) > 1:
        x1 = ox + centros_x[0] + D_AT/2
        x2 = ox + centros_x[1] - D_AT/2
        _hdim(msp, x1, x2, oy + W, oy + W + m, style)
        _label(msp, "d_entre_fases", x1 + (x2-x1)/2 - 70, oy + W + m + 10, height=25)

    _label(msp, "VISTA SUPERIOR", ox + L/2 - 120, oy - 2*m - 80, height=35, layer="TEXTO")


# ─── Função principal ────────────────────────────────────────────────────────

def exportar_dxf(p: dict, filepath: str):
    doc = ezdxf.new("R2010")
    doc.header["$INSUNITS"] = 4  # mm

    # Carrega linetype CENTER
    doc.linetypes.add("CENTER", [0.4, 12, -4, 4, -4])

    # Camadas
    camadas = [
        ("TANQUE",    7),   # branco/preto
        ("AT",        1),   # vermelho
        ("BT",        5),   # azul
        ("NUCLEO",    8),   # cinza
        ("COMUTADOR", 6),   # magenta
        ("COTAS",     3),   # verde
        ("TEXTO",     2),   # amarelo
    ]
    for nome, cor in camadas:
        doc.layers.add(nome, dxfattribs={"color": cor})

    # Estilo de cota
    style = "EPA"
    ds = doc.dimstyles.new(style)
    ds.dxf.dimtxt  = 28
    ds.dxf.dimasz  = 20
    ds.dxf.dimexe  = 12
    ds.dxf.dimexo  = 8
    ds.dxf.dimdli  = 0
    ds.dxf.dimclrd = 3   # cor da linha = verde
    ds.dxf.dimclrt = 3
    ds.dxf.dimclre = 3
    ds.dxf.dimdec  = 0

    msp = doc.modelspace()

    L = p["tanque_comprimento"]

    # Corte frontal: origem (0, 0)
    _desenhar_corte(msp, p, 0, 0, style)

    # Vista superior: offset horizontal + 400 mm de separação
    offset_x = L + 400
    _desenhar_superior(msp, p, offset_x, 0, style)

    # Bloco de título simplificado
    H = p["tanque_altura"]
    _rect(msp, 0, H + 300, L * 2 + 400, 180, "TEXTO", lw=30)
    _label(msp, "EPA — DISTÂNCIAS ELÉTRICAS DO TRANSFORMADOR",
           80, H + 360, height=50, layer="TEXTO")
    _label(msp, f"Sn: {p.get('Sn_MVA', '—')} MVA  |  "
                f"Un_AT: {p.get('Un_AT_kV', '—')} kV  |  "
                f"Un_BT: {p.get('Un_BT_kV', '—')} kV  |  "
                f"Fases: {int(p['n_fases'])}",
           80, H + 310, height=28, layer="TEXTO")

    doc.saveas(filepath)
