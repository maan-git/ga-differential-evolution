# HTTP API

------------

Endpoints:

<img align="right" height="180" src="/assets/img/iconfinder_Adventure_Map_2913095.png">

> [POST /parse]()

> POST /train

> POST /evaluate

> GET /status

> GET /version

> DELETE /models

------------

## Endpoints

### `POST /parse`

Você deve colocar os dados do POST neste formato:

```sh
$ curl -XPOST localhost:5000/parse -d '{"q":"texto aqui"}'
```

Por padrão, quando o projeto não é especificado na consulta, será utilizado um modelo `default`. Você pode (DEVE) especificar o projeto que deseja usar em sua consulta:

```sh
$ curl -XPOST localhost:5000/parse -d '{"q":"texto aqui", "project": "nome do projeto"}'
```

Por padrão, o último modelo treinado para o projeto será carregado. Você também pode consultar um modelo específico de um projeto:

```sh
$ curl -XPOST localhost:5000/parse -d '{"q":"texto aqui", "project": "nome do projeto", "model": "nome do modelo"}'
```

### `POST /train`

Você pode enviar seus dados de treinamento diretamente no terminal para treinar um novo modelo para um projeto. Essa solicitação aguardará a resposta do servidor: o modelo foi treinado com êxito ou o treinamento foi encerrado com erro. Se o modelo for treinado com êxito, um arquivo `zip` será retornado com o modelo treinado. Usando o servidor HTTP, você deve especificar o projeto que você quer treinar um novo modelo para ser capaz de usá-lo durante os pedidos de análise mais tarde: `/train?project=meu_projeto`. A configuração do modelo deve ser enviada como corpo da requisição.

**Utilizando os dados de treinamento no formato json:**

```yaml
language: "pt"

pipeline:
  - name: "SpacyNLP"
  - name: "SpacyTokenizer"
  - name: "RegexFeaturizer"
  - name: "CRFEntityExtractor"

# data contém a mesma coisa que um json descrito na seção dados de treinamento
data: {
    "softcore": {
        "common_examples": [
            {
                "text": "texto",
                "class": "classe"
                "entities":[]
            }
        ]
    }
}
```
`config_ner.yml`

Aqui está uma solicitação de exemplo mostrando como enviar a configuração para o servidor iniciar o treinamento:

```sh
$ curl -XPOST -H "Content-Type: application/x-yml" localhost:5000/train?project=meu_projeto \
    --data-binary @config_samples/config_ner.yml
```

!!! note "Nota"
    A solicitação deve sempre ser enviada como `application/x-yml`, independentemente de você usar json ou md para o formato de dados. Não envie json como `application/json`.

!!! note "Nota"
    Você não pode enviar uma solicitação de treinamento para um projeto que já está treinando um novo modelo.

!!! note "Nota"
    O servidor irá gerar automaticamente um nome para o modelo em treinamento. Se você quiser definir o nome, faça a requisição usando model como parâmetro: `localhost:5000/train?project=meu_projeto&model=meu_modelo`

### `POST /evaluate`

**EM BREVE**

### `GET /status`

Retorna todos os projetos atualmente disponíveis, seu status (`training` ou `ready`) e seus modelos carregados na memória, também retorna uma lista de projetos disponíveis que o servidor pode usar para atender as solicitações de `/parse`.