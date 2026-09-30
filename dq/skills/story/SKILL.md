---
name: story
description: Entrevista interativa para criar histórias de usuário bem estruturadas, com critérios de aceite. Use ao transformar uma ideia, demanda ou card em uma história pronta para desenvolvimento.
---

# /story — Criar história de usuário

Alvo (card/Issue/ideia/argumentos): **$ARGUMENTS**

## Processo

1. Se houver um card, Issue ou documento em **$ARGUMENTS**, leia-o antes de perguntar qualquer coisa. Não pergunte o que já está escrito lá.
2. Entreviste o usuário **uma pergunta por vez**, preferindo múltipla escolha quando possível. Cubra:
   - **Quem**: persona/papel que se beneficia.
   - **O quê**: a capacidade desejada.
   - **Por quê**: o valor ou problema resolvido.
   - **Contexto**: fluxo atual, restrições, dependências, o que está fora de escopo.
3. Resuma o entendimento em 2–3 frases e peça confirmação antes de redigir.
4. Redija a história no formato abaixo e peça revisão. Ajuste até o usuário aprovar.

## Formato de saída

```markdown
# <Título curto e orientado a valor>

**Como** <persona>, **quero** <capacidade>, **para** <benefício>.

## Contexto
<Problema, cenário atual, links relevantes>

## Critérios de aceite
- [ ] Dado <contexto>, quando <ação>, então <resultado observável>
- [ ] ...

## Fora de escopo
- ...

## Perguntas em aberto
- ...
```

## Qualidade

- A história deve ser pequena o bastante para ser entregue em uma iteração; se não for, proponha dividi-la.
- Cada critério de aceite precisa ser verificável (sem "rápido" ou "amigável" sem métrica).
- Não invente requisitos: o que for incerto vai em "Perguntas em aberto".
- Salve/publique o resultado onde o usuário indicar (arquivo, Issue, card). Se não indicou, pergunte.
