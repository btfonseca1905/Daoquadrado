---
name: spec
description: Elabora a especificação técnica (spec) de um card, Issue ou história, definindo o que será construído, interfaces, regras e critérios de aceite antes do plano de execução.
---

# /spec — Elaborar especificação técnica

Alvo (card/Issue/história/argumentos): **$ARGUMENTS**

## Processo

1. Leia o item em **$ARGUMENTS** por completo (descrição, critérios de aceite, comentários, links).
2. Explore o código e a documentação existentes para entender os padrões, módulos e contratos afetados. Não especifique no vazio.
3. Liste as lacunas e ambiguidades e resolva-as com o usuário, **uma pergunta por vez**. Não assuma respostas.
4. Quando houver mais de uma abordagem razoável, apresente 2–3 opções com trade-offs e recomende uma.
5. Redija a spec no formato abaixo, apresente por seções e peça aprovação. **Não implemente** nada nesta etapa.

## Formato de saída

```markdown
# Spec: <título>

## Objetivo
<O que muda e por quê, em poucas frases>

## Escopo
- Inclui: ...
- Não inclui: ...

## Comportamento esperado
<Regras de negócio, fluxos, estados, casos de borda, tratamento de erro>

## Design técnico
- Componentes/módulos afetados: ...
- Interfaces / contratos (APIs, eventos, schemas, dados): ...
- Decisões e alternativas descartadas: ...

## Critérios de aceite
- [ ] ...

## Estratégia de testes
<O que testar, em quais níveis, dados necessários>

## Riscos e dependências
...

## Perguntas em aberto
...
```

## Qualidade

- Cada critério de aceite do item original deve estar coberto pela spec.
- Seja específico o bastante para que outra pessoa monte o plano sem adivinhar.
- Registre decisões e o motivo; o que não foi decidido fica em "Perguntas em aberto".
