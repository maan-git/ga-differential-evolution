# Confidence e Fallback de Entidades e Classificações

cada uma das pipelines irá reportar uma pontuação de `confidence` juntamente com a classe ou entidade prevista.

Você pode usar a pontuação de confiança pra escolher quando ignorar a previsão do Softcore e acionar o comportamente de fallback, por exemplo, pedindo ao usuário para informar/preencher o campo faltante e/ou formular o `input` de outra forma.

## Escolhendo um corte de confiança

Uma boa maneira de escolher um corte de confiança é calcular a confiança de do modelo em um conjunto de testes e comparar os valores de confiança nos exemplos previstos corretamente e incorretamente.

## Uma nota sobre pontuações de confiança (`confidence`)

Tenha sempre em mente que a pontuação de confiança não é uma probabilidade real de que a previsão esteja correta, é apenas uma métrica definida pelo modelo que descreve aproximadamente o quão similar sua entrada foi dos dados de treinamento.

Um classificador de texto que utiliza `pre-trained embeddings`, por exemplo, geralmente informa números de confiança muito baixos, enquanto um modelo utilizando `supervised embeddings` fornece confidência muito altas. Um equivoco comum é que, se seu modelo relata alta confiança em seus exemplo de treinamento, é um modelo **"melhor"**. Na verdade, isso geralmente significa que seu modelo está super adaptado ([Overfitting](https://en.wikipedia.org/wiki/Overfitting)).