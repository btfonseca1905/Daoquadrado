# 📝 Template de Plano de Execução Técnico

**Card/Issue:** #{numero_da_issue}  
**Título:** [Título da Feature]  
**Status:** Planejamento  
**Data:** [Data de Criação]

---

## 1. Objetivo da Feature
[Descreva o objetivo geral da funcionalidade, o valor técnico e de negócios que ela gera, e resuma os critérios de aceitação BDD.]

---

## 2. Análise de Impacto

### 2.1. Projetos Afetados
- [ ] **BaseSender.Domain** (.NET 10 — entidades e enums)
- [ ] **BaseSender.Api** (.NET 10 — FastEndpoints, EF Core, Inertia)
- [ ] **client** (Vue 3 + Inertia + PrimeVue + Tailwind)
- [ ] **database/migrations** (dbmate)
- [ ] **e2e** (Playwright)
- [ ] **infra / CI** (`.github/workflows`, Dockerfile)

### 2.2. Camadas Internas Afetadas

#### BaseSender.Domain
- [ ] **Entities** — entidade herdando `BaseEntity` (`Entities/`)
- [ ] **Enums** — enumerações e classes de constantes de status (`Enums/`)

#### BaseSender.Api
- [ ] **Features** — fatia vertical em `Features/{Área}/{Ação}/` (Request + Validator + Response + Endpoint)
- [ ] **Infra** — `IEntityTypeConfiguration<T>` em `Infra/Configurations/` e `DbSet` em `Infra/AppDbContext.cs`
- [ ] **Shared** — helpers transversais (`Result<T>`, extensões de endpoint, `ICurrentUserService`)
- [ ] **Services** — integrações externas (Keycloak Admin, storage de avatar, provedores)
- [ ] **Configurations / Program.cs** — pipeline, autenticação, DI

#### database
- [ ] **Migration dbmate** — `database/migrations/{timestamp}_{nome}.sql` com `-- migrate:up` e `-- migrate:down`

#### client
- [ ] **Pages** — uma página por rota Inertia (`src/Pages/`)
- [ ] **Components** — componentes do módulo (`src/Components/{Área}/`)
- [ ] **Components/Ui** — componentes reutilizáveis do design system
- [ ] **composables** — lógica compartilhada (`src/composables/`)
- [ ] **style.css** — tokens de tema, se a feature exigir cor nova

---

## 3. Arquivos a Serem Modificados

| Projeto | Caminho do Arquivo | Tipo | Ação Técnica |
| :--- | :--- | :--- | :--- |
| `base-sender-core` | `[caminho/completo/arquivo]` | Novo / Modificado | [O que será desenvolvido] |

---

## 4. Implementação Detalhada por Etapa

> A ordem abaixo é a que o projeto usa: **banco → domínio → persistência → endpoint → tela**. Não inverta.

### Etapa 1: Migration (dbmate)
**Objetivo:** [Criar tabelas/colunas e índices]

**Arquivo:** `database/migrations/{timestamp}_{nome}.sql`
```sql
-- migrate:up

-- migrate:down
```
**Pontos de Atenção:**
- Índices únicos são filtrados por `WHERE is_removed = false`.
- Nunca usar `dotnet ef migrations` — o projeto não usa EF Migrations.

---

### Etapa 2: Domínio e Persistência (.NET 10)
**Objetivo:** [Entidade, configuração EF e DbSet]

**Arquivo:** `src/BaseSender.Domain/Entities/{Entidade}.cs`
```csharp
// entidade herdando BaseEntity
```

**Arquivo:** `src/BaseSender.Api/Infra/Configurations/{Entidade}Configuration.cs`
```csharp
// ToTable, colunas snake_case, índices filtrados, relacionamentos
```

---

### Etapa 3: Endpoints (FastEndpoints)
**Objetivo:** [Endpoints de página e/ou de dados]

**Arquivo:** `src/BaseSender.Api/Features/{Área}/{Ação}/{Ação}Endpoint.cs`
```csharp
// Request, Validator, Response e Endpoint no mesmo arquivo (REPR)
// Leitura → this.ViewAsync("Pagina", props)
// Escrita → HttpContext.Response.SendAsync(Result<T>.Success(...), 200)
```
**Pontos de Atenção:**
- Resolver o tenant com `GetCurrentCompanyIdAsync` e filtrar toda query por ele.
- Preencher auditoria com `GetCurrentUserIdAsync`.
- Validar a permissão do perfil no backend, não só ocultando o botão na tela.

---

### Etapa 4: Frontend (Vue 3 + Inertia)
**Objetivo:** [Páginas, componentes e consumo da API]

**Arquivo:** `src/client/src/Pages/{Pagina}.vue`
```vue
<!-- props tipadas vindas do endpoint, componentes de Components/Ui -->
```
**Pontos de Atenção:**
- Props chegam em camelCase.
- Chamadas de escrita com `axios`, tratando erro com `extractErrorMessage`/`applyFieldErrors`.
- Após mutação, recarregar com `router.reload({ only: [...] })`.
- Usar os tokens de tema (`bg-surface`, `text-content-primary`…), nunca cores cruas.

---

## 5. Regras de Negócio Implementadas

| ID | Regra de Negócio | Localização da Implementação |
| :--- | :--- | :--- |
| **RN01** | [Nome da Regra] | [Ex: `CreateXEndpoint.cs` Validator / índice único da migration] |

---

## 6. Testes e Validação de Aceite

### Cenários de Teste (BDD)
1. **[Cenário 1]**
   - **Dado** [Estado inicial]
   - **Quando** [Ação]
   - **Então** [Resultado observado]
2. **[Cenário 2 — isolamento entre empresas]**
   - **Dado** um registro de outra empresa
   - **Quando** o endpoint é chamado com o id dele
   - **Então** a resposta é 404

### Checklist de Homologação
- [ ] `dotnet build BaseSender.sln` sem erros
- [ ] `npx vue-tsc --noEmit` sem erros
- [ ] `npm run build` no `src/client` concluído
- [ ] Migration aplicada (`dbmate up`) e esquema conferido
- [ ] Testes E2E do Playwright executados (se houver cobertura)
- [ ] Fluxo visual validado no tema escuro, sem elemento claro sobrando
- [ ] Critérios de aceitação validados pelo usuário

---

## 7. Documentação Técnica a Atualizar
- [ ] `docs/architecture/api_rules.md` — novos contratos ou padrões de endpoint
- [ ] `docs/architecture/frontend_rules.md` — novos padrões de componente ou token
- [ ] `docs/architecture/database_rules.md` — nova convenção de esquema
- [ ] `specs/...` — nova especificação técnica da feature

---

## 8. Planejamento de Atividades (Tasks)
Lista de tarefas detalhadas a serem executadas localmente pelo desenvolvedor:
1. **[Atividade — Banco]**
   - Criar a migration dbmate e aplicá-la no ambiente de desenvolvimento.
2. **[Atividade — Backend]**
   - Entidade, configuração EF, DbSet e endpoints da fatia vertical.
3. **[Atividade — Frontend]**
   - Páginas, componentes e consumo dos endpoints.
4. **[Atividade — Testes]**
   - Cenários E2E no Playwright e validação dos critérios de aceite.
5. **[Atividade — Especificação]**
   - Atualizar as specs e as diretrizes de arquitetura na base de conhecimento.
