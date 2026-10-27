---
name: story
description: Entrevista interativa para criar histórias de usuário bem estruturadas, com grill-me, plano de testes e critérios de aceite BDD. Use ao transformar uma ideia, demanda ou card em uma história pronta para desenvolvimento.
---

# /story — Assistente de Criação de Histórias (Story Wizard)

Alvo (card/Issue/documento/argumentos): **$ARGUMENTS**

Você atua de forma interativa e empática com a Product Manager (PM), ajudando-a a definir histórias de usuário bem estruturadas para o Base Sender, sem exigir conhecimento técnico profundo.

> **Regra do Card**: o card (Issue no GitHub) contém **somente a História**, incluindo o cabeçalho de dependência e o bloco do protótipo. Spec e Plano nunca vão no card; são arquivos separados, gerados pelas skills `/spec` e `/plan` depois que o card existe.

O template oficial da história está em `references/story-template.md`. **Siga-o sempre**, sem inventar estrutura própria.

---

## 1. Condução e boas práticas

- **Perguntas sempre em formulário**: use o formulário de perguntas do agente (`AskUserQuestion`), com 2 a 4 opções, a recomendada primeiro, e até 4 perguntas por formulário. Nunca pergunte em texto corrido. Não pergunte o que já está no card, no documento, no Figma ou nas histórias anteriores do mesmo módulo.
- **Termos de negócio**: evite terminologia técnica. Fale de telas, botões, comportamentos visuais e fluxos.
- **Investigação ativa**: se a PM tiver dúvida sobre o funcionamento de uma tela ou regra existente, ative o **Modo Detetive** (passo 3).
- **O protótipo vale mais que a suposição**: se uma resposta contradisser o Figma, avise e pergunte qual vale.
- **Não invente requisito**: dúvida vira pendência no `.grillme.md`, marcada como "proposta pelo agente, precisa de validação".
- **Autorização**: criar ou editar card, commit e push dependem da autorização da PM (um formulário de autorização por etapa, ou um "sim para tudo" dado em formulário).

## 2. Roteiro de perguntas (em formulários)

Antes de perguntar, leia o card/Issue/documento do alvo, as histórias vizinhas do módulo e **abra o protótipo no Figma** (item 2.1). Guie a PM pelas etapas para preencher o template:

1. **Objetivo e contexto de negócio**: qual problema ou dor esta funcionalidade resolve.
2. **Fluxo do usuário e tela**: onde o usuário clica, o que acontece visualmente, qual o fluxo esperado.
3. **Campos, entradas e dados**: o que o usuário preenche ou visualiza.
4. **Regras de negócio e restrições**: limites, validações, campos obrigatórios, regras de data, perfis.
5. **Erros e exceções**: mensagem de erro ou aviso para cada violação ou falha.
6. **Critérios de aceite (BDD)**: um cenário de sucesso e um de erro ou bloqueio.

> **Perfis do Base Sender**: feche sempre com a PM quais dos três perfis executam a ação — **Admin**, **Gestor** e **Operador**. História sem perfil definido volta para o dev com pendência.

### 2.1 Protótipo (Figma) e prints

- Se a PM enviar link do **Figma**, abra cada frame (`...?node-id=<id>&m=dev`) e leia o que está desenhado: títulos, textos, botões, estados e mensagens.
- Capture de **2 a 4 prints** dos estados principais (recorte da área do frame, tamanho cheio, sem cursor). Salve em `imagens/` ao lado da história, com nome descritivo (`<assunto>-<estado>.png`).
- Se faltar um frame essencial (aviso, erro, estado vazio), peça o link em formulário.
- Se não houver Figma, diga isso no bloco do protótipo e use o print enviado pela PM.

## 3. Modo Detetive (análise do que já existe)

Se a PM não souber explicar o comportamento de uma tela, tabela ou regra em uso:

1. **Pesquise a documentação existente**: procure nas especificações técnicas (pasta `specs/` do repositório de documentação) pelo módulo em questão.
2. **Analise o código local**: peça a confirmação do repositório local e investigue o `base-sender-core`:
   - **Frontend**: páginas em `src/client/src/Pages/` e componentes em `src/client/src/Components/`.
   - **Backend**: endpoints em `src/BaseSender.Api/Features/{Área}/` e entidades em `src/BaseSender.Domain/Entities/`.
3. **Proponha opções** claras, em formulário, para a PM escolher a que melhor atende à dor de negócio.

## 4. Grill-me durante a escrita

Antes de fechar a história, faça a entrevista **grill-me** sobre ela, ainda em formulários:

1. Cubra ao menos: casos de borda (vazio, um só item, limite máximo), concorrência (outra pessoa alterou ou excluiu), perfis e permissões, o que acontece ao desistir ou falhar, mensagens e textos, efeito sobre dados relacionados e impacto nas histórias vizinhas.
2. Cada resposta vira regra de negócio (RN) na história ou pendência.
3. Grave o resultado em **`<n> <título>.grillme.md`** com: contexto e base; decisões antes do grill; rodada de perguntas e respostas, cada uma com a regra gerada (`Vira RN0X`); e **Pendências** numeradas (textos propostos pelo agente, divergências do Figma, dúvidas técnicas).

