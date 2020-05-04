# Executando no Docker

## Módulo de Treino

Para treinar um modelo, você precisa montar dois diretórios no contêiner Docker:

* um diretório contendo seu projeto que, por sua vez, inclui sua configuração e seus dados de treinamento
* um diretório que conterá o modelo treinado

```sh
docker run \
    -v <diretorio_do_projeto>:/app/project \
    -v <diretorio_de_saida_do_modelo>:app/models \
    ./softcore/dockers \
    run \
        python -m softcore.train \
            -c /app/project/<arquivo_de_configuracao>.yml
            -d /app/project/<dados de treino> \
            -o /app/model \
            --project <nome_do_projeto>
```

## Executando o Softcore como servidor Standalone

Para executar o Sofcore como servidor você precisa:

* montar um diretório com os modelos treinados
* expor uma porta

```sh
docker run \
    -p 5000:5000
    -v <diretorio dos modelos>:/app/projects \
    ./softcore/dockers \
    start \
        --path /app/projects
        --port 5000
```

Você pode então enviar pedidos para o seu servidor Softcore conforme descrito na seção [API HTTP](/api_reference/http_api/), por exemplo, se ele estiver sendo executado no localhost:

```
curl --request GET\
    --url 'http://localhost:5000/parse?q=Texto%20Aqui'
```

---------

### Alterando o Dockerfile

Sempre será necessário criar a melhor estrutura possível para o seu problema especifico. No arquivo `Dockerfile` é possível alterar os parâmetros de entrada do sistema.
