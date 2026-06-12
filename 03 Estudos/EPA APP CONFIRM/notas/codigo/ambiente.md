---
tags: [codigo, ambiente, venv, python, dependencias]
---

# Ambiente Virtual (.venv)

Relacionado: [[app-py]] | [[export-dxf-py]] | [[export-html3d-py]]

---

## Configuração

| Item | Valor |
|---|---|
| Python | 3.12.2 |
| Diretório do venv | `.venv\` (raiz do projeto) |
| Intérprete | `.venv\Scripts\python.exe` |
| Pip | 24.0 (no venv) |

---

## Pacotes Instalados (pinados)

```
contourpy==1.3.3
cycler==0.12.1
ezdxf==1.4.4
fonttools==4.63.0
kiwisolver==1.5.0
matplotlib==3.11.0
numpy==2.4.6
packaging==26.2
pillow==12.2.0
pyparsing==3.3.2
python-dateutil==2.9.0.post0
six==1.17.0
typing_extensions==4.15.0
```

> Arquivo `requirements.txt` na raiz contém estas versões exatas.

---

## Como Recriar o Ambiente

Se precisar recriar (nova máquina, Python reinstalado):

```powershell
# Na pasta do projeto:
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

---

## Como Rodar

| Método | Comando |
|---|---|
| **Duplo clique** | `run.bat` |
| **PowerShell** | `.\.venv\Scripts\python.exe app.py` |
| **VS Code** | Selecionar intérprete → `.venv\Scripts\python.exe` |
| **Terminal CMD** | `.venv\Scripts\python.exe app.py` |

---

## `run.bat`

```bat
@echo off
"%~dp0.venv\Scripts\python.exe" "%~dp0app.py"
```

`%~dp0` = diretório onde o `.bat` está localizado → funciona independente de onde o terminal está.

---

## Pacotes Diretos do Projeto

| Pacote | Para que serve |
|---|---|
| `matplotlib 3.11.0` | Geração das 4 vistas (subplots), embedding no tkinter |
| `numpy 2.4.6` | Reservado para cálculos futuros (v0.2+) |
| `ezdxf 1.4.4` | Geração de arquivos DXF (exportar_dxf) |
| `pillow 12.2.0` | Dependência do matplotlib (processamento de imagem) |

> `tkinter` não aparece no `requirements.txt` pois é parte da biblioteca padrão do Python — instalado junto com o Python.

---

## Notas

- O `.venv` **não deve ser commitado** no git (já no `.gitignore` se houver)
- Three.js para o HTML 3D vem de CDN — não está no venv
- Se no futuro for necessário suporte offline ao HTML 3D, será preciso baixar o bundle Three.js e incluir no projeto
