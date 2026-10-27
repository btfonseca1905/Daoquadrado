# 🐛 Template de Bug Report

Este documento define o modelo estruturado para a criação de relatórios de bug no ecossistema Base Sender. Ele permite que a Product Manager (PM) descreva um problema de forma clara e completa, fornecendo ao desenvolvedor ou agente de IA o contexto necessário para reprodução e correção segura.

---

## 🎯 Estrutura do Bug (Copiar e Preencher)

# 🐛 [Módulo/Área] Título Curto e Claro do Problema

**Tela afetada:** [ex: Listagem de WABAs / Detalhes da WABA / Cadastro de Usuário / Meu Perfil]  
**Ambiente:** [ex: Produção / Sandbox / Desenvolvimento local]  
**Prioridade:** [Crítico / Alto / Médio / Baixo]  
**Perfil do usuário afetado:** [Admin / Gestor / Operador]

---

### 1. 📋 Descrição do Problema (O Que Está Acontecendo)
[Descreva em linguagem simples o comportamento incorreto que está sendo observado. Evite jargões técnicos.]

*Exemplo: Ao clicar em "Sincronizar agora" na tela de detalhes da WABA, o botão fica girando indefinidamente e a data de sincronização não é atualizada.*

---

### 2. 🔁 Passos para Reproduzir (Como Fazer Acontecer)
[Liste os passos exatos que levam ao comportamento incorreto. Quanto mais detalhado, mais rápido será a correção.]

1. Faça login com um usuário de perfil **[Admin / Gestor / Operador]**.
2. Acesse a tela **[nome da tela]**.
3. [Passo 3 — ex: Clique na WABA "WABA 1"]
4. [Passo 4 — ex: Clique no botão "Sincronizar agora"]
5. **Resultado obtido:** [ex: O botão permanece no estado "Sincronizando" e nada muda na tela]

---

### 3. ✅ Comportamento Esperado (O Que Deveria Acontecer)
[Descreva o que o sistema deveria fazer se estivesse funcionando corretamente.]

*Exemplo: O botão deveria passar por "Sincronizando" → "Sincronizado" → "Sincronizar · MM:SS", e o campo "Sincronizado em" deveria exibir a data e hora atuais.*

---

### 4. 📸 Evidências (Prints / Vídeos / Logs)
[Adicione capturas de tela, gravações de tela ou mensagens de erro que comprovem o problema.]

- [ ] Print da tela com o erro visível
- [ ] Vídeo de reprodução (se o problema for intermitente ou difícil de capturar em print)
- [ ] Mensagem de erro copiada da tela ou do console do navegador (F12 → Aba Console)
- [ ] Aba Network (F12) com a requisição que falhou, se houver

```
[Cole aqui qualquer mensagem de erro copiada do console ou da tela]
```

---

### 5. 🌍 Contexto e Ambiente
[Preencha as informações de ambiente que podem influenciar o bug.]

| Campo | Valor |
|---|---|
| Ambiente | [Produção / Sandbox] |
| Navegador | [ex: Chrome 125 / Firefox 126 / Edge] |
| Sistema Operacional | [ex: Windows 11 / macOS 14] |
| URL da tela com problema | [ex: /wabas/12565849879122] |
| Usuário de teste usado | [ex: fulano@empresa.com — NÃO coloque senha] |
| Perfil do usuário | [Admin / Gestor / Operador] |
| Empresa (tenant) | [se o problema parecer específico de uma empresa] |
| Horário aproximado | [ex: 14h30 do dia 19/09/2026] |

---

### 6. 💥 Impacto no Negócio (Qual a Urgência)
[Explique o impacto prático desse bug para a operação do negócio.]

*Exemplos de impacto:*
- 🔴 **Crítico**: O bug impede totalmente o uso de uma funcionalidade principal, ou expõe dados de uma empresa para outra (falha de isolamento multi-tenant).
- 🟠 **Alto**: A funcionalidade está comprometida para alguns usuários ou cenários específicos, gerando retrabalho.
- 🟡 **Médio**: O sistema funciona, mas com comportamento incorreto ou visual inadequado, sem bloquear o fluxo principal.
- 🟢 **Baixo**: Problema cosmético ou de baixo impacto, sem prejuízo funcional.

**Impacto descrito:** [ex: Nenhum gestor consegue sincronizar WABAs. O suporte recebeu 3 relatos hoje.]

---

### 7. 🔄 Frequência e Reprodutibilidade
[O bug acontece sempre ou de forma intermitente?]

- [ ] **Sempre** — acontece toda vez que os passos são seguidos
- [ ] **Frequente** — acontece na maioria das tentativas
- [ ] **Intermitente** — acontece às vezes, sem padrão claro
- [ ] **Uma vez** — aconteceu uma vez e não consegui reproduzir

**Observações:** [ex: Parece acontecer apenas em WABAs com mais de 3 números]

---

### 8. 🧪 Critérios de Aceite da Correção (Como Saberemos que Está Resolvido)
[Descreva como o QA ou a PM vai validar que o bug foi corrigido.]

#### Cenário de Validação:
- **Dado** que o usuário está em [tela/módulo] e realiza [ação que causava o bug].
- **Quando** a correção for aplicada.
- **Então** [comportamento esperado correto deve ocorrer, sem o erro anterior].

*Exemplo:*
- **Dado** que o gestor está na tela de Detalhes da WABA.
- **Quando** ele clica em "Sincronizar agora".
- **Então** o botão percorre os 4 estados e o campo "Sincronizado em" exibe a data e hora atuais.

---

### 9. 📎 Informações Adicionais (Opcional)
[Qualquer contexto extra que possa ajudar: mudanças recentes no sistema, deploy novo, comparação com o ambiente sandbox, se envolve integração externa, etc.]

*Exemplo: O problema começou após o deploy de ontem às 18h. Em sandbox o comportamento está correto. Pode estar relacionado à integração com a Pontal.*
