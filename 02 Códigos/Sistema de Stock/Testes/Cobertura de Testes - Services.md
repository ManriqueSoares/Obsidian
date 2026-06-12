# Cobertura de Testes — app/ui/services

> Atualizado em: 2026-05-21
> Resultado da suite: **158 passed, 0 failed** (testes novos gerados para todas as funções sem cobertura)

---

## Correções feitas nesta sessão

### `tests/unit/test_add_chefia.py`
Três erros foram corrigidos:
1. Importava `listas_referencias` (inexistente) → corrigido para `listas_cadastro`
2. Usava `from app.ui.config.listas` → corrigido para `from config.listas` (conftest já adiciona `app/ui` no sys.path)
3. Handler é **síncrono** mas o teste usava `asyncio.run()` e `FakePage.update_async` → corrigido para chamada direta e `FakePage.update()`

### `tests/unit/test_analisar_cp_estoque.py` — `TestBaixarEstoqueMec::test_retorna_dataframe_quando_bot_bem_sucedido`
O teste mockava `_aguarda_arquivo` mas a função real chama `_aguarda_arquivo_reports` (função diferente). Corrigido para mockar `_aguarda_arquivo_reports`.

---

## Novos arquivos de teste criados

| Arquivo | Funções testadas |
|---|---|
| `tests/unit/test_atualiza_bd.py` | `_to_num`, `_to_str`, `_adiciona_linha_estoque_geral`, `_adiciona_df_resultado_...`, `_adicionar_lista_peps`, `adicionar_analise_estoque` |
| `tests/unit/test_email.py` | `_buscar_emails_destinatarios`, `_montar_tabela_html`, `_enviar_email_analise_estoque` |
| `tests/unit/test_login_user.py` | `_login_user` |

## Novas classes adicionadas em `test_analisar_cp_estoque.py`

`TestAguardaArquivoReports`, `TestPressionaOkSeExistir`, `TestAguardaBtnSap`, `TestBuscarCompradoresBd`, `TestTraduzirCompradores`, `TestColarMateriaisNoSap`, `TestFecharWorkbooksExportNoExcel`, `TestAnalisarEstoque`

### Nota técnica — `_fechar_workbooks_export_no_excel`
A função usa `import win32com.client as w32` **dentro do corpo**, o que resulta em `w32 = sys.modules["win32com"].client` (atributo do pacote raiz). `patch("win32com.client.GetActiveObject")` patchava `sys.modules["win32com.client"]`, um objeto diferente. A correção foi usar `patch.dict(sys.modules, {"win32com": mock_win32com, "win32com.client": mock_client})` com `mock_win32com.client = mock_client` para garantir consistência.

### Nota técnica — `_enviar_email_analise_estoque`
`email_usuario` é **sempre** incluído em `destinatarios` (linha: `list({*pilares, *responsaveis, email_usuario})`), então o e-mail nunca deixa de ser enviado. `pythoncom` é importado dentro da função (não no módulo), então deve ser mockado via `sys.modules.setdefault("pythoncom", MagicMock())` no topo do arquivo de teste, não via `patch("app.ui.services.email.pythoncom")`.

---

## Status por arquivo de service

### `add_chefia.py`
| Função | Status |
|---|---|
| `make_adicionar_chefia` | ✅ Com teste |

**Testes:** `test_add_chefia.py` (3 testes — add, ignora >20 chars, remove)

---

### `analisar_cp_estoque.py`
| Função | Status |
|---|---|
| `_normaliza_tag` | ✅ Com teste |
| `_clean_key` | ✅ Com teste |
| `_sap_session` | ✅ Com teste |
| `_pasta_sap` | ✅ Com teste |
| `_pasta_downloads` | ✅ Com teste |
| `_limpa_exports` | ✅ Com teste |
| `_aguarda_arquivo` | ✅ Com teste |
| `_aguarda_arquivo_reports` | ✅ Com teste |
| `_pressiona_ok_se_existir` | ✅ Com teste |
| `_aguarda_btn_sap` | ✅ Com teste |
| `_buscar_compradores_bd` | ✅ Com teste |
| `_traduzir_compradores` | ✅ Com teste |
| `_baixar_estoque_mec` | ✅ Com teste |
| `_buscar_lista_comp_sap` | ✅ Com teste |
| `_processar_lista_comp` | ✅ Com teste |
| `_enriquecer_com_estoque_mec` | ✅ Com teste |
| `_colar_materiais_no_sap` | ✅ Com teste |
| `_buscar_ztmm402_por_centro` | ✅ Com teste |
| `_buscar_ztmm402` | ✅ Com teste |
| `_fechar_workbooks_export_no_excel` | ✅ Com teste |
| `_buscar_qtd_pep` | ✅ Com teste |
| `_calcular_aproveitamento` | ✅ Com teste |
| `analisar_estoque` *(pública)* | ✅ Com teste |

**Testes:** `test_analisar_cp_estoque.py` (88 testes no total)

---

### `atualiza_bd.py`
| Função | Status |
|---|---|
| `_to_num` | ✅ Com teste |
| `_to_str` | ✅ Com teste |
| `_adiciona_linha_estoque_geral` | ✅ Com teste |
| `_adiciona_df_resultado_a_lista_aproveitamento_estoque` | ✅ Com teste |
| `_adicionar_lista_peps` | ✅ Com teste |
| `adicionar_analise_estoque` | ✅ Com teste |
| `_get_connection` | — (wrapper simples, testado indiretamente) |

**Testes:** `test_atualiza_bd.py` (20 testes)

---

### `cadastrar_centro.py`
| Função | Status |
|---|---|
| `add_centro` | ✅ Com teste |

**Testes:** `test_cadastrar_centro.py` (11 testes — responsável, chefias, pilares, commits, erros)

---

### `login_user.py`
| Função | Status |
|---|---|
| `_login_user` | ✅ Com teste |

**Testes:** `test_login_user.py` (7 testes — tipos ADMIN/RESPONSAVEL/PILAR, conexão, retorno)

---

### `email.py`
| Função | Status |
|---|---|
| `_buscar_emails_destinatarios` | ✅ Com teste |
| `_montar_tabela_html` | ✅ Com teste |
| `_enviar_email_analise_estoque` | ✅ Com teste |

**Testes:** `test_email.py` (16 testes)

---

## Resumo final

| Arquivo | Funções testadas | Funções sem teste |
|---|---|---|
| `add_chefia.py` | 1 | 0 |
| `analisar_cp_estoque.py` | 23 | 0 |
| `atualiza_bd.py` | 6 | 0 |
| `cadastrar_centro.py` | 1 | 0 |
| `login_user.py` | 1 | 0 |
| `email.py` | 3 | 0 |
| **Total** | **35** | **0** |

**Suite completa: 158 testes passando, 0 falhando.**
