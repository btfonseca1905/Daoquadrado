---
name: spec
description: Elabora a especificação técnica (spec) de um card a partir da história de usuário, cobrindo arquitetura, contratos de API, regras de negócio, schema e cenários BDD. Use depois que a história estiver pronta e antes do plano de execução.
---

# /spec — Criação de Especificação Técnica

Alvo (card/Issue/argumentos): **$ARGUMENTS**

Guie a elaboração de uma especificação técnica detalhada de uma nova feature do Base Sender, traduzindo a história de usuário em um guia arquitetural e técnico preciso. O template está em `references/spec-template.md`: **use-o sempre**, sem inventar estrutura própria.

> **Regra de persistência (obrigatória)**: a spec é gravada como arquivo **`spec.md`** em `artefatos/<card_id>/spec.md` (na raiz do repositório de trabalho), com nome sempre fixo para nunca existirem duas specs do mesmo card (sobrescreva a anterior após confirmar). **Nunca** escreva a spec no card/Issue (descrição, label ou sub-issue): o card contém somente a história. O workflow só está concluído depois que o arquivo foi gravado.

## Passo 1 — Ler a história de usuário

- Carregue o card/Issue da feature (`gh issue view <número> --repo <org>/docs`). A leitura serve só de contexto de negócio; a spec nunca vai nele.
- Extraia objetivos de negócio, fluxo da tela, regras de restrição e cenários de aceite (BDD).
- **Perfis**: confirme quais dos três perfis (Admin, Gestor, Operador) executam a ação. Se a história não disser, pergunte: a perfilização muda o desenho do endpoint.

## Passo 2 — Carregar documentação e specs relacionadas

Leia, no repositório de documentação (`docs`):

- **Mapeamento de projetos**: `docs/projects/README.md`.
- **Regras de arquitetura**: `docs/architecture/api_rules.md`, `docs/architecture/frontend_rules.md` e `docs/architecture/database_rules.md`.
- **Specs relacionadas (sempre, para consistência)**: liste as specs existentes em `specs/` e leia as do mesmo módulo/domínio da feature, mantendo nomenclatura, contratos e regras coerentes (ex.: ao especificar números, leia `specs/wabas-numeros.md` e `specs/wabas-overview.md`). Se nenhuma tiver relação, registre isso e siga: a leitura é obrigatória, o achado não.

## Passo 3 — Analisar documentação e explorar o código local

- **Análise prévia**: leia com atenção as regras de arquitetura, o mapeamento e as specs relacionadas.
- **Solicitação do repositório**: pergunte obrigatoriamente ao desenvolvedor o caminho absoluto do repositório local (ou confirme se deve usar a pasta ativa) antes de qualquer varredura (Glob), busca (Grep) ou leitura de arquivos.
- **Branch**: se precisar criar branch de trabalho/pesquisa, gere-a a partir da **`main`** do `base-sender-core` (o repositório **não tem branch `dev`**), salvo pedido explícito em contrário.
- **Investigação de código**, nas áreas afetadas do `base-sender-core`:
  - **Frontend**: `src/client/src/Pages/` (páginas Inertia) e `src/client/src/Components/` (`Shared`, `Ui` e a pasta do módulo).
  - **Backend**: `src/BaseSender.Api/Features/{Área}/` (endpoints), `src/BaseSender.Api/Infra/Configurations/` (mapeamento EF) e `src/BaseSender.Domain/Entities/` (entidades).
  - **Banco**: `database/migrations/` para ver o esquema vigente e o padrão das migrations dbmate.

## Passo 4 — Desenhar a arquitetura da feature

- **Modelo de dados**: novas tabelas ou colunas no PostgreSQL. Toda tabela nova herda o padrão do `BaseEntity` (soft delete + auditoria) e usa snake_case (ver `database_rules.md`).
- **Isolamento multi-tenant**: defina como a nova entidade se liga à `company`. Nenhum endpoint aceita `company_id` vindo do cliente; ele é sempre resolvido no servidor.
- **Contratos de API**: separe endpoints que **renderizam página** (resposta Inertia) dos que **recebem dados** (JSON com `Result<T>`).
- **Segurança**: avalie a necessidade de novas roles no Keycloak e como a permissão é checada no backend (não apenas ocultando o botão).
- **Integrações externas**: se tocar WABA/números, explicite o que é responsabilidade da Meta, da Pontal e da Sisbratel, e o que o Base Sender só sincroniza.
- **Fluxograma Mermaid**: diagrama de sequência ou fluxo da comunicação entre frontend, backend, banco e integrações.

## Passo 5 — Escrever a spec

Siga **rigorosamente** `references/spec-template.md`, sem pular seções. Detalhe:

- Regras de negócio associadas aos campos técnicos correspondentes.
- Padrões de retorno de erro e validações críticas (cooldowns, vazios, formatos, unicidade).
- Mudanças de schema e a migration dbmate correspondente.

## Passo 6 — Revisão e persistência

1. Apresente um resumo da spec no chat e só avance após **aprovação explícita**.
2. **(Opcional)** Se já existir `artefatos/<card_id>/spec.md`, exiba a versão anterior antes de sobrescrever.
3. Grave a spec em `artefatos/<card_id>/spec.md`.
4. Confirme ao usuário:
   - ✅ Especificação técnica revisada e aprovada.
   - ✅ Spec gravada em `artefatos/<card_id>/spec.md`.
   - ✅ Próximo passo: gerar o plano de execução técnico com `/plan`.
