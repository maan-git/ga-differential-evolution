# Executando um Servidor de Softcore

O Softcore permite sua execução tanto no Docker quanto diretamente via linha de comando.

!!! note "Nota"
    A execução via linha de comando serve para que você produza o melhor Dockerfile para seu problema.

O comando será algo parecido com isto:

```sh 
python -m softcore.server --path "/tmp/models/" --storage aws
```

## Parâmetros

### Emulate

**Sintaxe:** `-e` ou `--emulate` </br>
**Descrição:** Informa ao Softcore o formado de entrada dos dados de treinamento. É possível ver mais sobre os formatos de dados no arquivo `softcore.training_data.formats.readerwriter`. 

-------

### Token
 
**Sintaxe:**  `-t` ou `--token` </br>
**Descrição:** Token de autenticação. Se definido, rejeita todas as solicitações que não fornecerem este token como parâmetro da consulta.
**Exemplo:** `http://localhost:5000/parse?token=123`

-------

### Write

**Sintaxe:**  `-w` ou `--write` (Log HTTP)</br>
**Descrição:** Arquivo de logs do servidor.

-------

### Path

**Sintaxe:**  `--path` </br>
**Descrição:** Diretório de trabalho do servidor. Modelos são carregados deste servidor e modelos treinados serão salvos aqui.

-------

### Max Training Processes

**Sintaxe:**  `--max_training_processes` </br>
**Descrição:** Número de processos usados para lidar com o treinamento. Aumentar esse valor terá um grande impacto no uso de memória.

-------

### Num Threads

**Sintaxe:**  `--num_threads` </br>
**Descrição:** Número de threads a serem usadas para processar os pedidos de parser.

-------

### Response Log

**Sintaxe:**  `--response_log` (Log SoftCore)</br>
**Descrição:** Diretório onde os registros serão salvos (contendo consultas e respostas) Se definido como `null`, o registro será desabilitado.

-------

### Storage

**Sintaxe:**  `--storage` </br>
**Descrição:** Define o local remoto onde os modelos serão armazenados. Por exemplo, AWS. Se nada estiver configurado, o servidor servirá apenas os modelos persistidos em disco.

-------

### Config

**Sintaxe:** `-c` ou `--config` </br>
**Descrição:** Arquivo de configuração do modelo usado para o treinamento.



