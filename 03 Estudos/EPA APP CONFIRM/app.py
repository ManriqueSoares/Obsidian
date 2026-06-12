import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# ─── Paleta de cores ────────────────────────────────────────────────────────
COR = {
    "tanque":     "#4a4a4a",
    "oleo":       "#f5e6c8",
    "nucleo":     "#7f7f7f",
    "bobina_BT":  "#3a7ebf",
    "bobina_AT":  "#c0392b",
    "comutador":  "#8e44ad",
    "cota":       "#2c3e50",
    "fundo_app":  "#f0f0f0",
}

ESPESSURA_TANQUE = 0.05  # m (representação visual)


# ─── Helpers de desenho ──────────────────────────────────────────────────────

def _cota_horizontal(ax, x1, x2, y, valor, unidade="mm", cor=COR["cota"]):
    """Desenha cota horizontal com setas duplas e rótulo."""
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="<->", color=cor, lw=1.2))
    meio = (x1 + x2) / 2
    ax.text(meio, y, f" {valor:.0f} {unidade}", va="bottom", ha="center",
            fontsize=7, color=cor)


def _cota_vertical(ax, x, y1, y2, valor, unidade="mm", cor=COR["cota"]):
    """Desenha cota vertical com setas duplas e rótulo."""
    ax.annotate("", xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle="<->", color=cor, lw=1.2))
    meio = (y1 + y2) / 2
    ax.text(x, meio, f" {valor:.0f} {unidade}", va="center", ha="left",
            fontsize=7, color=cor)


def _retangulo(ax, x, y, w, h, cor_face, cor_borda="black", alpha=1.0, lw=1.5, label=None):
    r = patches.Rectangle((x, y), w, h, linewidth=lw,
                           edgecolor=cor_borda, facecolor=cor_face, alpha=alpha, label=label)
    ax.add_patch(r)
    return r


# ─── Conversão de unidades ──────────────────────────────────────────────────

def mm(v):
    """mm → m para plotagem."""
    return v / 1000.0


# ─── Vistas ─────────────────────────────────────────────────────────────────