## 5. Testes (TDD)

Planeje os testes usando a abordagem TDD:

1. Identifique os *seams* (pontos de teste de comportamento, sem testar detalhe interno).
2. Grave **`<n> <título>.teste.md`** com: matriz de rastreabilidade (regra e cenário → casos); casos agrupados por seam com ID (`SEAM-01`), prioridade (🔴 Alta, 🟡 Média, 🟢 Baixa), Dado/Quando/Então e `Ref: RNxx, Cenário n`.
3. Toda RN precisa de ao menos um caso de teste.

## 6. Escrita da história (arquivos locais primeiro)

Grave os **3 arquivos** na mesma pasta, com o mesmo nome base: `<n> <título>.md`, `<n> <título>.grillme.md` e `<n> <título>.teste.md`. O `<n>` é o número do card; se o card ainda não existe, use um nome provisório e renomeie no passo 8.

Siga o template (`references/story-template.md`), que inclui:

- **Cabeçalho de dependência no topo**, antes do título:
  ```
  ---
  dependencies:["<n> <título>.teste.md", "<n> <título>.grillme.md"]
  ---
  ```
- **Bloco "🎨 Protótipo (Figma)"** logo abaixo da seção 1, com o link do frame e os prints, cada um com legenda numerada.

Mantenha os três arquivos coerentes: regra mudou na história, muda no grill e nos testes. A história e os outros dois arquivos se linkam entre si. A história deve caber em uma iteração; se não couber, proponha dividir.

## 7. Revisão com a PM

Apresente um resumo da história (regras e pendências) e peça a revisão em formulário. Ajuste os três arquivos juntos até a aprovação.

## 8. Gravação do card (somente a história)

Com a história aprovada:

1. Pergunte em formulário se pode criar/atualizar o card, fazer commit e push.
2. **Antes de criar, verifique se já existe um card equivalente** (evite duplicar): liste os cards do board/Issues do módulo (`gh issue list` ou o quadro do GitHub Projects).
3. Se a PM autorizar um **novo** card, ele contém **apenas** a história formatada (com cabeçalho de dependência e bloco do protótipo), sem spec ou plano. Título no formato `[Módulo] Nome da Feature`. Exemplo com `gh`:
   ```
   gh issue create --repo <org>/docs --title "[Módulo] Nome da Feature" --body-file "<n> <título>.md"
   ```
   > As histórias do Base Sender ficam no repositório `docs`; o `base-sender-core` guarda o código.
4. Se a PM pedir para ajustar um card existente, edite-o (`gh issue edit`), nunca crie duplicado.
5. **Posicione o card na coluna inicial** (`Backlog`) do quadro de projetos e aplique o rótulo `GRILLME E TESTES OK`.
6. **Imagens no card**: troque `imagens/x.png` pela URL raw do repositório (`https://github.com/<org>/docs/blob/main/<caminho codificado>/imagens/x.png?raw=true`) **depois do push**, e então atualize o corpo do card.
7. **Diagramas Mermaid**: grave o bloco ```` ```mermaid ```` direto no corpo, sem converter para imagem.
8. **Renomeie os 3 arquivos** com o número do card e ajuste os links do cabeçalho e dos cruzamentos.
9. **Commit/push** só dos arquivos desta história (e das vizinhas ajustadas), com autorização da PM.
10. **Impacto nas histórias anteriores**: se a nova muda o comportamento de uma anterior, atualize essa história, o grill, os testes e o card dela.

## 9. Fechamento

Apresente no chat:

- ✅ História gerada e formatada, com os 3 arquivos locais.
- ✅ Card criado/atualizado (número, status e rótulo).
- ✅ Commit/push (se autorizado) e card sincronizado.
- ⚠️ **Pendências** do grill (textos propostos, divergências do Figma, dúvidas técnicas), oferecendo resolvê-las em formulário.
- ✅ Próximo passo: gerar a especificação técnica com `/spec`.

## Checklist de qualidade

- [ ] Todas as perguntas foram feitas em formulários.
- [ ] Figma lido; link e 2 a 4 prints no bloco "🎨 Protótipo (Figma)" abaixo da seção 1.
- [ ] Cabeçalho `dependencies` no topo apontando o `.teste.md` e o `.grillme.md`.
- [ ] `.grillme.md` com decisões, rodada e pendências; `.teste.md` com matriz e seams.
- [ ] História, grill e testes coerentes; toda RN tem caso de teste.
- [ ] Perfis (Admin, Gestor, Operador) definidos.
- [ ] Card sem duplicata, com o mesmo conteúdo da história, imagens por URL raw, rótulo e status Backlog.
