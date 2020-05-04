FROM python:3.7-stretch

ENV DE_GA_DOCKER="YES" \
    HOME=/app \
    PYTHON_PACKAGES=/usr/local/lib/python3.7/dist-packages

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core openssl libssl-dev libffi6 libffi-dev c  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR ${HOME}

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

COPY . ${HOME}

RUN pip install -r requirements-dev.txt

RUN pip install -e .

VOLUME ["/app/projects", "/app/logs", "/app/data"]

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]

# -c : Arquivo de configuração
# --path: Pasta onde os modelos serão salvos
# --storage: storage remoto onde os modelos serão persistidos
# --max_training_processes: Numero de processos utilizados no treino de modelos
# --num_threads: Numero de threads utilizadas no processo de parser

CMD ["start", "-c", "config.yml", "--path", "/app/projects", "--storage", "aws"]