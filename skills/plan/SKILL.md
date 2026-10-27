---
name: plan
description: Cria o plano de execução técnico de um card, lendo a história, a spec e o código local, e detalhando arquivos, etapas, riscos e testes antes de qualquer implementação. Use depois da spec aprovada.
---

# /plan — Criação de Plano de Execução Técnico

Alvo (card/Issue/argumentos): **$ARGUMENTS**

Mapeie exatamente como a funcionalidade será implementada no código do Base Sender, gerando um plano técnico detalhado, passo a passo, **antes de escrever qualquer código**. O template está em `references/plan-template.md`: **use-o sempre**.

> **Regra de persistência (obrigatória)**: o plano é gravado como arquivo **`plan.md`** em `artefatos/<card_id>/plan.md`, com nome sempre fixo para nunca existirem dois planos do mesmo card. **Nunca** escreva o plano no card/Issue: o card contém somente a história. Uma cópia de trabalho opcional em `execution_plan_{card_id}.md` na raiz do repositório local serve só de apoio na implementação. O workflow só está concluído depois que `plan.md` foi gravado.

## Passo 1 — Analisar a história e carregar a spec

- **Leitura conjunta obrigatória**: leia a **história** (card) **e** a **spec** (`artefatos/<card_id>/spec.md`). O plano se baseia nas duas combinadas, nunca em apenas uma.
- **Carregar a história**: `gh issue view <número> --repo <org>/docs`.
- **Spec não encontrada**: se `artefatos/<card_id>/spec.md` não existir e o desenvolvedor não indicou outro arquivo, peça: *"Não encontrei a Spec deste card. Pode rodar `/spec` primeiro, indicar o caminho de um arquivo local ou colar o conteúdo da especificação?"*
- Identifique critérios de aceitação e limites do escopo.
- **Se já existir `artefatos/<card_id>/plan.md`**, exiba-o no chat e peça confirmação para sobrescrever ou reutilizar antes de elaborar um novo.

## Passo 2 — Carregar documentação e specs relacionadas

No repositório de documentação (`docs`), leia:

- **Mapeamento de projetos**: `docs/projects/README.md`.
- **Diretrizes de arquitetura**: `docs/architecture/api_rules.md`, `frontend_rules.md` e `database_rules.md`.
- **Specs relacionadas** (além da spec do próprio card): liste `specs/` e leia as do mesmo módulo/domínio, para respeitar contratos e regras já documentados.

## Passo 3 — Analisar documentação e explorar o código local

- **Análise prévia**: leia as regras de arquitetura, o mapeamento e as specs relacionadas.
- **Solicitação do repositório**: pergunte obrigatoriamente ao desenvolvedor o caminho absoluto do repositório local (ou confirme a pasta ativa) antes de qualquer varredura (Glob), busca (Grep) ou leitura de arquivos.
- **Leitura obrigatória de código local**: para um plano **extremamente técnico**, navegue pelas pastas e leia o código-fonte dos arquivos que serão modificados. O plano deve detalhar passo a passo o que muda e onde. Não faça suposições genéricas sem verificar o código existente.
- **Branch**: a branch de feature sai da **`main`** do `base-sender-core` (**não existe branch `dev`**), salvo pedido explícito da história, da spec ou do desenvolvedor.
- **Investigação dirigida**: siga o padrão de fatia vertical — um módulo costuma tocar `Features/{Área}/`, `Infra/Configurations/`, `Domain/Entities/`, `database/migrations/` e `client/src/Pages` + `client/src/Components`.

## Passo 4 — Mapear impactos por projeto e camada

- **BaseSender.Domain** (.NET 10): entidades em `Entities/` (herdando `BaseEntity`) e enums em `Enums/`.
- **BaseSender.Api** (.NET 10 / FastEndpoints):
  - Feature slice em `Features/{Área}/{Ação}/` — Request, Validator, Response e Endpoint no mesmo arquivo (REPR).
  - Mapeamento EF em `Infra/Configurations/{Entidade}Configuration.cs` e `DbSet` em `Infra/AppDbContext.cs`.
  - Serviços de integração em `Services/`, utilitários transversais em `Shared/`.
  - Pipeline em `Configurations/` e `Program.cs`.
- **Banco**: nova migration em `database/migrations/{timestamp}_{nome}.sql`, formato dbmate (`-- migrate:up` / `-- migrate:down`).
- **client** (Vue 3 + Inertia + PrimeVue + Tailwind): páginas em `src/Pages/`, componentes de módulo em `src/Components/{Área}/`, reutilizáveis em `Components/Ui/` e `Components/Shared/`, composables em `src/composables/`, tokens de tema em `src/style.css`.
- **e2e** (Playwright): cenários em `e2e/tests/` e page objects em `e2e/pages/`.

## Passo 5 — Gerar o plano detalhado

Siga **rigorosamente** `references/plan-template.md`. O plano deve conter:

- Os arquivos específicos a criar/modificar (caminhos completos).
- Trechos de rascunho de código das mudanças lógicas propostas.
- Sequência exata de execução (migration → domínio → configuração EF → endpoint → tela).
- Riscos técnicos (performance, concorrência, isolamento entre empresas, limites de rate limit de integrações externas).

## Passo 6 — Revisão do usuário

Apresente o plano estruturado no chat e exija **aprovação explícita**. Se houver pedidos de alteração, refine e reapresente. Só prossiga com confirmação.

## Passo 7 — Persistir o plano

1. Grave o plano em `artefatos/<card_id>/plan.md` (substituindo o existente, nunca duplicando). **Não** grave o plano no corpo do card.
2. **Cópia local (opcional)**: `execution_plan_{card_id}.md` na raiz do repositório local. Ela **não** é o registro oficial.
3. Só reporte conclusão depois de confirmar que o arquivo foi gravado. Descrever o plano no chat sem gravar **não conta como concluído**.
4. Confirme ao usuário:
   - ✅ Plano de execução técnico gerado e aprovado.
   - ✅ Plano gravado em `artefatos/<card_id>/plan.md`.
   - ✅ (Opcional) Cópia local em `<caminho_repositorio>/execution_plan_{card_id}.md`.
   - ✅ Próximo passo: implementar com `/execute`.
