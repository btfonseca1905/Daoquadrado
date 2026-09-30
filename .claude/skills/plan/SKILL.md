---
name: plan
description: Cria o plano de execução técnico de um card. Segue o workflow oficial e sempre atualizado do MCP gf7-delivery-mcp.
---

<!-- gerado-por: skills/SETUP.md (gf7-delivery-mcp) — atalho fino, seguro para sobrescrever em atualizações -->

# /plan — Cria o plano de execução técnico de um card

Alvo (card/Issue/argumentos): **$ARGUMENTS**

## Instruções obrigatórias

1. Chame a tool do MCP para carregar o workflow oficial **agora**:
   `mcp__gf7-delivery-mcp__tool_read_knowledge_document(filepath="workflows/create_plan_workflow.md")`
2. O documento retornado é a **única fonte da verdade** deste comando. Siga os passos dele na ordem exata, aplicando **$ARGUMENTS** onde o workflow referenciar o card/Issue alvo.
3. **Nunca** use uma versão em cache, resumida ou lembrada deste workflow — ele é atualizado com frequência no MCP e só a leitura no momento da invocação garante a versão vigente.
4. Se a chamada da tool falhar (MCP desconectado, sem permissão, arquivo inexistente), informe o erro ao usuário e pare — não improvise um processo alternativo.