def vista_corte_frontal(ax, p):
    """Corte vertical longitudinal (Y-Z): tanque, parte ativa, comutador, cotas."""
    ax.set_title("Corte Frontal", fontsize=9, fontweight="bold")
    ax.set_aspect("equal")
    ax.set_facecolor(COR["oleo"])

    L   = mm(p["tanque_comprimento"])
    H   = mm(p["tanque_altura"])
    e   = ESPESSURA_TANQUE
    n_f = p["n_fases"]

    # Tanque (contorno)
    _retangulo(ax, 0, 0, L, H, "none", COR["tanque"], lw=3)

    # Para simplificação, desenha fase central (ou única)
    d_lat   = mm(p["d_AT_tanque"])
    d_fundo = mm(p["d_fundo"])
    d_topo  = mm(p["d_topo"])
    h_PA    = mm(p["altura_PA"])
    d_AT    = mm(p["diametro_AT_ext"])

    # Largura disponível por fase
    largura_fase = L / n_f
    # Posição da fase central
    x_centro = L / 2

    # Núcleo (simplificado como retângulo cinza)
    d_nucleo = mm(p["diametro_nucleo"])
    x_nucleo = x_centro - d_nucleo / 2
    y_nucleo = d_fundo
    _retangulo(ax, x_nucleo, y_nucleo, d_nucleo, h_PA,
               COR["nucleo"], alpha=0.9, label="Núcleo")

    # Enrolamento AT (anel ao redor do núcleo — vista de corte)
    folga_AT_BT = mm(p["folga_AT_BT"])
    d_BT = mm(p["diametro_BT_ext"])
    x_AT_esq = x_centro - d_AT / 2
    x_AT_dir = x_centro + d_AT / 2 - mm(15)
    for x_b in [x_AT_esq, x_AT_dir]:
        _retangulo(ax, x_b, y_nucleo, mm(15), h_PA,
                   COR["bobina_AT"], alpha=0.85)
    # Enrolamento BT
    x_BT_esq = x_centro - d_BT / 2
    x_BT_dir = x_centro + d_BT / 2 - mm(10)
    for x_b in [x_BT_esq, x_BT_dir]:
        _retangulo(ax, x_b, y_nucleo, mm(10), h_PA,
                   COR["bobina_BT"], alpha=0.85)

    # Comutador
    if p["tem_comutador"]:
        h_comut = mm(p["altura_comutador"])
        d_c_AT  = mm(p["d_comut_AT"])
        d_c_tk  = mm(p["d_comut_tanque"])
        y_comut = d_fundo + h_PA + d_c_AT
        w_comut = d_AT + 2 * mm(20)
        _retangulo(ax, x_centro - w_comut / 2, y_comut, w_comut, h_comut,
                   COR["comutador"], alpha=0.75, label="Comutador")
        ax.text(x_centro, y_comut + h_comut / 2, "COMUT.", ha="center",
                va="center", fontsize=6, color="white", fontweight="bold")
        # Cota d_comut_AT
        _cota_vertical(ax, x_centro - w_comut / 2 - 0.04,
                       d_fundo + h_PA, y_comut,
                       p["d_comut_AT"])
        # Cota d_comut_tanque (topo)
        y_topo_comut = y_comut + h_comut
        _cota_vertical(ax, x_centro + w_comut / 2 + 0.04,
                       y_topo_comut, H,
                       p["d_comut_tanque"])

    # ── Cotas principais ──
    # d_fundo
    _cota_vertical(ax, -0.06, 0, d_fundo, p["d_fundo"])
    ax.text(-0.09, d_fundo / 2, "d_fundo", ha="center", va="center",
            fontsize=6, color=COR["cota"], rotation=90)

    # d_topo
    y_topo_PA = d_fundo + h_PA
    _cota_vertical(ax, -0.06, y_topo_PA, H, p["d_topo"])
    ax.text(-0.09, y_topo_PA + mm(p["d_topo"]) / 2, "d_topo",
            ha="center", va="center", fontsize=6, color=COR["cota"], rotation=90)

    # d_AT_tanque (lateral esquerda)
    x_PA_esq = x_centro - d_AT / 2
    _cota_horizontal(ax, 0, x_PA_esq, d_fundo / 2, p["d_AT_tanque"])
    ax.text(x_PA_esq / 2, d_fundo / 2 - 0.03, "d_AT_tanque",
            ha="center", va="top", fontsize=6, color=COR["cota"])

    # Altura da parte ativa
    _cota_vertical(ax, L + 0.05, d_fundo, d_fundo + h_PA, p["altura_PA"])
    ax.text(L + 0.08, d_fundo + h_PA / 2, "H_PA",
            ha="left", va="center", fontsize=6, color=COR["cota"], rotation=90)

    # Altura do tanque
    _cota_vertical(ax, L + 0.12, 0, H, p["tanque_altura"])
    ax.text(L + 0.15, H / 2, "H_tanque",
            ha="left", va="center", fontsize=6, color=COR["cota"], rotation=90)

    ax.set_xlim(-0.18, L + 0.2)
    ax.set_ylim(-0.1, H + 0.1)
    ax.axis("off")

    # Legenda
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COR["nucleo"], label="Núcleo"),
        Patch(facecolor=COR["bobina_BT"], label="Enrol. BT"),
        Patch(facecolor=COR["bobina_AT"], label="Enrol. AT"),
    ]
    if p["tem_comutador"]:
        legend_elements.append(Patch(facecolor=COR["comutador"], label="Comutador"))
    ax.legend(handles=legend_elements, loc="upper right", fontsize=6)


