# coding:utf-8
import logging

from de_GA import utils
from de_GA.training_data.formats.soft import SoftReader
from de_GA.training_data import TrainingData

logger = logging.getLogger(__name__)


def _load(filename, language="pt"):
    # TODO: INSERIR MAIS TIPOS DE DADOS DE ENTRADA
    reader = SoftReader()

    if reader:
        return reader.read(filename, language=language)
    else:
        return None


def load_data(resource_name, language="pt") -> "TrainingData":

    files = utils.list_files(resource_name)
    data_sets = [_load(f, language) for f in files]
    data_sets = [ds for ds in data_sets if ds]
    if len(data_sets) == 0:
        training_data = TrainingData()
    elif len(data_sets) == 1:
        training_data = data_sets[0]
    else:
        training_data = data_sets[0].merge(*data_sets[1:])

    return training_data
