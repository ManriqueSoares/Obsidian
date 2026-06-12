---
tags: [dominio, resfriamento, cooling, ONAN, ONAF, OFAF, termico]
---

# Resfriamento

Relacionado: [[parametros-mecanicos]] | [[canecos]] | [[enrolamentos]]

---

## Códigos de Resfriamento (IEC 60076-2)

Formato: `[meio interno][circulação interna][meio externo][circulação externa]`

| Código | Descrição |
|---|---|
| **ONAN** | Oil Natural / Air Natural — convecção natural em óleo e ar |
| **ONAF** | Oil Natural / Air Forced — convecção natural em óleo, ventiladores externos |
| **OFAF** | Oil Forced / Air Forced — bomba de óleo + ventiladores |
| **ODAF** | Oil Directed / Air Forced — óleo direcionado nos canais dos enrolamentos |
| **ONAN/ONAF** | Dupla classificação (potência ONAN + potência ONAF) |
| **OFWF** | Oil Forced / Water Forced — trocador de calor água-óleo |

---

## Impacto no Projeto dos Canecos

O tipo de resfriamento define os requisitos dos canais de óleo entre canecos:

| Resfriamento | d_entre_canecos mínimo (térmico) |
|---|---|
| ONAN | 4–6 mm (convecção natural — canal suficientemente alto) |
| ONAF | 4–6 mm |
| OFAF | 3–5 mm (fluxo forçado — menor canal pode ser suficiente) |
| ODAF | 2–4 mm (óleo direcionado — maior pressão disponível) |

> O critério dielétrico pode superar o térmico para tensões altas — usar sempre o máximo.

---

## Canais de Óleo

### Canais axiais (entre canecos)
- Mantidos por espaçadores (key spacers) de pressboard
- Fluxo vertical por convecção (ONAN) ou forçado

### Canais radiais (entre enrolamentos)
- Entre BT e AT: cilindro isolante com canais radiais
- Manutenção por espaçadores radiais

### Circulação no tanque
- Óleo sobe pelos enrolamentos (quente) → sobe ao radiador → resfria → desce pelas laterais do tanque
- Para ODAF: dutos direcionam o fluxo

---

## Temperatura — Limites IEC 60076-2

| Grandeza | Limite (IEC) |
|---|---|
| Temperatura ambiente máxima | 40°C |
| Elevação média do óleo | ≤ 60 K (ONAN/ONAF) |
| Elevação do ponto mais quente (hot spot) | ≤ 78 K |
| Temperatura máxima do ponto mais quente | 118°C (40 + 78) |
| Fator de ponto quente `H` | 1,1–1,3 |

---

## Notas do usuário

> _Preencher com tipos de resfriamento típicos dos projetos, critérios de uprating, faixas de temperatura ambiente do local de instalação_
