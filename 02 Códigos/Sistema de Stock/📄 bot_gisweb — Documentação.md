# bot_gisweb — Documentação

← [[Aproveitamento de Estoque]] | [[📄 analisar_cp_estoque — Documentação SAP]]

> **Arquivo:** `app/ui/services/bot/index.js`
> **Tecnologia:** Node.js + Puppeteer (Chromium/Edge)
> **Função:** Baixar automaticamente o relatório de estoque disponível do GISWEB

---

## O que é

Bot que automatiza o navegador Edge para entrar no sistema interno **GISWEB** da WEG e exportar a planilha de materiais disponíveis para aproveitamento (`reports.xlsx`).

Substitui o arquivo Excel local `ESTOQUE MEC.xlsx` que era usado nas macros VBA.

---

## Como funciona

```
1. Conecta ao Edge já aberto na porta de debug 9222
2. Navega para: https://gisweb-stock.weg.net/stockReuse/availableMaterials
3. Se a página de login aparecer → clica "Entrar"
4. Clica no botão "Exportar Materiais"
5. O arquivo reports.xlsx é baixado na pasta Downloads do usuário
```

### Porta de debug do Edge

O bot se conecta a uma instância do Edge já rodando com depuração remota habilitada, evitando precisar lidar com login SSO manualmente.

---

## Como é chamado pelo Python

```python
# Em analisar_cp_estoque.py
resultado = subprocess.run(
    ["node", "index.js"],
    cwd=_BOT_DIR,        # pasta app/ui/services/bot/
    capture_output=True,
    text=True,
)
```

- `node` deve estar no PATH do sistema
- O bot roda de forma síncrona — o Python aguarda a conclusão
- Após o bot terminar, o Python aguarda até 60s para o arquivo aparecer em disco

---

## Arquivo gerado

| Campo | Valor |
|-------|-------|
| Nome do arquivo | `reports.xlsx` |
| Pasta | `C:\Users\{usuario}\Downloads\` |
| Sobreescrita | O arquivo anterior é removido antes de rodar o bot |

---

## Colunas do reports.xlsx usadas

| Coluna | Uso no código |
|--------|---------------|
| `Material` | Chave para cruzamento com a BOM (CS12) |
| `Valor Unitário` | Preço unitário do componente |
| `Centro` | Centro do armazém MEC |
| `Área` | Filtro de área (MECANICA, PARTE ATIVA, etc.) |

Outras colunas presentes no arquivo (não utilizadas no momento):

`Tipo`, `Descrição Material`, `Estoque Livre`, `Unidade`, `Valor Total`, `Tipo Material`, `Dias Parados`, `Saldo SAP (RPA)`, `Alterado Por`, `Data Alteração`, `Comentário Coordenador`, `Data Atualização (RPA)`

---

## Pré-requisitos

- Node.js instalado e no PATH
- Edge aberto com porta de debug 9222
- Acesso à rede interna WEG (VPN ou rede local)
- Usuário já logado no GISWEB via SSO

---

## Possíveis falhas

| Falha | Causa provável |
|-------|----------------|
| `Bot falhou (código != 0)` | Node não instalado, Edge não aberto na porta 9222, sem acesso à rede |
| `reports.xlsx não apareceu após execução` | Download falhou no GISWEB, permissão de pasta, ou timeout |
| Arquivo com dados antigos | Arquivo anterior não foi removido (verificar permissão) |
