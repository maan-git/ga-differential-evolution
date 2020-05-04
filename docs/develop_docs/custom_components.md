# Componentes Personalizados

<img align="right" height="180" src="/assets/img/iconfinder_Spell_Book_2913104.png">

Você pode criar um componente personalizado para executar uma tarefa específica que o Softcore não oferece atualmente (análise de sentimento, por exemplo). Abaixo está a especificação da classe `softcore.components.Component` com os métodos que você precisará implementar.

Você pode adicionar um componente personalizado ao seu pipeline adicionando o caminho do módulo. Então, se você tiver um módulo chamado `sentiment` contendo uma classe chamada `SentimentAnalzer` ficaria:

```yaml
pipeline:
    - name: "sentiment.SentimentAnalyzer"
```

Também não deixe de ler a seção sore o [ciclo de vida](ciclo de vida) de um componente.

Você pode utilizar esse exemplo de componente, que contém os métodos mais importantes que você deve implementar.

```python

from softcore.components import Component
import typing
from typing import Any, Optional, Text, Dict

if typing.TYPE_CHECKING:
    from softcore.model import Metadata


class MeuComponente(Component):
    """Um novo componente"""

    # Define quais atriutos o componente da pipeline
    # fornece quando chamado. Os atributos listados
    # devem ser definidos pelo componente no objeto de mensagem
    # durante o teste e treino, ex:
    # ``message.set("entities", [...])``
    provides = []

    # Quais atributos em uma mensagem são exigidos por este
    # componente, por exemplo, se `requires` contém "tokens",
    # o componente anterior na pipeline precisa fornecer "tokens",
    # dentro da propriedade `provides` descrita acima.
    requires = []

    # Define os parâmetros de configuração padrão de um componente
    # esses valores podem ser sobrescritos na configuração de pipeline
    # do modelo. O componente deve escolher padrões sensíveis
    # e deve ser capaz de criar resultados razoáveis com os padrões
    defaults = {}

    # Define qual(is) idioma(s) este componente pode manipular.
    # Este atributo é projetado para a instância do 
    # #método: `can_handle_language`
    # O valor padrão é `None`, o que significa que ele pode
    # manipular todos os idiomas.
    # Esse é um recurso importante para compatibilidade com 
    # versões anteriores dos componentes.
    language_list = None

    def __init__(self, component_config=None):
        super(MeuComponente, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Treina este componente

            Neste momento o componente é treinado com os dados de treinamento.
            O componente pode alterar qualquer atributo de contexto, que é criado
            por uma chamada para o método: `components.Component.pipeline_init`
            de qualquer componente."""
        pass
    
    def process(self, message, **kwargs):
        """Processa uma mensagem recebida (parse)

            Neste momento o componente processa uma entrada de
            mensagem (`components.Message`)
            O Componente pode alterar qualquer atributo de
            contexto criado por qualquer componente anterior."""
        pass

    def persist(self,
                file_name: Text,
                model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persiste este componente em disco para carregamento futuro."""

        pass

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir: Optional[Text] = None,
             model_metadata: Optional['Metadata'] = None,
             cached_component: Optional['Component'] = None,
             **kwargs: Any
             ) -> 'Component':
        """Carrega este componente a partir de um arquivo"""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
```

## Component

### `class` `#!python class softcore.components.Component(component_config=None)`

Um componente (**Component**) é uma unidade de processamento de mensagens (**Message**) em um pipeline.

Os componentes são coletados sequencialmente em um pipeline. Cada componente é chamado um após o outro. Isso vale para inicialização, treinamento, persistência e carregamento dos componentes. Se um componente vier primeiro em uma pipeline, seus métodos serão chamados primeiro.

Por exemplo, para processar uma mensagem recebida, o metódo `#!python def process` de cada componente será chamado. Durante o processamento (assim como o treinamento, persistência e inicialização), os componentes podem passar informações para outros componentes, fornecendo atributos para o contexto de pipeline. O contexto de pipeline contém todas as informações dos componentes anteriores que um componente pode usar para fazer seu próprio processamento. Por exemplo, um `featurizer component` pode fornecer recursos usados por outro componente no pipeline para fazer uma classificação.

### `classmethod` `#!python def required_packages() -> List[str]`

Especifique quais pacotes python precisam ser instalados para usar este componente, por exemplo `#!python ["unidecode"]`.

Essa lista de requisitos nos permite emitir uma falha (**raise**) no inicio do treinamento se um pacote necessário não estiver instalado.

### `classmethod` `#!python def create(component_config: Dict[str, Any], config: softcore.config.SoftModelConfig) -> softcore.components.Component`

Cria este componente (por exemplo, antes de um treinamento ser iniciado).

O método pode acessar todos os parâmetros de configuração.

### `#!python provide_context() -> Union[Dict[str, Any], NoneType]`

Inicializa este componente para uma nova pipeline

Esta função será chamada antes que o treinamento seja iniciado e antes que a primeira **mensagem** seja processada usando o interpretador. O componente tem a oportunidade de adicionar informações ao contexto que é passado pelo pipeline durante o treinamento e a análise de mensagens. A maioria dos componentes não precisa da implementação deste método. É usado principalmente para inicializar ambientes de estrutura spacy e tensorflow (carregar vetores de palavras para o pipeline, por exemplo).


### `#!python train(training_data: TrainingData, cfg: softcore.config.SoftModelConfig) -> Union[Dict[str, Any], NoneType]`

Treina o componente

Neste momento o componente é treinado com os dados de treinamento.
O componente pode alterar qualquer atributo de contexto, que é criado
por uma chamada para o método: `components.Component.pipeline_init`
de qualquer componente.

### `#!python process(message: Message. **kwargs) -> None`

Processa uma mensagem recebida.

Momento em que os componentes processam uma mensagem recebida. O componente pode alterar qualquer atributo de contexto apresentado, que é criado por uma chamada a função `components.Component.pipeline_init()` de QUALQUER componente e em qualquer atributo de contexto criado por uma chamada a função `components.Component.process()` de componentes anteriores a este.

### `#!python persist(file_name: str, model_dir: str) -> Union[typing.Dict[str, typing.Any], NoneType]`

Persiste o componente em disco para carregamento futuro.

### `#!python prepare_partial_processing(pipeline: List[_ForwardRef('Component')], context: Dict[str, Any]) -> None

Define o pipeline e o contexto usado para processamento parcial.

O pipeline deve ser uma lista de componentes que são anteriores a este no pipeline e já terminaram seu treinamento (e, portanto, podem ser usados com segurança para processar mensagens).

### `#!python partially_process(message: Message ) -> Message

Permite que o componente processe mensagens durante o treinamento (dados de treinamento externos, por exemplo)

A mensagem passada será processada por todos os componentes anteriores a este na pipeline.

### `classmethod` `#!python def can_handle_language(language: collections.abc.Hashable) -> bool`

Verifica se o componente suporta uma idioma especifico.

Este método pode ser sobrescrito quando necessário.

