---
name: generate-personas
description: Generate a diverse set of synthetic user personas for your product — typed primary/secondary/tertiary/negative, mix on request — saved as markdown files ready for interviews and critiques
argument-hint: "[count, mix and/or focus, e.g. '2 primary, 1 tertiary, 1 negative for the B2B segment']"
disable-model-invocation: true
---

# /generate-personas

Atenção!
Faça um Passo de cada vez, e dentro de cada Passo, faça uma pergunta por vez.

## Workflow

1. **Apresente o contexto do projeto** 
Comece explicando para o Agente o que você está desenvolvendo. Não é necessário preencher um formulário perfeito; você pode descrever o projeto naturalmente.
Por exemplo:
Estou desenvolvendo uma plataforma de gestão financeira para pequenos empresários. O público principal são donos de pequenas empresas com pouco conhecimento financeiro. Estamos na fase de protótipo e queremos entender quais funcionalidades seriam mais importantes para esse público.
O Agente procurará entender principalmente: setor de atuação, público-alvo, problema que o projeto pretende resolver, objetivos, estágio atual do projeto, aprendizados já obtidos e próximos passos.
Quanto mais contexto você fornecer, mais consistente será a persona criada.

2. **Complete as informações que estiverem faltando** 
Depois da descrição inicial, o Agente pode aprofundar aspectos importantes do projeto.
Por exemplo, ele pode explorar questões como:
Quem exatamente você quer representar com a persona?
A pessoa já utiliza alguma solução concorrente?
Qual problema ela enfrenta atualmente?
Quem participa da decisão de compra?
Existe algum recorte específico de idade, profissão, renda ou localização?
O produto é B2B ou B2C?
Você não precisa necessariamente conhecer todas as respostas. Quando algum dado não existir, pode informar que se trata de uma hipótese a ser explorada.
Essa distinção é importante: uma persona sintética é especialmente útil para formular hipóteses, mas não substitui entrevistas ou pesquisas com usuários reais.

3. **Solicite a criação da persona** 
Depois que houver contexto suficiente, peça algo como:
Crie uma persona sintética representando meu público principal.
O Agente estruturará a persona considerando dimensões como dados demográficos, profissão, renda, localização, características psicográficas, valores, estilo de vida, objetivos, dores, frustrações, comportamento de compra, uso de tecnologia, redes sociais, jornada de decisão, motivadores, medos e mapa de empatia.
A persona também pode incluir uma pequena narrativa para tornar o perfil mais concreto.

4. **Revise a persona criada** 
Leia o perfil e verifique se ele faz sentido para o projeto.
Você pode corrigir qualquer hipótese. Por exemplo:
A renda está muito alta. Esse público normalmente ganha entre R$ 4 mil e R$ 7 mil.
Ou:
Essa persona parece muito confortável com tecnologia. Quero representar alguém que tenha dificuldade com ferramentas digitais.
Ou ainda:
Crie uma versão mais conservadora dessa persona.
O Agente pode então recalibrar o perfil.

5. **Salve** 
O  Agente deve criar um perfil da persona pronto para ser copiado e criado um arquivo .md
