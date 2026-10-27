# 📝 Template de História / Card de Feature (Padrão para PM) — v2

Este documento define o modelo estruturado para a criação de histórias de usuário (User Stories) no ecossistema do Base Sender. Ele permite que a Product Manager (PM) descreva regras e fluxos funcionais sem jargão técnico, oferecendo ao desenvolvedor ou agente de IA o contexto necessário para mapeamento e desenvolvimento seguros.

> 🆕 **v2**: a história começa com o **cabeçalho de dependência** (grill-me e testes) e traz, logo abaixo da seção 1, o bloco **🎨 Protótipo (Figma)** com link e prints.

---

## 🎯 Estrutura da História (Copiar e Preencher)

```
---
dependencies:["<n> [Módulo] Nome.teste.md", "<n> [Módulo] Nome.grillme.md"]
---
```

# 🚀 [Módulo/Área] Nome Curto e Claro da Feature

**Eu, como** [perfil do usuário — Admin, Gestor ou Operador],  
**quero** [ação ou funcionalidade desejada — ex: adicionar um número novo a uma WABA],  
**para que** [benefício ou valor de negócio — ex: a operação tenha mais números ativos para disparo].

---

### 1. 💼 Contexto de Negócio (O Porquê)
[Explique em termos simples qual problema esta funcionalidade resolve, por que ela é importante para a empresa e qual o perfil do usuário final.]
*Exemplo: Hoje o vínculo da WABA é feito colando o ID manualmente no sistema depois de concluir o embed em um link externo da Pontal — processo sujeito a erro, que deixa a WABA quebrada quando as etapas saem fora de ordem.*

### 🎨 Protótipo (Figma)

🔗 [Descrição do frame 1](link-do-figma-node-id=...&m=dev) · 🔗 [Descrição do frame 2](link-do-figma)

![Legenda curta do print 1](imagens/assunto-estado.png)
*1. Legenda numerada explicando o que o print mostra (textos, botões, estados).*

![Legenda curta do print 2](imagens/assunto-outro-estado.png)
*2. Legenda numerada do segundo print.*

*(de 2 a 4 prints; sem Figma, informe e use o print enviado pela PM)*

---

### 2. 🖥️ Fluxo de Funcionamento (O Quê)
[Descreva o comportamento visual e a sequência de ações que o usuário realiza na interface.]
*   **Acesso**: Onde essa tela fica no menu? (ex: "WABAs > Detalhes da WABA > aba Números").
*   **Perfil**: quais dos três perfis executam esta ação — Admin, Gestor, Operador? O comportamento muda entre eles?
*   **Comportamento passo a passo**:
    *   *Passo 1*: O usuário acessa a tela X.
    *   *Passo 2*: Clica no botão "Adicionar número".
    *   *Passo 3*: O sistema exibe o formulário.
    *   *Passo 4*: Ao clicar em "Continuar", o sistema registra e exibe a confirmação.

[Opcional: um fluxograma em bloco ```mermaid, gravado direto no corpo.]

---

### 3. 📊 Campos e Dados Envolvidos (Os Dados)
[Se a funcionalidade exigir que o usuário digite dados, selecione opções ou visualize novas colunas, descreva-os aqui.]
*   **Campo "Nome de exibição"** (texto, obrigatório, máx. 100 caracteres com contador).
*   **Campo "DDD"** (seleção única, obrigatório).
*   **Campo "Status"** (somente leitura, vem da integração).

---

### 4. 🛑 Regras de Negócio e Restrições (Os Limites)
[Defina o que é permitido e o que é proibido nas ações do usuário. Cada regra deve ser verificável.]
*   **RN01**: [Regra] — ex: um número só pode estar vinculado a uma WABA em todo o sistema.
*   **RN02**: [Regra de perfil] — ex: ação restrita a Admin; o botão fica oculto para os demais, e a permissão também é validada no backend.

---

### 5. 🚨 Cenários de Erro e Exceções
[Explique como o sistema deve reagir se algo der errado ou se o usuário realizar uma ação inválida.]
*   **Caso de Erro 1**: Se o número já estiver cadastrado, exiba: *"Não foi possível adicionar este número, tente outro."* (sem revelar em qual conta ele está em uso).
*   **Caso de Erro 2**: Se houver falha na integração, exiba: *"Falha ao conectar. Tente novamente."* e permita nova tentativa.

---

### 🧪 6. Critérios de Aceite (BDD - Gherkin)
[Descreva cenários de testes reais passo a passo usando a lógica Dado / Quando / Então.]

#### Cenário 1: Ação concluída com sucesso
*   **Dado** que o usuário (perfil X) está na tela Y.
*   **Quando** ele preenche todos os campos obrigatórios com valores válidos e confirma.
*   **Então** o sistema registra o dado e exibe a mensagem de confirmação: *"Tudo pronto!"*.

#### Cenário 2: Bloqueio de campo obrigatório ausente
*   **Dado** que o usuário está no formulário.
*   **Quando** ele deixa o campo "Nome de exibição" vazio e tenta continuar.
*   **Então** o sistema impede a submissão, sinaliza o campo e exibe: *"Preenchimento obrigatório"*.

#### Cenário 3: Perfil sem permissão
*   **Dado** que o usuário logado tem o perfil Operador.
*   **Quando** ele acessa a tela.
*   **Então** a ação não é exibida, e uma chamada direta ao endpoint é rejeitada pelo backend.

---

## 📎 Arquivos que acompanham a história
- **`<n> <título>.grillme.md`**: decisões da entrevista grill-me, rodada de perguntas e respostas (com a regra gerada) e pendências.
- **`<n> <título>.teste.md`**: matriz de rastreabilidade, casos de teste por seam, com prioridade e referência às regras.
- **`imagens/`**: os prints do protótipo citados no bloco 🎨 Protótipo (Figma).
