# Formato dos Dados de Treinamento

### Formato de Dados

Você pode fornecer dados de treinamento como json (markdown em breve), como um único arquivo ou como um diretório contendo vários arquivos.

<img align="right" height="180" src="/assets/img/iconfinder_Spell_Scroll_2913111.png">

### Formato JSON

O formato JSON consiste em um objeto de nível superior chamado `softcore_data`, com as chaves `common_examples`, `entity_synonyms`, `lookup_tables` e `regex_features`. O mais importante é o `common_examples`.

```json
{
    "softcore": {
        "common_examples": [],
        "regex_features" : [],
        "lookup_tables"  : [],
        "entity_synonyms": []
    }
}
```

Os dados contidos em `common_examples` são usado para treinar seu modelo. Você deve colocar todos os seus exemplos de treinamento nesta chave. As **regex features** são uma ferramenta para ajudar o classificador a detectar entidades ou classe (texto) para melhorar o desempenho.

### Visualizando os dados de treinamento

Em breve será desenvolvido ferramentas que vão facilitar o trabalho de marcação em textos. No momento indicamos o uso de ferramentas como [Dataturks](https://dataturks.com/).

### Exemplos Comuns

Um exemplo de uso comum têm três componentes: `text`, `class`, e `entities`. Os primeiros são strings, enquanto o último é um array (lista).

* O texto (text) é um documento jurídico, uma receita de bolo, uma pesquisa em uma faq; Um exemplo do que seria submetido para a análise. [requerido]
* A classe (class) é a intenção/label/classe que deve ser associada ao texto. [opcional].
* As entidades (entities) são partes específicas do texto que precisam ser identificadas. [opcional].

As entidades são especificadas com um valor de start e end, que juntos formam um intervalo de estilo python para aplicar à string, como no exemplo abaixo. As entidades podem abranger várias palavras e , de fato, o campo não precisa corresponder exatamente a subsequencia em seu exemplo. Dessa forma, você pode mapear sinônimos ou erros ortográficos para o mesmo.

```json
{
    "text": "gostaria de comprar uma pizza",
    "class": "comprar",
    "entities": [
        {
            "start": 24,
            "end": 29,
            "value": "pizza",
            "entity": "alimento"
        }
    ]
}
```

### Regex Features (Expressões regulares)

Expressões regulares podem ser usadas para ajudar a classificação de texto (classes) e a extração de entidades. Por exemplo. se a sua entidade tiver uma determinada estrutura como em um CEP, você poderá usar uma expressão regular para facilitar a detectação dessa entidade. Para o exemplo do CEP:

```json
{
    "softcore":{
        "regex_features":[
            {
                "name": "cep",
                "pattern": "[0-9]{5}-[0-9]{3}"
            }
        ]
    }
}
```

A chave `name` não define a entidade nem a classe `(classificação de texto)`, é apenas uma descrição legível para você lembrar-se de como esse regex é usado e é o titulo do recurso de `feature` correspondente.

!!! warning "Atenção"
    Os recursos de regex `(regex features)` não definem entidades nem classes de documentos! Eles simplesmente fornecem padrões para ajudar o classificador a reconhecer entidades e classes relacionadas. Portanto, você ainda precisa fornecer exemplos de classes e entidades como parte de seus dados de treinamento!

### Lookup Table (Tabelas de Pesquisa)

As tabelas de consulta na forma de arquivos externos ou listas de elementos também podem ser especificadas nos dados de treinamento. As tabelas de pesquisa fornecidas externamente devem estar em um formato separado por uma nova linha. Por exemplo `data/treino/lookup_tables/alimentos.txt` pode conter:

> pizza 
> hamburger 
> bife 
> carne 
> frango

E pode ser carregado da seguinte forma:

```json
{
    "softcore": {
        "lookup_tables": [
            {
                "name": "alimentos",
                "elements": "data/treino/lookup_tables/alimentos.txt"
            }
        ]
    }
}
```

Como alternativa, os elementos de pesquisa podem ser incluídos diretamente como uma lista:

```json
{
    "softcore": {
        "lookup_tables": ["pizza", "hamburger", "bife", "carne", "frango"]
    }
}
```

Quando as tabelas de consulta são fornecidas nos dados de treinamento, o conteúdo é combinado em um padrão de expressão regular, sem distinção entre maiúsculas e minúsculas, que procura correspondências exatas nos exemplos de treinamento. Os regex `(expressão regular)` são processados de maneira idêntica ao `regex features`.

!!! note "Nota"
    Para que as tabelas de consulta sejam efetivas, deve haver alguns exemplos de correspondências em seus dados de treinamento. Caso contrário, o modelo não aprenderá a usar os recursos de correspondência da tabela de consulta.

!!! danger "Aviso"
    É preciso ter cuidado com o tipo de dados que está presente em suas `lookup tables`. Por exemplo, se alguns dos elementos são combinados com palavras comuns que não são a entidade que você deseja extrair, isso limitará a eficácia desse método. Na verdade, isso pode prejudicar o desempenho do reconhecimento de entidades. Portanto, tente usar as tabelas de consulta somente quanto tiver uma lista de frases ou tokens não ambíguios com os quais você deseja corresponder e certifique-se de filtrar elementos possivelmente problemáticos.