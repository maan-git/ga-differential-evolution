# Armazenando Modelos na Nuvem

Softcore atualmente suporta o uso do [S3](https://aws.amazon.com/pt/s3/) para salvar seus modelos.

## Armazenamento Amazon S3

O S3 é suportado utilizando o módulo [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) que você pode instalar via `#!bash pip install boto3`.

Inicie um servidor Softcore com a opção `storage` definida como `aws`. Obtenha suas credenciais do S3 e defina as seguintes variáveis de ambiente:

* AWS_SECRET_ACCESS_KEY
* AWS_ACCESS_KEY_ID
* AWS_DEFAULT_REGION
* BUCKET_NAME
* AWS_ENDPOINT_URL

Se não houver `bucket` com o nome **BUCKET_NAME** o Core irá criá-lo.

## Informações

Os modelos são compactados antes de serem salvos na numve. A convenção de nomenclatura de arquivos compactados com gzip é *[PROJECT]___[MODEL_NAME].tar.gz* e é armazenada na pasta raiz do serviço de armazenamento. Atualmente, você não pode especificar manualmente o caminho no armazenamento em nuvem.

Se armazenar modelos treinados, o Softcore erá compactar o novo modelo e carregá-lo no contêiner. Se estiver recuperando/carregando modelos do armazenamento em nuvem, o Softcore baixará o modelo gzipado localmente e extrairá o conteúdo para o local especifico pela `flag` `--path`