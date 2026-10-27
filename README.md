# D² [do Discovery ao Delivery] — Skills de Produto

Coleção unificada de 10 Skills de IA da **Bruna Fonseca | b-a.BA Educação Corporativa**, para cobrir o caminho do Discovery ao Delivery.

## Skills incluídas

| Skill (pasta em `skills/`) | O que faz |
|---|---|
| `gerar-one-pager-produto` | Entrevista guiada que entrega um One-Pager de Produto em Markdown |
| `prd-lovable-bruna-fonseca` | Discovery, MVP, PRD em Markdown, fluxos Mermaid e prompt de prototipação para o Lovable |
| `metricas-heart-produto` | Matriz de métricas com o framework HEART, fórmulas explicadas e preview opcional de dashboard |
| `roadmap-lean-inception` | Roadmap com Lean Inception: valor, esforço, confiança, ondas e quarters |
| `validar-prototipo-persona` | Valida um protótipo web navegando com uma persona sintética (.md) e gera relatório de UX |
| `story` | Entrevista para criar histórias de usuário com critérios de aceite |
| `spec` | Especificação técnica de um card |
| `plan` | Plano de execução técnico de um card |
| `execute` | Implementa o plano técnico aprovado |
| `bug` | Entrevista para documentar bugs reproduzíveis |

> **Atenção:** `story`, `spec`, `plan`, `execute` e `bug` dependem do MCP **gf7-delivery-mcp** conectado na sua IA. Sem ele, elas informam o erro e param. As outras cinco funcionam sozinhas.

## Pré-requisitos

- Uma IA com suporte a Skills: **Claude Code** (terminal ou extensão do VS Code) ou **Codex** (VS Code/CLI).
- `git` instalado (ou baixe o repositório em ZIP pelo botão **Code → Download ZIP** do GitHub).

## 1. Baixar o repositório

```bash
git clone https://github.com/btfonseca1905/Daoquadrado.git
cd Daoquadrado
```

## 2. Instalar as Skills

Cada Skill é uma pasta dentro de `skills/`. Instalar é copiar essas pastas para o diretório de Skills da sua IA. Escolha **um** destino por ferramenta:

| Ferramenta | Só neste projeto | Para todos os projetos |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |

`~` é a sua pasta de usuário (no Windows, `C:\Users\SEU_USUARIO`).

### Claude Code

macOS / Linux / Git Bash:

```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills"
Copy-Item -Recurse -Force .\skills\* "$HOME\.claude\skills\"
```

Depois reabra o Claude Code. Invoque pelo nome, por exemplo `/roadmap-lean-inception` ou `/story`.

### Codex

macOS / Linux / Git Bash:

```bash
mkdir -p ~/.agents/skills
cp -r skills/* ~/.agents/skills/
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
Copy-Item -Recurse -Force .\skills\* "$HOME\.agents\skills\"
```

Depois reabra o VS Code. Invoque com `$`, por exemplo `$metricas-heart-produto`.

### Instalar só algumas Skills

Copie apenas as pastas que quiser, por exemplo:

```bash
cp -r skills/roadmap-lean-inception ~/.claude/skills/
```

> A pasta da Skill deve ser copiada **inteira** (com `SKILL.md`, `references/`, `scripts/`, `assets/`). Não copie só o `SKILL.md`.

## 3. Conferir se funcionou

Peça à IA: *"Quais Skills você tem disponíveis?"*. Os nomes da tabela acima devem aparecer. Se não aparecerem, confira se a pasta copiada contém um `SKILL.md` direto dentro dela (`.../skills/NOME/SKILL.md`) e reabra a ferramenta.

## 4. Exemplos para começar

- `/gerar-one-pager-produto` — "Quero um one-pager da minha ideia de produto."
- `/prd-lovable-bruna-fonseca` — "Quero transformar minha ideia em PRD e protótipo no Lovable."
- `/metricas-heart-produto` — "Defina as métricas do meu produto com HEART."
- `/roadmap-lean-inception` — "Monte meu roadmap a partir destes épicos."
- `/validar-prototipo-persona` — "Valide este protótipo com a persona do arquivo persona.md."

## Observações

- `metricas-heart-produto` inclui a planilha `assets/base-metricas.xlsx`. Ela é pública se o repositório for público.
- `validar-prototipo-persona` precisa de uma ferramenta de navegação (browser) disponível na sua IA.
- `metricas-heart-produto` e `roadmap-lean-inception` trazem scripts Python opcionais; as Skills funcionam sem executá-los.

Conheça o D² [do Discovery ao Delivery]: [www.daoquadrado.com.br](http://www.daoquadrado.com.br)
