# Perguntas Frequents (FAQ)

## Quais idiomas o Softcore suporta ?

O Softcore pode ser usado para entender qualquer idioma que possa ser tokenizado (em espaços em branco ou usando um tokenizador personalizado), mas alguns backends (pipelines) estão restritas a idiomas especificos.

Você pode ler mais sobre os idiomas suportados pelo Softcore em [Suporte ao Idioma](link).

## Quantos exemplos de treinamento eu preciso ?

Infelizmente, a resposta é que *depende*.

Um bom ponto de partida é ter 10 exemplos para cada classe e construir a partir daí.

Se você tiver classe que sejam facilmente confundidas (intersecção), precisará de mais dados de treinamento. Assim à medida que você adiciona mais classes, mais exemplos de treino será necessário.

O mesmo vale para entidades, o numero de exemplos de treinamento que você precisará depende de quão estreitamente relacionados são os diferentes tipos de entidade e de como as entidades são claramente distinguíveis de não entidades em seu cado de uso.

Para avaliar o desempenho de seu modelo, uso o [script de avaliação](link).

## Qual versão do Softcore estou rodando ?

Para descobrir qual versão do Softcore está executando, você pode executar.

```bash
python -c "differential_evolution_GA"
```

## Por que estou recebendo um `UndefinedMetricWarning` ?

A advertência completa é: O aviso é resultado da falta de dados de treinamento. Durante o treinamento, o conjunto de dados será dividido em várias partes, se houver poucas amostras de treinamento para qualquer uma das classes, a divisão poderá resultar em divisões que não contenham nenhum exemplo para essa `classes. UndefinedMetricWarning: F-score is ill-defined and being set to 0.0 in labels with no predicted samples.`

Por isso, a solução é adicionar mais amostras de treinamento. Como isso é apenas um aviso, o treinamento ainda será bem sucedido, mas as precisões dos modelos resultantes podem ser fracas quando você não tiver dados de treinamento suficientes.

## Ele é executado em Python 3 ?

Sim, o Softcore suporta o Python 3.5, 3.6 e 3.7. Se houver algum problema com uma versão específica do Python, sinta-se à vontade para criar uma `Issue` ou fornecer uma correção diretamente.
