# coding:utf-8

import logging
import os
import warnings

from copy import deepcopy
from collections import Counter

from de_GA.utils import write_json_to_file, lazyproperty

DEFAULT_TRAINING_DATA_OUTPUT_PATH = "training_data.json"

logger = logging.getLogger(__name__)


class TrainingData(object):

    MIN_EXAMPLES_PER_ENTITY = 2

    def __init__(self, training_examples=None, regex_features=None, lookup_table=None):

        if training_examples:
            self.training_examples = training_examples
        else:
            self.training_examples = []

        self.regex_features = regex_features if regex_features else []
        self.lookup_tables = lookup_table if lookup_table else []

    @lazyproperty
    def intent_examples(self):
        return [ex for ex in self.training_examples if ex.get("intent")]

    @lazyproperty
    def entity_examples(self):
        return [ex for ex in self.training_examples if ex.get("entities")]

    @lazyproperty
    def intents(self):
        """Returns the set of intents in the training data."""
        return set([ex.get("intent") for ex in self.training_examples]) - {None}

    @lazyproperty
    def examples_per_intent(self):
        """Calculates the number of examples per intent."""
        intents = [ex.get("intent") for ex in self.training_examples]
        return dict(Counter(intents))

    @lazyproperty
    def entities(self):
        """Returns the set of entity types in the training data."""
        entity_types = [e.get("entity") for e in self.sorted_entities()]
        return set(entity_types)

    @lazyproperty
    def examples_per_entity(self):
        """Calculates the number of examples per entity."""
        entity_types = [e.get("entity") for e in self.sorted_entities()]
        return dict(Counter(entity_types))

    def sorted_entities(self):
        entity_examples = [
            entity for ex in self.entity_examples for entity in ex.get("entities")
        ]
        return sorted(entity_examples, key=lambda e: e["entity"])

    def as_json(self, **kwargs):
        from de_GA.training_data.formats import SoftWriter

        return SoftWriter().dumps(self)

    def persist(self, dir_name, filename=DEFAULT_TRAINING_DATA_OUTPUT_PATH):

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        data_file = os.path.join(dir_name, filename)
        write_json_to_file(data_file, self.as_json(indent=4))

        return {"training_data": data_file}

    def merge(self, *others: "TrainingData") -> "TrainingData":

        training_examples = deepcopy(self.training_examples)
        regex_features = deepcopy(self.regex_features)
        lookup_tables = deepcopy(self.lookup_tables)

        for o in others:
            training_examples.extend(deepcopy(o.training_examples))
            regex_features.extend(deepcopy(o.regex_features))
            lookup_tables.extend(deepcopy(o.lookup_tables))

        return TrainingData(training_examples, regex_features, lookup_tables)

    def validate(self) -> None:
        logger.debug("Validationg training data...")

        # emit warnings for entities with only a few training samples
        for entity_type, count in self.examples_per_entity.items():
            if count < self.MIN_EXAMPLES_PER_ENTITY:
                warnings.warn(
                    "Entity '{}' has only {} training examples! "
                    "minimum is {}, training may fail."
                    "".format(entity_type, count, self.MIN_EXAMPLES_PER_ENTITY)
                )

    # TODO
    # def train_test_split(self, train_frac: float = 0.8):

    #     train, test = [], []
    #     for intent
