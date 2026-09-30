---
name: execute
description: Executa a implementação de um plano técnico aprovado, tarefa por tarefa, verificando cada passo com testes antes de declarar conclusão.
---

# /execute — Executar plano aprovado

Alvo (card/Issue/plano/argumentos): **$ARGUMENTS**

## Processo

1. Leia o plano (e a spec) em **$ARGUMENTS**. Se não houver plano aprovado, pare e sugira rodar `/plan`.
2. Crie uma lista de tarefas a partir do plano e trabalhe **uma por vez**, na ordem.
3. Para cada tarefa:
   - Implemente exatamente o que o plano descreve, seguindo os padrões do código existente.
   - Rode a verificação definida (teste, build, lint) e leia a saída real.
   - Só marque a tarefa como concluída se a verificação passar.
4. Se algo no plano se mostrar errado ou incompleto, **pare e informe** o usuário com a evidência; não improvise mudanças de escopo em silêncio.
5. Ao terminar, rode a suíte de testes relevante e confirme cada critério de aceite.

## Regras

- Faça apenas o que o plano pede; sugestões extras vão para o relatório final, não para o código.
- Não faça commit, push ou ações externas sem o usuário ter pedido.
- Relate resultados com fidelidade: se um teste falhou ou uma etapa foi pulada, diga isso com a saída.

## Relatório final

- O que foi implementado (por tarefa).
- Saída dos testes/verificações executados.
- Desvios do plano e o motivo.
- Pendências e pontos de atenção.
