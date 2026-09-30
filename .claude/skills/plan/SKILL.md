---
name: plan
description: Cria o plano de execução técnico de um card, Issue ou spec, dividido em tarefas pequenas, ordenadas e verificáveis. Use antes de implementar.
---

# /plan — Criar plano de execução

Alvo (card/Issue/spec/argumentos): **$ARGUMENTS**

## Processo

1. Leia o item e a spec associada em **$ARGUMENTS**. Se não houver spec e a mudança for não trivial, sugira rodar `/spec` primeiro.
2. Explore o código para identificar arquivos, funções, testes e padrões que serão tocados. Cite caminhos reais.
3. Quebre o trabalho em tarefas **pequenas** (idealmente de 2 a 15 minutos cada), ordenadas por dependência, cada uma com resultado verificável.
4. Planeje testes junto de cada tarefa (teste primeiro quando fizer sentido).
5. Apresente o plano ao usuário e ajuste até a aprovação. **Não implemente** nesta etapa.

## Formato de saída

```markdown
# Plano: <título>

## Resumo
<Abordagem em 2–4 frases>

## Arquivos afetados
- `caminho/arquivo` — o que muda

## Tarefas
1. **<Tarefa>**
   - Arquivos: ...
   - Passos: ...
   - Verificação: <comando ou teste e resultado esperado>
2. ...

## Testes
...

## Riscos e mitigação
...

## Definição de pronto
- [ ] Critérios de aceite atendidos
- [ ] Testes passando
- [ ] ...
```

## Qualidade

- Sem placeholders vagos ("tratar erros", "ajustar depois"): diga exatamente o quê.
- Cada tarefa deve poder ser concluída e verificada isoladamente.
- Inclua como reverter ou mitigar se a mudança for arriscada (migração, dados, API pública).
