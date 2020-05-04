import datetime

from de_GA.utils import save_result
from de_GA.differential_evolution import DifferentialEvolution


def run(params_md, params_ga, data, params_storage):
    """
    :param params_md: dictionary containing the parameters of the model
    :param params_ga: dictionary containing the parameters of the GA
    :param data: X_train, y_train, X_test, y_test
    :param params_storage: Path where the results will be stored
    :return:
    """

    """
    Params GA
    params_ga = {
        'num_exp': 2,
        'num_runs': 10,
        'num_indvs': 5
    }
    """

    """
    Params Model
    params_model = {
        'model': {
            'type': 'classifier',
            'model_name': 'random_forest',
            'metric': 'precission',
            'value_metric': 0.93,
            'print_status': True
        },
        'bootstrap': {
            'values': [True, False],
            'optimizer': 'yes',
            'type': bool
        },
        'max_depth': {
            'values': [True, None],
            'optimizer': 'yes',
            'type': bool
        },
        'max_features': {
            'values': 'auto',
            'optimizer': 'no',
            'type': str
        },
        'min_samples_leaf': {
            'values': [1, 3],
            'optimizer': 'yes',
            'type': int
        },
        'min_samples_split': {
            'values': [2, 4],
            'optimizer': 'yes',
            'type': int
        },
        'n_estimators': {
            'values': [1, 40],
            'optimizer': 'yes',
            'type': int
        }
    }
    """

    """
    data = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
    }
    """

    """
    params_storage = {
        'path': 'local/folder/',
        'model_name': 'model_name'
    }
    """
    val, val_total = 0, 0
    print_time = True
    vals_res, params_res, models_res = [], [], []

    for i in range(params_ga['num_exp']):
        start = datetime.datetime.now()
        de = DifferentialEvolution(data=data,
                                   num_iterations=params_ga['num_runs'],
                                   CR=0.75,
                                   F=0.48,
                                   population_size=params_ga['num_indvs'],
                                   print_status=True,
                                   func=params_md['model']['metric'],
                                   model=params_md['model']['model_name'],
                                   params=params_md,
                                   type=params_md['model']['type'],
                                   metric_value=params_md['model']['value_metric'])
        val, params_sim, model_ml = de.simulate()

        vals_res.append(val)
        params_res.append(params_sim)
        models_res.append(model_ml)

        val_total += val
        if print_time:
            print("\nTime taken:", datetime.datetime.now() - start)
        print('-' * 80)
        print("\nFinal average of all runs:", val_total / params_ga['num_runs'])

    save_result(vals_res, r'{}_{}'.format(params_storage['model_name'], 'val'), params_storage['path'])
    save_result(params_res, r'{}_{}'.format(params_storage['model_name'], 'params'), params_storage['path'])
    save_result(models_res, r'{}_{}'.format(params_storage['model_name'], 'model'), params_storage['path'])
