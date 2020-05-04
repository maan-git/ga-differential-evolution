import random
import os
import pickle
import re
from datetime import datetime


def generate_rand_int(min_value, max_value):
    return random.randint(min_value, max_value)


def generate_rand_float(min_value, max_value):
    return random.uniform(min_value, max_value)


def generate_rand_bool(min_value, max_value):
    return random.choice([min_value, max_value])


def get_rand_value(type_value):
    types = {
        int: generate_rand_int,
        float: generate_rand_float,
        bool: generate_rand_bool
    }
    return types.get(type_value, "Type not found!")


def generate_rand_value(min_valeu, max_value, type_value):
    tp_value_func = get_rand_value(type_value)
    return tp_value_func(min_valeu, max_value)


def make_dict(key_pivot, keys, values):
    return {key_pivot: dict(zip(keys, values))}


def save_result(data, file_name, path):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(r"{}/{}_{}_res.txt".format(path, datetime.now().strftime("%Y_%m_%d_%H_%M"), file_name), "w+") as file:
        for dt in data:
            file.write(str(dt) + '\n')


def open_pkl(file_name, path):
    res = ""
    file_path = r'{}/{}_model.pkl'.format(path, file_name)
    with open(file_path, 'rb') as file:
        res = pickle.load(file)
    return res


if __name__ == '__main__':
    # print(generate_rand_value('a', 'b', bool))
    # save_result(['a', 'b'], 'dados_otmizacao', '../../data/results')
    class a:
        def __init__(self):
            self.coords = ['a', 'b']


    class b:
        def __init__(self):
            self.coords = ['c', 'd']


    obj_a = a()
    obj_b = b()
    print(generate_rand_value(obj_a, obj_b, bool).coords[1])
