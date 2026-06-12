# EPA APP — Distâncias Elétricas em Transformadores

> Ferramenta para cálculo e visualização de distâncias elétricas em projetos de transformadores de potência.  
> Baseada em grandezas elétricas e mecânicas reais, normas IEC 60076 / ABNT NBR 5356.

---

## Mapa do Vault

### Domínio — Conceitos Técnicos

| Nota | Conteúdo |
|---|---|
| [[notas/dominio/parametros-eletricos]] | Sn, Un, Um, BIL, SIL, grupo de ligação, tap range |
| [[notas/dominio/parametros-mecanicos]] | Geometria geral: núcleo, enrolamentos, dimensões do tanque |
| [[notas/dominio/niveis-isolamento]] | Tabelas IEC 60076-3: Um → BIL / SIL / Uac |
| [[notas/dominio/distancias-eletricas]] | Definição e tabela de todas as distâncias do projeto |
| [[notas/dominio/nucleo]] | Tipos, escalonamento, indução, materiais |
| [[notas/dominio/enrolamentos]] | Tipos de bobina AT/BT, geometria, condutores, leads |
| [[notas/dominio/canecos]] | Definição, parâmetros, distribuição de impulso, tipos |
| [[notas/dominio/comutadores]] | DETC/OLTC, posicionamento, n° de comutadores, tensões |
| [[notas/dominio/resfriamento]] | Códigos ONAN/ONAF/OFAF/ODAF, impacto nos canais |
| [[notas/dominio/normas]] | IEC 60076, ABNT NBR 5356, IEC 60214, Cigré, ONS |
| [[notas/dominio/isolamento/isolamento-oleo]] | Rigidez dielétrica, sistemas de isolamento, efeito das barreiras |
| [[notas/dominio/isolamento/pressboard]] | Tipos, propriedades, cilindro isolante, espaçadores |

### Cálculos — Metodologia

| Nota | Conteúdo |
|---|---|
| [[notas/calculos/metodologia-distancias]] | Fluxo de cálculo completo por par de eletrodos |
| [[notas/calculos/tensoes-ensaio]] | LI, SI, ACSD, ACID, impulso cortado, distribuição de impulso |
| [[notas/calculos/formulario]] | Equações de referência rápida |

### App — Decisões de Projeto

| Nota | Conteúdo |
|---|---|
| [[notas/app/arquitetura]] | Stack, estrutura de arquivos, vistas geradas |
| [[notas/app/versoes]] | Changelog planejado (v0.1 → v1.0) |

### Código — Documentação Técnica dos Arquivos

| Nota | Arquivo | Conteúdo |
|---|---|---|
| [[notas/codigo/app-py]] | `app.py` | Paleta, helpers, 4 vistas matplotlib, classe App, dict `p`, limitações |
| [[notas/codigo/export-dxf-py]] | `export_dxf.py` | Layers DXF, estilo de cota EPA, geometria do corte/superior, limitações |
| [[notas/codigo/export-html3d-py]] | `export_html3d.py` | Template Three.js, geometria 3D, materiais, cotas 3D, OrbitControls |
| [[notas/codigo/ambiente]] | `.venv` / `run.bat` | Pacotes pinados, como recriar, como rodar |

### Sessões

| Nota | Conteúdo |
|---|---|
| [[notas/sessoes/2026-06-12]] | Início do projeto — decisões iniciais, escopo, perguntas em aberto |

---

## Fluxo de Dados do App (visão geral)

```
ENTRADAS (usuário)
    │
    ├─ Elétricos: Sn, Un_AT, Un_BT, Um_AT, BIL_AT, SIL_AT, Uac_AT
    │             grupo_ligacao, uk%, tap_range, n_posicoes
    │
    ├─ Mecânicos: tipo_nucleo, D_col, n_fases, tipo_enrol_AT, tipo_enrol_BT
    │             n_canecos, h_caneco, tipo_comutador, n_comutadores
    │
    └─ Resfriamento: tipo_cooling
            │
            ▼
    CÁLCULOS (norma + metodologia)
            │
            ├─ Um → BIL, SIL, Uac  (tabela IEC 60076-3)
            ├─ BIL → d_AT_tanque, d_fundo, d_topo
            ├─ BIL, distribuição de impulso → d_entre_canecos
            ├─ BIL_comut → d_comut_AT, d_comut_tanque
            ├─ BIL + fase-fase → d_entre_fases
            └─ D_col + n_canecos → dimensões do enrolamento
            │
            ▼
    SAÍDAS
            ├─ Tabela de distâncias calculadas
            ├─ Vista: Corte Frontal
            ├─ Vista: Superior
            ├─ Vista: Detalhe Canecos
            └─ Vista: Detalhe Comutador
```

---

## Status

| Componente | Estado |
|---|---|
| Vault de notas do domínio | ✅ Estrutura criada — preencher com dados do projeto |
| App v0.1 (entradas manuais + 4 vistas) | ✅ Funcional |
| App v0.2 (cálculo automático de distâncias) | 🔲 Planejado |
| App v1.0 (folha de cálculo completa + relatório) | 🔲 Planejado |

---

## Perguntas em Aberto

- [ ] Quais normas são referência primária? (IEC pura / ABNT / mistura?)
- [ ] Qual o tipo de enrolamento AT mais comum nos projetos? (disco contínuo / interleaved?)
- [ ] O transformador é sempre trifásico ou contempla monofásico?
- [ ] Existe terciário de estabilização?
- [ ] O neutro AT é sempre aterrado (graduado) ou pode ser isolado?
- [ ] Que tabelas de distância são usadas internamente (próprias da empresa ou da norma pura)?
- [ ] Há necessidade de blindagem eletrostática (electrostatic shield)?
