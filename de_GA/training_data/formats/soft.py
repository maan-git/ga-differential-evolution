from de_GA.training_data.formats.readerwriter import (
    JsonTrainingDataReader,
    TrainingDataWriter,
)


class SoftWriter(TrainingDataWriter):
    def dumps(self, training_data, **kwargs):
        formatted_examples = [
            example.as_dict() for example in training_data.training_examples
        ]

        return {"de_GA": {"common_examples": formatted_examples}}


class SoftReader(JsonTrainingDataReader):
    def read_from_json(self, js, **kwargs):
        from de_GA.training_data import Message, TrainingData

        data = js["de_GA"]
        common_examples = data.get("common_examples", [])
        regex_features = data.get("regex_features", [])
        lookup_tables = data.get("lookup_tables", [])

        training_examples = []
        for ex in common_examples:
            msg = Message.build(ex["text"], ex.get("intent"), ex.get("entities"))
            training_examples.append(msg)

        return TrainingData(training_examples, regex_features, lookup_tables)
