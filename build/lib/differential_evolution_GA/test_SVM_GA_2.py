import pandas as pd

from sklearn.model_selection import train_test_split
from de_GA.utils import open_pkl

from de_GA.run import run

if __name__ == '__main__':

    """
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
    kernel='linear', max_iter=-1, probability=True, random_state=None,
    shrinking=True, tol=0.001, verbose=True) 
    """
    number_of_exps = 1
    number_of_runs = 4
    number_of_indvs = 15
    val, val_total = 0, 0
    print_time = True
    vals_res, params_res, models_res = [], [], []

    path_doc_extra = "../data_tests/data"
    df_data = pd.read_csv(r"{}/{}".format(path_doc_extra, "data_classification.csv"), sep=";", encoding="UTF-8")
    # df_data_fil = df_data_fil_.sample(frac=0.99)

    X_train_fil, X_test_fil, y_train_fil, y_test_fil = train_test_split(
        df_data.drop(columns=['Y1', 'Y2']),
        df_data['Y1'],
        test_size=0.2,
        random_state=101)

    X_train_fil, X_val_fil, y_train_fil, y_val_fil = train_test_split(
        X_train_fil,
        y_train_fil,
        test_size=0.2, random_state=101)

    data = {
        'X_train': X_train_fil,
        'X_test': X_test_fil,
        'y_train': y_train_fil,
        'y_test': y_test_fil
    }

    params_svm = {
        'model': {
            'type': 'classification',
            'model_name': 'svm',
            'metric': 'precission',
            'value_metric': 0.93,
            'print_status': True
        },
        'C': {
            'values': [1, 5],
            'optimizer': 'yes',
            'type': float
        },
        'kernel': {
            'values': 'linear',
            'optimizer': 'no',
            'type': str
        },
        'verbose': {
            'values': False,
            'optimizer': 'no',
            'type': bool
        },
        'probability': {
            'values': True,
            'optimizer': 'no',
            'type': bool
        }
    }
    params_ga = {
        'num_exp': 2,
        'num_runs': 2,
        'num_indvs': 5
    }

    params_storage = {
        'path': '../data/results',
        'model_name': 'svm'
    }
    run(params_svm, params_ga, data, params_storage)
