---
tags: [dominio, enrolamentos, bobinas, AT, BT, tipos]
---

# Enrolamentos — Tipos e Geometria

Relacionado: [[canecos]] | [[parametros-mecanicos]] | [[nucleo]] | [[distancias-eletricas]]

---

## Arranjo Radial (Concêntrico)

O arranjo mais comum em transformadores de potência:

```
        ┌──────────────────────────────────────┐  ← Tanque
        │   d_AT_tanque                        │
        │     ┌────────────────────────┐       │
        │     │ AT  (enrol. externo)   │       │
        │     │   ┊d_AT_BT             │       │
        │     │    ┌──────────────┐   │       │
        │     │    │ BT (interno) │   │       │
        │     │    │  d_col_BT ┊  │   │       │
        │     │    │   ┌──────┐  │   │       │
        │     │    │   │Núcleo│  │   │       │
        │     │    │   └──────┘  │   │       │
        │     │    └──────────────┘   │       │
        │     └────────────────────────┘       │
        └──────────────────────────────────────┘
```

---

## Tipos de Bobina — AT

### Disco Contínuo (Continuous Disc)
- Espiras em discos horizontais empilhados axialmente
- Cada disco = um "caneco"
- Aplicação: AT de média e alta tensão
- Boa distribuição de impulso com interleaving
- **Interleaved disc**: espiras intercaladas entre discos adjacentes para melhorar distribuição de tensão sob impulso

### Hélice (Helical)
- Espiras em camadas helicoidais
- Típico para BT e AT de baixa tensão com alta corrente
- Canais de óleo axiais entre camadas (helical channels)

### Camada (Layer)
- Múltiplas camadas enroladas coaxialmente
- Comum em BT de transformadores de distribuição
- Separação por papel Kraft entre camadas

### Folha / Fita (Foil)
- Condutor em folha contínua
- Alta corrente / baixa tensão (BT, terciário)
- Construção compacta

---

## Tipos de Bobina — BT

| Tipo | Corrente | Tensão | Observação |
|---|---|---|---|
| Folha (foil) | Alta (> 1000 A) | Baixa | Compacta, fácil de enrolar |
| Hélice multifio | Alta | Baixa-média | CTC ou cabos em paralelo |
| Disco | Média | Média | Quando BT tem tensão elevada |

---

## Parâmetros Geométricos por Enrolamento

### Altura dos enrolamentos
- Idealmente `h_AT ≈ h_BT` (minimiza forças axiais de curto-circuito)
- Diferença de altura → força axial residual → requer pressagem adequada

### Relação de alturas e distâncias de topo/fundo
```
        ┌─────────────────────────┐
        │   d_topo_AT (ligação)   │  ← distância do topo do AT até a tampa
        ├─────────────────────────┤
        │                         │
        │     Enrolamento AT      │  h_AT
        │                         │
        ├─────────────────────────┤
        │   d_fundo_AT (ligação)  │  ← distância do fundo do AT até a base
        └─────────────────────────┘
```

As distâncias de topo e fundo são determinadas por:
1. Distância dielétrica da ponta do enrolamento (tensão máxima) → metal aterrado
2. Espaço para ligações (leads), terminais
3. Canais de óleo (resfriamento)

---

## Condutores

| Tipo | Descrição | Aplicação |
|---|---|---|
| Fio redondo esmaltado | Pequenas seções, múltiplos em paralelo | Distribuição |
| Retangular papel Kraft | Seção maior, simples ou paralelo | AT potência |
| CTC (Continuously Transposed Cable) | Múltiplos fios transpostos contínuos | AT alta corrente |
| Folha de alumínio/cobre | BT foil | BT alta corrente |

---

## Conexão de Saída (Leads / Ligações)

As ligações (leads) que saem dos enrolamentos e vão para:
- Buchas (bushings) na tampa ou lateral do tanque
- Comutador (tap leads AT)

**Distâncias das ligações**:
- Lead AT → tanque: função do BIL_AT
- Lead AT → lead AT (entre fases): função da tensão fase-fase + BIL
- Lead de neutro → tanque: função do BIL_neutro (pode ser bem menor se neutro aterrado)

> As ligações são frequentemente o elemento de maior dimensionamento crítico, pois são condutores em campo não uniforme (pior que eletrodo cilíndrico).

---

## Notas do usuário

> _Preencher com tipos de enrolamentos usados nos projetos, materiais de condutor e fornecedores_
