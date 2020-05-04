# Configuração dos Componentes

!!! Nota
    Está é uma referência das opções de configurações de cada componente integrado no Softcore. Se você deseja criar um componente personalizado, confira a seção "**[Componentes Personalizados](/develop_docs/custom_components/)**"

----------

<img align="right" height="180" src="/assets/img/iconfinder_Potion_2913113.png">

## Componentes

* [SpacyNLP](#spacynlp)
* [RegexFeaturizer](#regexfeaturizer)
* [MorphFeaturizer](#morphfeaturizer)
* [CRFEntityExtrator](#crfentityextrator)

----------

### SpacyNLP

**Resumo**: Inicializador de linguagem Spacy

**Saída**: nenhuma

**Descrição**: Inicializa o framework Spacy. Todos os componentes que utilizam Spacy dependem deste, portanto, este deve ser colocado no início de cada pipeline que usa componentes baseados no Spacy

**Configurações**: nenhuma

----------

### RegexFeaturizer

**Resumo**: Extração/Criação de features através de regex.

**Saída**: `text_features` e `tokens.pattern`

**Descrição**: Durante o treinamento, o `ComponentBuilder` cria uma lista de expressões regulares (regex) definidas no dados de treinado, podendo ser diretamente `expressões regulares` ou `lookup tables`. Para cada regex, uma feature será definida marcando se esta expressão foi encontrada no dado de entrada, que será posteriormente inserira no classificador de texto/extrator de entidade para simplificar a classificação.

!!! Nota
    Na pipeline, deve ser definido um tokenizador no passo anterior a este.

**Configurações**: nenhuma.

----------

### MorphFeaturizer

**Resumo**: Extração/Criação de features através de uma tabela morfológica.

**Saída**: `text_features`

**Descrição**: 

!!! Nota
    Na pipeline, deve ser definido um tokenizador no passo anterior a este.

**Configurações**: nenhuma.

----------

### CRFEntityExtrator

**Resumo**: Extração de entidade CRF

**Saída**: acrescenta `entities`

**Exemplo de saída**:
```python
{
    "entities": [
        {
            "value":"Florianópolis",
            "start": 20,
            "end": 33,
            "entity": "city",
            "confidence": 0.874,
            "extractor": "CRFEntityExtractor"
        }
    ]
}
```

**Descrição**:  Este componente implementa CRF (campos aleatórios condicionais) para fazer o reconhecimento de entidades nomeadas. Os CRFs podem ser considerados como uma cadeia e Markov não direcionada, onde os passos de tempo são palavras e os estados são classes de entidade. Recursos das palavras (letras maiúsculas, marcações POS, etc.) fornecem probabilidades para certas classes de entidade, assim como as transições entre tags ded entidades vizinhas: o conjunto mais provável de tags é então calculado e retornado. Se os recursos do POS forem usados (pos ou pos2), um componente que faça a extração das features será necessário (spaCy, nltk, etc).

!!! Nota
    Na pipeline, deve ser definido um tokenizador no passo anterior a este.

**Configurações**: 
```yaml
pipeline:
    - name: "CRFEntityExtractor"
      # As features (recursos) são um array `[antes, palavra, após]`
      # Funcionalidades disponíveis:
      # ``low``, ``title``, ``suffix5``, ``suffix3``, ``suffix2``,
      # ``suffix1``, ``pos``, ``pos2``, ``prefix5``, ``prefix2``,
      # ``bias``, ``upper`` e ``digit``
      features: [
          ["low", "title"],
          ["bias", "suffix3"],
          ["upper", "pos", "pos2"]
      ]
      # Está configuração determina se é necessário usar
      # a marcação BILOU ou não.
      # BILOU tagging é mais rigoroso no entanto 
      # requer mais exemplos por entidade. 
      # Regra de ouro: use somente se tem mais de
      # 100 exemplos por entidade
      BILOU_flag: true
      # Esse valor é informado ao sklearn_crfsuite.CRFTagger antes do treinamento;
      max_iterations: 50
      # Esse valor é informado ao sklearn_crfsuite.CRFTagger antes do treinamento;
      # Especifica o coeficiente de regularização de L1
      L1_c: 0.1
      # Esse valor é informado ao sklearn_crfsuite.CRFTagger antes do treinamento;
      # Especifica o coeficiente de regularização de L2
      L2_c: 0.1
```
