# Extração de Entidades

| Componente               | Requer           | Modelo     | Notas    |
| ------------------------ | ---------------- | ---------- | ------- |
| CRFEntityExtractor       | sklearn-crfsuite | [CRF](https://repository.upenn.edu/cis_papers/159/)        | Bom para treinar entidades personalizadas     |

## Entidades Customizadas

Quase todos os projetos envolveram alguma entidade personalizada. O componente `CRFEntityExtractor` pode aprender entidades personalizadas em qualquer idioma.

## Expressões Regulares (regex)

Você pode usar expressões regulares para ajudar o modelo de **CRF** a reconhecer entidades. No formato de dados de treinamento, você pode fornecer uma lista de expressões regulares, cada uma das quais fornece um recurso binário ao componente `CRFEntityExtractor`, que diz se a regex foi encontrada (1) ou não (0).

Se você quer apenas corresponder exatamente expressões regulares, você pode fazer isso em seu código, como uma etapa de pós-processamento depois de receber o formulário de resposta do Softcore.

## Retorno da Extração de Entidades

No objecto retornado após a análise, há dois campos que mostram informações sobre como a pipeline impactou as entidades retornadas. O campos `extractor` de uma entidade informa qual extrator de entidade encontrou essa entidade especifica.

```python
{
    "text": "Eu moro em Florianópolis",
    "intent": "restaurant_search",
    "entities": [
        {
            "value":"Florianópolis",
            "start": 11,
            "end": 24,
            "entity": "city",
            "confidence": 0.874,
            "extractor": "CRFEntityExtractor"
        }
    ]
}
```

!!! note "Nota"
    A confiança (`confidence`) será definida pelo extrator de entidade CRF (componente *CRFEntityExtractor*) ou pelo extrator definido na pipeline.
