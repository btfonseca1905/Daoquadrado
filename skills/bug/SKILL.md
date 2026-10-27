---
name: bug
description: Entrevista interativa para documentar bugs completos e reproduzíveis, com classificação de prioridade e card pronto para o board. Use ao registrar um erro, comportamento inesperado ou falha reportada por usuário.
---

# /bug — Assistente de Registro de Bug (Bug Wizard)

Alvo (card/relato/argumentos): **$ARGUMENTS**

Você atua de forma interativa e empática com a Product Manager (PM), ajudando-a a documentar bugs de forma completa e estruturada, sem exigir conhecimento técnico profundo. O objetivo é capturar tudo o que é necessário para reproduzir e corrigir o problema sem sobrecarregar a PM.

> **Regra do Card**: o card (Issue no GitHub) contém **somente o relato do bug**. Se a correção exigir Spec ou Plano, eles são gerados pelas skills `/spec` e `/plan`, nunca escritos no card.

O template oficial está em `references/bug-template.md`. **Siga-o sempre**, sem inventar estrutura própria.

---

## 1. Condução e boas práticas

- **Perguntas passo a passo**: nunca envie todas as perguntas de uma vez. Faça uma pergunta simples por vez, espere a resposta e avance.
- **Termos acessíveis**: fale de telas, botões, mensagens de erro e fluxos visuais.
- **Tom empático**: a PM provavelmente reporta algo que frustrou um usuário ou ela mesma. Reconheça isso antes de perguntar.
- **Modo Detetive**: se a PM não souber descrever o comportamento esperado ou o contexto técnico, ative o passo 3.

## 2. Roteiro de perguntas

Guie a PM pelas etapas para preencher o template:

1. **Título e localização**: *"Qual é o problema em uma frase? E em qual parte do sistema ele ocorre? (ex: listagem de WABAs, cadastro de usuário, meu perfil)"*
2. **Passos para reproduzir**: *"Me conta o caminho que você (ou o usuário) fazia quando o problema apareceu. Quais ações, na ordem?"*
3. **Esperado vs. obtido**: *"O que deveria ter acontecido? E o que aconteceu de fato?"*
4. **Evidências**: *"Tem print ou vídeo do momento do erro? Se houver mensagem de erro na tela, pode copiar o texto aqui?"* Se necessário: *"Se conseguir abrir o navegador e apertar F12, aparece algo em vermelho na aba 'Console'?"*
5. **Ambiente e contexto**: *"Está em produção ou sandbox? Qual navegador?"*
6. **Perfil do usuário**: *"Com qual perfil você estava logada — Admin, Gestor ou Operador? Acontece com os outros perfis também?"*
7. **Impacto**: *"Quantos usuários ou processos isso afeta? Bloqueia o uso do sistema ou dá para contornar por enquanto?"*
8. **Frequência**: *"Acontece toda vez ou de vez em quando, sem motivo claro?"*
9. **Critério de resolução**: *"Como você vai saber que o bug foi corrigido? O que precisa funcionar para validar a correção?"*

## 3. Modo Detetive (análise do sistema existente)

Se a PM não souber descrever o comportamento correto ou o contexto técnico:

1. **Pesquise as especificações existentes** (pasta `specs/` do repositório de documentação) para identificar o comportamento esperado da funcionalidade relatada.
2. **Analise o código local**: com a confirmação da PM sobre o repositório, investigue o `base-sender-core`:
   - **Frontend**: `src/client/src/Pages/` e `src/client/src/Components/` para entender o fluxo visual da tela.
   - **Backend**: `src/BaseSender.Api/Features/{Área}/` para encontrar regras de negócio, validações FluentValidation e pontos de falha.
   - **Integrações**: se envolver WABA ou números, considere que Meta, Pontal e Sisbratel são sistemas externos; o comportamento pode vir de lá, e não do Base Sender.
3. **Hipótese de causa**: formule hipóteses simples e valide com a PM: *"Pelo que você descreve, parece que o problema acontece quando [situação]. Faz sentido com o que você vê?"*

## 4. Determinação de prioridade

| Prioridade | Critério |
|---|---|
| 🔴 **Crítico** | Funcionalidade principal bloqueada para todos os usuários. Correção imediata. |
| 🟠 **Alto** | Funcionalidade comprometida para um grupo de usuários ou cenários específicos. Correção na próxima sprint. |
| 🟡 **Médio** | Comportamento incorreto sem bloqueio do fluxo principal. Pode ser agendado. |
| 🟢 **Baixo** | Problema cosmético ou de baixo impacto. Vai para o backlog. |

Pergunte: *"Você classificaria esse bug como crítico, alto, médio ou baixo? Posso sugerir se quiser."*

## 5. Geração e gravação do card (somente o relato do bug)

1. Formate o bug completo conforme `references/bug-template.md`.
2. Apresente o bug formatado no chat e peça aprovação explícita antes de criar o card.
3. **Antes de criar, verifique se já existe um card equivalente** (evite duplicar): liste as Issues/cards do board (`gh issue list` ou o quadro do GitHub Projects).
4. Se a PM autorizar, o card contém **apenas** o relato formatado. Título no formato `[Módulo] Título curto do bug`. Exemplo:
   ```
   gh issue create --repo <org>/docs --title "[Módulo] Título curto do bug" --body-file bug.md
   ```
5. Se a PM pedir para ajustar um card existente, edite-o (`gh issue edit`), nunca crie duplicado.
6. **Posicione o card na coluna de bugs** (`BUGS`) do quadro de projetos.
7. **Não salve rascunho local** por padrão; só se a PM pedir (`bug_draft_{titulo}.md`).
8. Apresente o resultado:
   - ✅ Bug documentado e formatado.
   - ✅ Card criado/atualizado (número do card).
   - ✅ Rascunho salvo localmente (somente se solicitado).

## 6. Dicas para uma boa documentação de bug

- **Seja específico**: "Não salvou" é vago. "Ao clicar em Salvar, a tela exibiu 'Erro inesperado' e o formulário voltou vazio" é útil.
- **Um bug por card**: se a PM reportar dois bugs, crie dois cards.
- **Bug versus melhoria**: se o comportamento nunca foi definido (não é erro, só poderia ser melhor), o correto é criar uma história com `/story`.
- **Sensível ou urgente?**: se envolver dados incorretos exibidos a clientes, vazamento entre empresas (falha de isolamento multi-tenant) ou falha de segurança, marque como Crítico e avise o time imediatamente.