def vista_superior(ax, p):
    """Vista superior (X-Y): disposição das fases, d_entre_fases, d_AT_tanque."""
    ax.set_title("Vista Superior — Corte Horizontal", fontsize=9, fontweight="bold")
    ax.set_aspect("equal")
    ax.set_facecolor(COR["oleo"])

    L   = mm(p["tanque_comprimento"])
    W   = mm(p["tanque_largura"])
    n_f = p["n_fases"]
    d_AT = mm(p["diametro_AT_ext"])
    d_ef = mm(p["d_entre_fases"])

    # Contorno do tanque
    _retangulo(ax, 0, 0, L, W, "none", COR["tanque"], lw=3)

    # Posição das fases ao longo do comprimento
    if n_f == 1:
        centros_x = [L / 2]
    else:
        espacamento = (L - 2 * mm(p["d_AT_tanque"]) - n_f * d_AT) / (n_f - 1) + d_AT
        x0 = mm(p["d_AT_tanque"]) + d_AT / 2
        centros_x = [x0 + i * espacamento for i in range(n_f)]

    y_centro = W / 2
    rotulos = ["Fase A", "Fase B", "Fase C"][:n_f]

    for i, cx in enumerate(centros_x):
        # AT (círculo externo)
        circ_AT = plt.Circle((cx, y_centro), d_AT / 2,
                             color=COR["bobina_AT"], alpha=0.7)
        ax.add_patch(circ_AT)
        # BT
        d_BT = mm(p["diametro_BT_ext"])
        circ_BT = plt.Circle((cx, y_centro), d_BT / 2,
                              color=COR["bobina_BT"], alpha=0.8)
        ax.add_patch(circ_BT)
        # Núcleo
        d_n = mm(p["diametro_nucleo"])
        circ_n = plt.Circle((cx, y_centro), d_n / 2,
                             color=COR["nucleo"], alpha=0.9)
        ax.add_patch(circ_n)
        ax.text(cx, y_centro, rotulos[i], ha="center", va="center",
                fontsize=7, fontweight="bold", color="white")

    # Cota d_AT_tanque (lateral)
    _cota_horizontal(ax, 0, centros_x[0] - d_AT / 2, -0.05, p["d_AT_tanque"])
    ax.text((centros_x[0] - d_AT / 2) / 2, -0.08, "d_AT_tanque",
            ha="center", va="top", fontsize=6, color=COR["cota"])

    # Cota d_entre_fases
    if n_f > 1:
        for i in range(n_f - 1):
            x1 = centros_x[i] + d_AT / 2
            x2 = centros_x[i + 1] - d_AT / 2
            _cota_horizontal(ax, x1, x2, W + 0.05, p["d_entre_fases"])
        ax.text(L / 2, W + 0.09, "d_entre_fases",
                ha="center", va="bottom", fontsize=6, color=COR["cota"])

    # Cota largura do tanque
    _cota_vertical(ax, L + 0.06, 0, W, p["tanque_largura"])
    ax.text(L + 0.10, W / 2, "L_tanque",
            ha="left", va="center", fontsize=6, color=COR["cota"], rotation=90)

    ax.set_xlim(-0.15, L + 0.18)
    ax.set_ylim(-0.18, W + 0.18)
    ax.axis("off")


def vista_canecos(ax, p):
    """Detalhe vertical de uma fase: canecos do enrolamento AT com distâncias."""
    ax.set_title("Detalhe — Canecos (Enrol. AT)", fontsize=9, fontweight="bold")
    ax.set_facecolor("#fafafa")

    n_c   = p["n_canecos"]
    h_c   = mm(p["h_caneco"])
    d_ec  = mm(p["d_entre_canecos"])
    d_AT  = mm(p["diametro_AT_ext"])
    d_BT  = mm(p["diametro_BT_ext"])

    altura_total = n_c * h_c + (n_c - 1) * d_ec
    y_ini = 0

    for i in range(n_c):
        y = y_ini + i * (h_c + d_ec)
        _retangulo(ax, 0, y, d_AT / 2 - d_BT / 2, h_c,
                   COR["bobina_AT"], alpha=0.85)
        ax.text((d_AT / 2 - d_BT / 2) / 2, y + h_c / 2,
                f"C{i+1}", ha="center", va="center", fontsize=7, color="white")

        # Cota d_entre_canecos
        if i < n_c - 1:
            y_gap = y + h_c
            _cota_vertical(ax, d_AT / 2 - d_BT / 2 + 0.015,
                           y_gap, y_gap + d_ec, p["d_entre_canecos"])

    # Cota altura caneco
    _cota_vertical(ax, -0.015, 0, h_c, p["h_caneco"])
    ax.text(-0.035, h_c / 2, "h_caneco",
            ha="center", va="center", fontsize=6, color=COR["cota"], rotation=90)

    # Dimensão radial
    _cota_horizontal(ax, 0, d_AT / 2 - d_BT / 2, -0.02,
                     p["diametro_AT_ext"] / 2 - p["diametro_BT_ext"] / 2)

    ax.set_xlim(-0.06, d_AT / 2 - d_BT / 2 + 0.08)
    ax.set_ylim(-0.05, altura_total + 0.05)
    ax.set_aspect("equal")
    ax.axis("off")


