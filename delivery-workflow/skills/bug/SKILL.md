---
name: bug
description: Entrevista interativa para documentar bugs completos e reproduzíveis. Use quando o usuário relatar um defeito e precisar de um registro claro para investigação ou correção.
---

# /bug — Documentar bug reproduzível

Alvo (card/Issue/descrição/argumentos): **$ARGUMENTS**

## Processo

1. Leia o que já existe em **$ARGUMENTS** (Issue, card, log, descrição) e, se útil, o código/logs relacionados. Não repita perguntas já respondidas.
2. Entreviste o usuário **uma pergunta por vez** até ter:
   - **Resumo**: uma frase do que está errado.
   - **Passos para reproduzir**: numerados, determinísticos, a partir de um estado inicial conhecido.
   - **Resultado esperado** vs. **resultado atual**.
   - **Ambiente**: versão, SO/navegador, configuração, dados relevantes.
   - **Frequência**: sempre, intermitente, somente em certas condições.
   - **Evidências**: mensagens de erro, stack traces, logs, capturas de tela.
   - **Impacto**: quem é afetado e a gravidade (bloqueante, alta, média, baixa).
   - **Regressão**: quando começou a ocorrer / última versão que funcionava, se conhecido.
3. Se possível, tente reproduzir o bug você mesmo e registre o resultado.
4. Redija o relatório no formato abaixo e peça confirmação.

## Formato de saída

```markdown
# [Bug] <resumo curto>

**Gravidade:** <bloqueante|alta|média|baixa>  **Frequência:** <...>

## Passos para reproduzir
1. ...

## Resultado esperado
...

## Resultado atual
...

## Ambiente
...

## Evidências
...

## Hipóteses / notas de investigação
<Somente o que for sustentado por evidências; marque suposições como tal>
```

## Qualidade

- Um terceiro deve conseguir reproduzir apenas lendo o relatório.
- Separe fato de hipótese. Não proponha correção sem evidência; se propuser, marque como hipótese.
- Um relatório = um bug. Se surgirem outros problemas, sugira relatórios separados.
