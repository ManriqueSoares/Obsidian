# CLAUDE.md — Vault Notas Manrique

Este arquivo documenta a estrutura e o contexto do vault Obsidian do Manrique para uso do Claude Code.

---

## Sobre o usuário

- **Nome:** Manrique
- **Empresa:** WEG EQUIPAMENTOS ELÉTRICOS S.A
- **Área:** GCV (Grupo de Cálculo Vetorial ou similar)
- **Perfil técnico:** Engenharia elétrica + desenvolvimento de software/automação
- **Stack principal:** Python, VBA, PowerShell, SQL (PostgreSQL, MySQL), Power BI

---

## Estrutura do Vault

```
Notas Manrique/
├── CLAUDE.md              ← este arquivo
├── 00 Notas/              ← notas gerais e diário
│   ├── Notas GERAIS 📓.md ← hub principal: tarefas globais e links para o diário
│   └── Calendário/        ← notas diárias (formato DD-MM-YYYY.md)
├── 01 Projetos/           ← projetos de engenharia
│   ├── EPA/               ← Estudos de Parte Ativa (IDs numéricos ex: EPA - 19192378.md)
│   ├── Aterramentos/      ← estudos de aterramento (norma WPR-7583)
│   ├── Buchas/            ← especificações de buchas de transformadores
│   └── Comutadores/       ← especificações de comutadores sob carga
├── 02 Códigos/            ← notas técnicas de código e desenvolvimento
│   ├── Ambiente de Projeto EPA/   ← diagramas Excalidraw do ambiente EPA
│   ├── Etiquetas COD/             ← VBA para geração de etiquetas (Excel)
│   ├── PLANILHAS PS/              ← PowerShell para planilhas PA
│   ├── Rapha/                     ← adaptação do VBA de colega (QM/Claim) para GCV
│   └── Sistema de Stock/          ← sistema Python + PostgreSQL de aproveitamento de estoque
├── 03 Estudos/            ← materiais de estudo
│   └── EPA/               ← estudos técnicos de parte ativa
├── 04 Claude/             ← conversas e snippets salvos com o Claude
│   ├── Conversas/         ← histórico de conversas relevantes
│   └── Snippets/          ← trechos de código gerados/revisados pelo Claude
└── BD Docs/               ← banco de PDFs e imagens usadas como anexos nas notas
```

---

## Projetos ativos (contexto)

### Sistema de Stock (Python + PostgreSQL)
- Sistema de aproveitamento de estoque WEG, deploy no Railway
- Banco PostgreSQL com tabelas `ESTOQUE_GERAL` e `ENVIO PILARES`
- Possui sistema de cadastro de centros (responsável, chefia, pilares), e-mail de confirmação e notificação
- Código-fonte: `C:\Users\manriquef\Documents\Projeto Stock`
- Notas: `02 Códigos/Sistema de Stock/`

### EPA — Estudos de Parte Ativa
- Cada projeto tem um ID numérico (ex: `19192378`) que vira uma nota em `01 Projetos/EPA/`
- Cada nota EPA registra: documento de referência, configuração, aterramento, acessórios (buchas AT/BT, comutador)
- Lista mestra de estudos para revisar: `01 Projetos/EPA/BD Estudos PA.md`
- Especificações de componentes ficam em `01 Projetos/Buchas/` e `01 Projetos/Comutadores/`

### Etiquetas (VBA Excel)
- Macro para geração de etiquetas de peças/componentes
- Módulos: `Modulo ETIQUETAS`, `Modulo criar etiquetas`
- Notas: `02 Códigos/Etiquetas COD/`

### VBA Rapha — Sistema QM/Claim
- Adaptação de código VBA de colega (Rapha) para funcionar no GCV
- Arquivos principais: `AbrircaminhoQMSeClaim.vba`, `SAP.vba`
- Código local: `C:\Users\manriquef\Documents\COD_RAPHA`
- Notas: `02 Códigos/Rapha/`

### Planilha PA (PowerShell)
- Scripts PowerShell para manipulação/automação da planilha de controle PA
- Notas: `02 Códigos/PLANILHAS PS/`

---

## Plugins instalados

| Plugin | Uso |
|--------|-----|
| Calendar | Notas diárias (Daily Notes) |
| Excalidraw | Diagramas e mapas visuais |
| Full Calendar | Visualização de calendário |
| Kanban | Quadros de tarefas |
| Local REST API | Integração externa com o vault |
| Mind Map | Mapas mentais |
| Icon Folder | Ícones nas pastas |
| PDF+ | Anotações em PDFs |
| Stopwatch | Controle de tempo |
| Style Settings | Personalização do tema |

**Temas disponíveis:** AnuPpuccin, Tokyo Night

---

## Convenções do vault

- **Notas diárias:** `00 Notas/Calendário/DD-MM-YYYY.md` (algumas em `YYYY-MM-DD.md`)
- **Projetos EPA:** `01 Projetos/EPA/EPA - [ID numérico].md`
- **Componentes:** nome técnico completo como título (ex: `BUCHA COND GOB 550kV 800A PORCEL SOLID.md`)
- **Anexos:** todos os PDFs e imagens vão para `BD Docs/`
- **Links internos:** usam sintaxe Obsidian `[[Nome da nota]]`

---

## Como usar este vault com o Claude

- Para **salvar uma conversa relevante**, criar nota em `04 Claude/Conversas/`
- Para **salvar código gerado**, criar nota em `04 Claude/Snippets/`
- Para **criar uma nota EPA**, seguir o padrão de `01 Projetos/EPA/EPA - [ID].md`
- Ao **mencionar um projeto**, referenciar o ID ou nome para eu buscar o contexto correto
- O **diário** fica em `00 Notas/Calendário/` — útil para registrar decisões do dia