def vista_comutador(ax, p):
    """Detalhe do comutador: posição, distâncias para AT e tanque."""
    ax.set_title("Detalhe — Comutador", fontsize=9, fontweight="bold")
    ax.set_facecolor("#fafafa")

    if not p["tem_comutador"]:
        ax.text(0.5, 0.5, "Sem comutador\nconfigurado",
                ha="center", va="center", fontsize=10, color="gray",
                transform=ax.transAxes)
        ax.axis("off")
        return

    h_PA    = mm(p["altura_PA"])
    h_comut = mm(p["altura_comutador"])
    d_c_AT  = mm(p["d_comut_AT"])
    d_c_tk  = mm(p["d_comut_tanque"])
    d_AT    = mm(p["diametro_AT_ext"])
    d_fundo = mm(p["d_fundo"])
    H_tanque = h_PA + d_fundo + d_c_AT + h_comut + d_c_tk

    w = d_AT * 1.5
    x0 = 0

    # Tanque
    _retangulo(ax, x0 - 0.03, 0, w + 0.06, H_tanque, "none", COR["tanque"], lw=3)
    ax.set_facecolor(COR["oleo"])

    # Parte ativa (AT)
    _retangulo(ax, x0, d_fundo, d_AT, h_PA, COR["bobina_AT"], alpha=0.7, label="AT")

    # Comutador
    y_comut = d_fundo + h_PA + d_c_AT
    _retangulo(ax, x0 + 0.01, y_comut, d_AT - 0.02, h_comut,
               COR["comutador"], alpha=0.8, label="Comutador")
    ax.text(x0 + d_AT / 2, y_comut + h_comut / 2, "COMUT.",
            ha="center", va="center", fontsize=7, color="white", fontweight="bold")

    # Cota d_comut_AT
    _cota_vertical(ax, x0 + d_AT + 0.015,
                   d_fundo + h_PA, y_comut, p["d_comut_AT"])
    ax.text(x0 + d_AT + 0.05, d_fundo + h_PA + d_c_AT / 2, "d_comut_AT",
            ha="left", va="center", fontsize=6, color=COR["cota"], rotation=90)

    # Cota d_comut_tanque (topo)
    y_fim_comut = y_comut + h_comut
    _cota_vertical(ax, x0 + d_AT + 0.015,
                   y_fim_comut, H_tanque, p["d_comut_tanque"])
    ax.text(x0 + d_AT + 0.05, y_fim_comut + d_c_tk / 2, "d_comut_tanque",
            ha="left", va="center", fontsize=6, color=COR["cota"], rotation=90)

    ax.set_xlim(x0 - 0.12, x0 + d_AT + 0.18)
    ax.set_ylim(-0.05, H_tanque + 0.08)
    ax.set_aspect("equal")
    ax.axis("off")


# ─── Geração das vistas ──────────────────────────────────────────────────────

def gerar_visualizacao(p, frame_canvas):
    """Cria a figura com 4 subplots e embute no frame tkinter."""
    for widget in frame_canvas.winfo_children():
        widget.destroy()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Esboço de Distâncias Elétricas — Transformador",
                 fontsize=12, fontweight="bold", y=0.98)
    fig.patch.set_facecolor(COR["fundo_app"])

    vista_corte_frontal(axes[0][0], p)
    vista_superior(axes[0][1], p)
    vista_canecos(axes[1][0], p)
    vista_comutador(axes[1][1], p)

    plt.tight_layout(rect=[0, 0, 1, 0.97])

    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    plt.close(fig)


