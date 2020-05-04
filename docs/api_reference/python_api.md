# Python API

<img align="right" height="180" src="/assets/img/iconfinder_Knight_2913116.png">

Além de utilizar o Softcore acoplado ao Softapis como um servidor HTTP, você pode usá-lo diretamente no seu programa Python. Softcore no momento só suporta o Python 3.5 acima; 

## Treinando um modelo

```python
from softcore.training_data import load_data
from softcore.model import Trainer
from softcore import config

training_data = load_data("./caminho/dos/seus/dados/de/treino.json")
trainer = Trainer(config.load("arquivo/de/configuração.yaml"))

interpreter = trainer.train(training_data)

model_directory = trainer.persist("./modelos")
```

## Consumindo um modelo

<img align="right" height="180" src="/assets/img/iconfinder_Helmet.jpg_2913118.png">

Você pode consumir seu modelo diratamente do Softcore em seu script Python. Para fazer isso, você precisa carregar os metadados do seu modelo e instanciar um intérprete (`softcore.model.Interpreter`). O `metadata.json` no diretório do seu modelo contém as informações necessárias para reconstruir seu modelo:

```python
from softcore.model import Interpreter

# onde model_directory contém o diretório do modelo persistido
interpreter = Interpreter.load(model_directory)
```

Você pode então usar o interpretador carregado para analisar o texto:

```python
interpreter.parse(u"Texto exemplo")
```

## Reduzindo o uso de memória ao carregar vários modelos

<img align="right" height="180" src="/assets/img/iconfinder_Armor_2913124.png">

Se vários modelos forem criados, é razoável compartilhar componentes entre os diferentes modelos. Por exemplo,  o componente `SpacyTokenizer`, que é utilizado por cada pipeline que deseja tokenizar um texto, pode ser armazenado em cache para evitar o que sempre ocorra o seu instanciamento. Para usar o cache, deve-se passar um `ComponentBuilder` ao carregar e treinar modelos.

Aqui um breve exemplo de como criar um construtor de componentes, que pode ser reutilizado para treinar e executar vários modelos. **Para treinar um modelo**:

```python
from softcore.training_data import load_data
from softcore import config
from softcore.components import ComponentBuilder
from softcore.model import Trainer

builder = ComponentBuilder(use_cache=True)

training_data = load_data("./caminho/dos/seus/dados/de/treino.json")
trainer = Trainer(config.load("arquivo/de/configuração.yaml"))
interpreter = trainer.train(training_data)
model_directory = trainer.persist("./modelos")
```

O mesmo construtor pode ser usado para carregar um modelo (pode ser totalmente diferente). O construtor armazena apenas componentes seguros para serem compartilhados entre os modelos. Aqui um breve exemplo de como usar o construtor ao carregar modelos:

```python
from softcore.model import Interpreter
from softcode import config

interpreter = Interpreter.load(model_directory, builder)
interpreter_clone = Interpreter.load(model_directory, builder)
```

# Classes importantes

<img align="right" height="180" src="/assets/img/iconfinder_Sword_2913105.png">

## Config

####`#!python softcore.config.load(filename: Union[str, Nonetype] = None, **kwargs) -> softcore.config.SoftModelConfig`

-------

####`#!python class softcore.config.SoftModelConfig(configuration_values=None)`

-------

####`#!python __init__(configuration_values=None)`

Cria uma configuração de modelo, opcionalmente substituindo os padrões por um dicionário `configuration_values`

## Interpreter

####`#!python softcore.model.Interpreter(pipeline: List[softcore.components.Component], context: Union[typing.Dict[str, typing.Any], Nonetype], model_metadata: Union[softcore.model.Metadata, NoneType] = None)`

Utiliza uma pipeline de componentes já treinados para fazer análise de texto.

-------

####`#!python static load(model_dir: str, component_builder: Union[softcore.components.ComponentBuilder, NoneType] = None, skip_validation: bool = False) -> softcore.model.Interpreter`

Cria um interpretador baseado em um modelo persistido.

**Parâmetros:**

* **skip_validation**: Se definido como True, tenta verificar se todos os pacotes necessários para os componentes estão instalados antes de carregá-los
* **model_dir**: O caminho do modelo a ser carregado
* **component_builder**: O `ComponentBuilder` que será utilizado

**Retorna**: Um intérprete que utiliza o modelo carregado.

-------

## Metadata

####`#!python class softcore.model.Metadata(metadata: Dict[str, Any], model_dir: Union[str, NoneType])`

Captura todas as informações sobre um modelo para carrega-lo e prepará-lo.

-------

####`#!python static load(model_dir: str)`

Carrega os metadados de um diretório de modelos.

**Parâmetros:** **model_dir** (str) - o diretório onde o modelo é salvo.

**Retorna:** Um objeto de metadados que descreve o modelo.

**Tipo de Retorno:** [Metadata](#metadata)

-------

## ComponentBuilder

####`#!python class softcore.components.ComponentBuilder(use_cache: bool = True)`

Cria construtores `(builder)` e intérpretes `(Interpreter)` baseados nas configurações.

Caches dos componentes para reutilização.

-------

####`#!python load_component(component_meta: Dict[str, Any], model_dir: str, model_metadata: Metadata, **context) -> softcore.components.Component`

Tenta recuperar um componente do cache, senão chame `load` para criar um novo componente.

**Parâmetros:**

* **component_meta** (dict): Os metadados do componente para carregar no pipeline 
* **model_dir**: O caminho do modelo a ser carregado
* **model_metadata** ([Metadata](#metadata)): `softcore.models.Metadata`
  
**Retorna**: O componente carregado.

**Tipo de retorno:** [Component](/develop_docs/custom_components/#component)