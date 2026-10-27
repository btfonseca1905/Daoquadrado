# Rastreabilidade e cuidados ao usar a planilha

O catálogo `catalogo-metricas.md` transcreve as células da fonte original sem normalizar fórmulas. Por isso, **uma fórmula registrada não é automaticamente uma fórmula validada**.

## Procedimento

1. Encontre a métrica pelo nome, sinônimo ou sigla no catálogo.
2. Registre a **aba e a linha** correspondente.
3. Leia a função da métrica e o campo “Como medir” antes de formular o cálculo.
4. Identifique unidade, evento, período e população elegível. Não atribua a um dado inexistente uma origem no Excel.
5. Se a planilha trouxer uma descrição, não uma operação, faça uma **proposta de operacionalização** claramente identificada e ancorada na necessidade do produto.
6. Se uma fórmula literal divergir da definição da métrica, informe o problema e peça validação somente se impedir o cálculo. Para recomendações não bloqueadas, apresente a proposta e siga a etapa.

## Alertas já identificados no arquivo recebido

- **Taxa de conversão por etapa do funil**, em `Métricas de Produto!9`, `Métricas de Marketing!8` e `Métricas de Negócio!27`: o campo “Como medir” divide usuários da etapa 1 por usuários da etapa 2. Para medir conversão **da etapa 1 para a etapa 2**, a proposta coerente é `(usuários que chegaram à etapa 2 / usuários elegíveis na etapa 1) × 100`. Identifique como **correção proposta**, não como fórmula literal do Excel.
- **Taxa de ativação**, em `Métricas de Produto!15` e `!74`: “% de usuários que experimentaram a proposta de valor” é uma definição, não uma operação completa. Proponha `(usuários elegíveis que realizaram o evento de ativação / usuários elegíveis) × 100`, definindo previamente o evento de valor e o período.
- **Taxa de engajamento**, em `Métricas de Produto!19`: a própria fonte informa que depende do produto, com exemplos de eventos. Defina um evento de valor específico e a métrica adequada, como frequência média por usuário engajado ou percentual de ativos que realizou o evento. Rotule a operação como proposta.
- **Customer Effort Score**, em `Métricas de Produto!58`, usa “emoticons referentes ao esforço” e não uma fórmula. A aba `Métricas de UX!25` apresenta uma média ponderada por notas de 1 a 5. Use a versão de UX quando houver pesquisa numérica; explique a escala e o sentido de uma boa nota.
- **Taxa de retenção**, em `Métricas de Produto!20` e `!72` e `Métricas de Negócio!29`, é descrita como retenção de clientes. Se o produto usar comportamento de usuários, cohorts ou contas B2B, redefina explicitamente população inicial, retorno e janela antes de calcular. Não trate churn e retenção como inversos automáticos em bases diferentes.
- **Usuários ativos**, em `Métricas de Produto!18` e `!53`, remete a DAU/WAU/MAU e não constitui divisão matemática. Reporte contagem de usuários únicos que fizeram um evento qualificado por dia, semana ou mês, indicando a escolha de atividade. Se calcular razão DAU/MAU, rotule-a como métrica derivada.
- **Sucesso na tarefa**, em `Métricas de UX!3` e `Métricas de Produto!31`, usa sucessos divididos por tentativas. Especifique se múltiplas tentativas da mesma pessoa contam separadamente.
- **Tempo de tarefa**, em `Métricas de UX!4`, utiliza soma de tempos sobre total de usuários. Defina como tratar abandonos, tentativas repetidas e casos sem sucesso antes de calcular a média.

## Regras de apresentação

- Fórmula em português e com termos definidos.
- Percentual deve indicar `× 100` quando a operação produzir proporção.
- Não inventar metas, benchmarks, resultados ou números reais. Em preview de imagem, todos os números fictícios devem ser identificados como simulados.
- Não usar ferramentas de busca ou referências externas. A base de conhecimento local e as informações do usuário são as únicas fontes da Skill.