# ─── Interface de entrada ────────────────────────────────────────────────────

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EPA — Distâncias Elétricas em Transformadores  v0.1")
        self.geometry("1280x820")
        self.configure(bg=COR["fundo_app"])
        self._build_ui()

    def _build_ui(self):
        # Painel esquerdo: entradas
        frame_esq = ttk.Frame(self, width=340)
        frame_esq.pack(side="left", fill="y", padx=8, pady=8)
        frame_esq.pack_propagate(False)

        # Scroll nas entradas
        canvas_scroll = tk.Canvas(frame_esq, bg=COR["fundo_app"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_esq, orient="vertical",
                                  command=canvas_scroll.yview)
        canvas_scroll.configure(yscrollcommand=scrollbar.set)
        # Botão empacotado ANTES do scroll para reservar espaço na base
        ttk.Button(frame_esq, text="▶  Gerar Visualização",
                   command=self._gerar).pack(side="bottom", pady=10, fill="x", padx=4)

        scrollbar.pack(side="right", fill="y")
        canvas_scroll.pack(side="left", fill="both", expand=True)

        self.frame_entradas = ttk.Frame(canvas_scroll)
        win_id = canvas_scroll.create_window((0, 0), window=self.frame_entradas,
                                             anchor="nw")
        self.frame_entradas.bind("<Configure>",
            lambda e: canvas_scroll.configure(
                scrollregion=canvas_scroll.bbox("all")))
        canvas_scroll.bind("<Configure>",
            lambda e: canvas_scroll.itemconfig(win_id, width=e.width))

        self.vars = {}
        self._build_secoes()

        # Painel direito: canvas matplotlib
        self.frame_canvas = ttk.Frame(self)
        self.frame_canvas.pack(side="right", fill="both", expand=True,
                               padx=4, pady=8)

    def _secao(self, titulo):
        lf = ttk.LabelFrame(self.frame_entradas, text=titulo, padding=6)
        lf.pack(fill="x", padx=4, pady=4)
        return lf

    def _campo(self, frame, label, chave, default, unidade="mm"):
        row = ttk.Frame(frame)
        row.pack(fill="x", pady=1)
        ttk.Label(row, text=label, width=22, anchor="w").pack(side="left")
        var = tk.DoubleVar(value=default)
        self.vars[chave] = var
        ttk.Entry(row, textvariable=var, width=8).pack(side="left")
        ttk.Label(row, text=unidade, foreground="gray").pack(side="left", padx=2)

    def _check(self, frame, label, chave, default=True):
        var = tk.BooleanVar(value=default)
        self.vars[chave] = var
        ttk.Checkbutton(frame, text=label, variable=var).pack(anchor="w")

    def _combo(self, frame, label, chave, opcoes, default):
        row = ttk.Frame(frame)
        row.pack(fill="x", pady=1)
        ttk.Label(row, text=label, width=22, anchor="w").pack(side="left")
        var = tk.IntVar(value=default)
        self.vars[chave] = var
        cb = ttk.Combobox(row, textvariable=var, values=opcoes, width=6,
                          state="readonly")
        cb.current(opcoes.index(default))
        cb.bind("<<ComboboxSelected>>", lambda e: var.set(int(cb.get())))
        cb.pack(side="left")

    def _build_secoes(self):
        # ── Tanque ──
        s = self._secao("Tanque")
        self._campo(s, "Comprimento interno", "tanque_comprimento", 1800)
        self._campo(s, "Largura interna",     "tanque_largura",     900)
        self._campo(s, "Altura interna",      "tanque_altura",      2200)
        self._combo(s, "Número de fases",     "n_fases", [1, 3], 3)

        # ── Parte Ativa ──
        s = self._secao("Parte Ativa")
        self._campo(s, "Altura da PA",          "altura_PA",          1500)
        self._campo(s, "Diâm. ext. AT",         "diametro_AT_ext",    500)
        self._campo(s, "Diâm. ext. BT",         "diametro_BT_ext",    380)
        self._campo(s, "Diâm. núcleo",          "diametro_nucleo",    200)
        self._campo(s, "Folga AT-BT (cil.)",    "folga_AT_BT",         40)
        self._campo(s, "d_AT_tanque (lateral)", "d_AT_tanque",        120)
        self._campo(s, "d_fundo",               "d_fundo",            180)
        self._campo(s, "d_topo (sem comut.)",   "d_topo",             200)
        self._campo(s, "d_entre_fases",         "d_entre_fases",       80)

        # ── Canecos ──
        s = self._secao("Canecos (Enrol. AT)")
        self._campo(s, "Número de canecos",    "n_canecos",    8, "")
        self._campo(s, "Altura do caneco",     "h_caneco",    80)
        self._campo(s, "Dist. entre canecos",  "d_entre_canecos", 25)

        # ── Comutador ──
        s = self._secao("Comutador")
        self._check(s, "Possui comutador", "tem_comutador", True)
        self._campo(s, "Altura do comutador",   "altura_comutador",  350)
        self._campo(s, "d_comut_AT",            "d_comut_AT",         60)
        self._campo(s, "d_comut_tanque",        "d_comut_tanque",    120)

    def _coletar(self):
        p = {}
        for chave, var in self.vars.items():
            p[chave] = var.get()
        p["n_canecos"] = int(p["n_canecos"])
        p["n_fases"]   = int(p["n_fases"])
        p["tem_comutador"] = bool(p["tem_comutador"])
        return p

    def _gerar(self):
        try:
            p = self._coletar()
            gerar_visualizacao(p, self.frame_canvas)
        except Exception as exc:
            messagebox.showerror("Erro", str(exc))


# ─── Entry point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = App()
    app.mainloop()
