# Modelo de prompt para Lovable

Gerar um bloco completo independente do histórico da conversa:

```text
Crie [protótipo navegável / MVP funcional] para [nome].

CONTEXTO E OBJETIVO
[Problema, público, proposta de valor e resultado desejado.]

ESCOPO DO MVP
[Funcionalidades incluídas; itens explicitamente excluídos.]

ATORES E JORNADAS
[Quem utiliza, permissões, tarefas completas e exceções.]

TELAS E NAVEGAÇÃO
[Tela, componentes, CTA, validações, destino e estados vazio/erro/carregamento/sucesso.]

REGRAS DE NEGÓCIO
[Condições, cálculos, mensagens e critérios observáveis.]

DADOS E INTEGRAÇÕES
[Entidades e campos; persistência; autenticação, se pertinente; integrações autorizadas.]
[Sem backend definido: dados simulados rotulados, sem alegar integração real.]

DESIGN E EXPERIÊNCIA
[Referência visual fornecida, hierarquia, responsividade e acessibilidade.]

CRITÉRIOS DE ACEITE
[Checklist verificável do comportamento esperado.]

IMPLEMENTAÇÃO E LIMITES
[Ordem sugerida; dependências; hipóteses; funcionalidades que não devem ser criadas.]
```

- Se o usuário quiser apenas protótipo, não exigir pagamento, autenticação ou banco de dados reais.
- Se quiser produto funcional, explicitar dependências de serviços, credenciais e configurações.
- Não inventar endpoints, pesquisas, dados pessoais ou chaves.
- Preferir instruções específicas de comportamento a adjetivos visuais vagos.
