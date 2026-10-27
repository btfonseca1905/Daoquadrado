---
name: execute
description: Executa a implementação do plano técnico aprovado, com branch, PR, build e homologação pelo usuário. Use depois que spec e plano estiverem aprovados.
---

# /execute — Execução e Implementação do Plano Técnico

Alvo (card/Issue/argumentos): **$ARGUMENTS**

Implemente as alterações de código do Base Sender conforme o plano aprovado, garantindo build limpo e homologação pelo usuário.

> **Regra de persistência**: Plano (`plan.md`) e Spec (`spec.md`) ficam em `artefatos/<card_id>/`, gerados por `/plan` e `/spec`. Carregue-os sempre dali, nunca do corpo do card. O card contém somente a história.

## Passo 1 — Carregar plano, spec e diretrizes

1. Leia `artefatos/<card_id>/plan.md`. Se não existir, **interrompa** e direcione o desenvolvedor a rodar `/plan` primeiro. Exiba um resumo das etapas no chat.
2. Leia também `artefatos/<card_id>/spec.md` para relembrar o contexto arquitetural.
3. Leia as diretrizes de arquitetura do repositório de documentação: `docs/architecture/api_rules.md`, `frontend_rules.md` e `database_rules.md`.

## Passo 2 — Preparar o ambiente Git

1. **Repositórios**: o código vive em `base-sender-core`; documentação e histórias vivem em `docs`.
2. **Atualizar a base**: a branch de feature sai da **`main`** (o `base-sender-core` **não tem branch `dev`**), salvo pedido explícito da história, da spec ou do desenvolvedor. Rode `git checkout main` e `git pull`.
3. **Criar a feature branch**: `git checkout -b feature/{numero_da_issue}` (ex.: `feature/100`).

## Passo 3 — Vincular branch e PR ao card

Depois de criar a branch e commitar as primeiras alterações:

1. **Publicar a branch e vinculá-la à issue** (aparece na seção "Development" do card):
   ```
   git push -u origin feature/{numero_da_issue}
   ```
   Referencie a issue nos commits (`feat({numero_da_issue}): ...`) ou vincule pela interface do GitHub.
2. **Abrir o Pull Request**, vinculado ao card:
   ```
   gh pr create --repo <org>/base-sender-core --base main --head feature/{numero_da_issue} \
     --title "feat({numero_da_issue}): {titulo_da_feature}" --body "Closes <org>/docs#{numero_da_issue}"
   ```
3. **Mover o card** no quadro de projetos: `Fazendo` ao começar; `Code Review` ao abrir o PR; `Aguardando Testes` ao entregar para teste.

## Passo 4 — Implementar e compilar

Siga à risca as etapas do plano, na ordem que o projeto usa:

1. **Banco (`database/migrations/`)**: crie a migration dbmate (`-- migrate:up` / `-- migrate:down`) antes de mexer no modelo. Nunca use `dotnet ef migrations`: o projeto não usa EF Migrations.
2. **Domínio (`src/BaseSender.Domain/`)**: entidades herdando `BaseEntity`, com classes de constantes de status quando aplicável.
3. **Persistência (`src/BaseSender.Api/Infra/`)**: `IEntityTypeConfiguration<T>` em `Configurations/` mapeando snake_case e índices filtrados, mais o `DbSet` no `AppDbContext`.
4. **Endpoints (`src/BaseSender.Api/Features/{Área}/`)**: Request, Validator, Response e Endpoint no mesmo arquivo. Endpoints de leitura renderizam página via `ViewAsync`; os de escrita retornam `Result<T>` em JSON.
5. **Frontend (`src/client/src/`)**: páginas em `Pages/`, componentes no módulo correspondente, reaproveitando `Components/Ui/`. Consumo de API com `axios` e os helpers de `composables/useFormErrors`.
6. **Validação de sintaxe**: garanta que tudo compila limpo:
   ```
   dotnet build BaseSender.sln
   cd src/client && npx vue-tsc --noEmit && npm run build
   ```

## Passo 5 — Homologação e testes pelo usuário

A IA codifica, mas a validação final de negócio cabe ao usuário:

1. Apresente um resumo claro dos arquivos modificados e da lógica aplicada.
2. Solicite:
   > *"Por favor, execute os testes locais da funcionalidade na sua máquina para validar os cenários de aceite (BDD). Me reporte se encontrar qualquer bug ou comportamento divergente."*
3. Se a feature tiver cobertura E2E, rode os testes Playwright de `e2e/` e reporte o resultado.
4. Se o usuário apontar inconsistências, corrija e repita build e teste.
5. **Condição de parada**: só avance com a confirmação explícita de aprovação e homologação funcional.

## Passo 6 — Relatório de entrega (opcional)

Spec e Plano são os únicos artefatos obrigatórios. O relatório é apenas resumo de apoio:

1. Detalhe: modificações por camada (banco, domínio, API, frontend), lista de arquivos alterados no commit e status de aprovação dos cenários homologados.
2. Se quiser registro, grave em `artefatos/<card_id>/accomplished.md`.
3. Confirme a conclusão:
   - ✅ Alterações codificadas e compiladas.
   - ✅ Branch e PR vinculados ao card.
   - ✅ Card movido para a coluna correta do board.
   - ✅ Homologado pelo usuário final.
   - ✅ (Opcional) Relatório de entrega em `artefatos/<card_id>/accomplished.md`.
