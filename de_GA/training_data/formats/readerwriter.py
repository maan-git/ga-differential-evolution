# coding:utf-8
import json

from de_GA import utils
from de_GA.utils import read_file


class TrainingDataReader(object):
    def read(self, filename, **kwargs):
        return self.reads(read_file(filename), **kwargs)

    def reads(self, s, **kwargs):
        raise NotImplementedError


class TrainingDataWriter(object):
    def dump(self, filename, training_data):
        s = self.dumps(training_data)
        utils.write_to_file(filename, s)

    def dumps(self, training_data):
        raise NotImplementedError


class JsonTrainingDataReader(TrainingDataReader):
    def reads(self, s, **kwargs):
        js = json.loads(s)
        return self.read_from_json(js, **kwargs)

    def read_from_json(self, js, **kwargs):
        raise NotImplementedError
