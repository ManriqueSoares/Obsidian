# Dicionários em Python — Acesso e Adição

Contexto: usado em `acompanhamento_page.py` para associar dados (progresso, responsável, status) a cada área da lista `self.areas`.

---

## Estrutura usada no projeto

```python
self.dados_areas = {
    "GERAL":          {"progresso": 75, "responsavel": "Carlos Silva",   "status": "Em andamento"},
    "PARTE MECÂNICA": {"progresso": 90, "responsavel": "Ana Souza",      "status": "Concluído"},
    "PARTE ATIVA":    {"progresso": 40, "responsavel": "João Pereira",   "status": "Pendente"},
}
```

A chave do dicionário externo (`"GERAL"`, `"PARTE MECÂNICA"` etc.) é o mesmo valor que está na lista `self.areas`, o que permite acessar os dados pelo item do loop.

---

## Como acessar valores

### Acessar o dicionário interno completo de uma área
```python
dados = self.dados_areas["GERAL"]
# dados = {"progresso": 75, "responsavel": "Carlos Silva", "status": "Em andamento"}
```

### Acessar um campo específico diretamente
```python
progresso = self.dados_areas["GERAL"]["progresso"]  # 75
status    = self.dados_areas["GERAL"]["status"]      # "Em andamento"
```

### Acessar durante um loop pela lista self.areas
```python
for area in self.areas:
    dados      = self.dados_areas[area]
    progresso  = dados["progresso"]
    responsavel = dados["responsavel"]
    status     = dados["status"]
```

### Acessar com `.get()` (seguro — não lança erro se a chave não existir)
```python
progresso = self.dados_areas.get("GERAL", {}).get("progresso", 0)
# Se "GERAL" não existir, retorna 0 em vez de erro
```

---

## Como adicionar novos itens

### Adicionar uma nova área ao dicionário
```python
self.dados_areas["PINTURA"] = {"progresso": 55, "responsavel": "Fernanda Lima", "status": "Em andamento"}
```

> Lembrar também de adicionar `"PINTURA"` à lista `self.areas` para aparecer na tela.

### Atualizar um campo de uma área existente
```python
self.dados_areas["GERAL"]["progresso"] = 80
```

### Adicionar um novo campo a todas as áreas (ex: prioridade)
```python
for area in self.dados_areas:
    self.dados_areas[area]["prioridade"] = "Alta"
```

---

## Resumo rápido

| Operação | Sintaxe |
|---|---|
| Ler valor | `dicionario["chave"]` |
| Ler com segurança | `dicionario.get("chave", valor_padrão)` |
| Adicionar / sobrescrever | `dicionario["nova_chave"] = valor` |
| Atualizar campo interno | `dicionario["chave"]["campo"] = novo_valor` |
| Iterar chaves | `for chave in dicionario:` |
| Iterar pares | `for chave, valor in dicionario.items():` |
