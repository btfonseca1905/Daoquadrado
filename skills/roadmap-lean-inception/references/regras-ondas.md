# Regras obrigatórias das ondas

Uma **onda** é um conjunto de épicos entregue antes da onda seguinte. A validação é independente de quarters.

1. **Quantidade:** de 1 a 3 épicos por onda.
2. **Confiança vermelha:** no máximo 1 épico Vermelho por onda.
3. **Três itens de baixa/média confiança:** uma onda com 3 épicos não pode ter todos apenas Amarelos ou Vermelhos; deve incluir ao menos um Verde.
4. **Esforço técnico:** soma dos esforços (1, 2 ou 3) não pode ultrapassar 5.
5. **Valor mínimo:** soma da importância para o Negócio **>= 4** e soma da importância para o Usuário **>= 4**, separadamente, em cada onda.
6. **Dependência:** se B depende de A, `onda(B) > onda(A)`.

Em qualquer tabela, usar `VU` para valor de usuário, `VN` para valor de negócio e `ET` para esforço técnico.

## Atenção à viabilidade

Um épico isolado nunca consegue atingir sozinho a regra 5, pois cada nota é no máximo 3. Portanto, com estas regras, uma onda de um item é **sempre inviável**. Em geral, os épicos precisam formar pares ou trios compatíveis. Listas com número de épicos que não permite essa composição e cadeias longas de dependências podem não ter solução.

Não relaxar a soma mínima nem forçar uma onda inválida. Reportar a incompatibilidade e solicitar decisão do PM.

## Exemplo de entrada do script

```json
{
  "epicos": [
    {"id": "E01", "usuario": 3, "negocio": 3, "esforco": 2, "confianca": "verde", "depende_de": []},
    {"id": "E02", "usuario": 2, "negocio": 2, "esforco": 2, "confianca": "amarelo", "depende_de": []},
    {"id": "E03", "usuario": 3, "negocio": 3, "esforco": 1, "confianca": "verde", "depende_de": ["E01"]},
    {"id": "E04", "usuario": 2, "negocio": 2, "esforco": 2, "confianca": "amarelo", "depende_de": []}
  ]
}
```

O script lê o JSON e retorna ondas e totais. Se nenhuma solução satisfizer as regras, retorna um erro estruturado. Use saída do script como apoio de verificação, mantendo o julgamento de priorização transparente.
