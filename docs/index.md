# Softcore

<img align="right" height="180" src="/assets/img/iconfinder_Dragon_Egg_2913098.png">

## Processos simplificados

Softcore é uma ferramenta que possibilita a implementação e consumo de processos de entendimento de linguagem natural, de forma rápida e prática.

Por exemplo, como treinar e consumir um modelo de extração de entidade nomeada:

``` python
from softcore.training_data import load_data
from softcore.model import Trainer
from softcore import config

training_data = load_data("./caminho/dos/seus/dados/de/treino.json")
trainer = Trainer(config.load("arquivo/de/configuração.yaml"))

# treinamento
interpreter = trainer.train(training_data)

# persistencia
trainer.persist("./modelos")

#consumo
interpreter.parser("texto")

```

## Sobre

Você deve pensar no Softcore como um conjunto de APIs de alto nível para construir seu próprio modelo utilizando bibliotecas NLP e ML existentes. O processo de configuração é projetado para ser o mais simples possível.

Softcore é escrito em Python, mas você pode usá-lo de qualquer linguagem usando o Softcore como um servidor HTTP. Se seu projeto está sendo desenvolvido em Python, você pode simplesmente importar as classes relevantes.

## Começando

* Instalação
* Tutorial: Extraindo entidades nomeadas de documentos jurídicos (médio)
