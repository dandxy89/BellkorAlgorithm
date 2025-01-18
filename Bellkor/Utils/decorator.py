import logging
import os
import pickle
import time
from functools import wraps
from inspect import signature

module_logger = logging.getLogger("Bellkor.Utils.Decorators")


def test_method(
    enable: bool = True,
    model: str = "name",
    test: str = "test",
    conditions: dict = None,
):
    """Decorated for tests, captures inputs and results of the method

    :param enable:          True/False to enable
    :param model:           Expr
    :param test:            Test_name e.g "my_test" - will create sub-folder in tests/integrated/my_test/func_1.pkl
    :param conditions:      Mapping of argument names to values, eg. {'year_index': 4, 'solve_method': 'Demand'}
                            If any of these values are not as specified, the decorator will be disabled
    :return:

    """
    conditions = conditions or {}

    def all_as_kwargs(method, args, kwargs):
        parameter_names = list(signature(method).parameters)
        args_as_kwargs = dict(zip(parameter_names, args, strict=False))
        args_as_kwargs.update(kwargs)
        return args_as_kwargs

    def satisfies_conditions(method, args, kwargs):
        kwargs = all_as_kwargs(method, args, kwargs)
        return all(kwargs.get(key) == value for key, value in conditions.items())

    def all_as_args(method, args, kwargs):
        args = list(args)
        keyword_or_default_parameters = list(signature(method).parameters.values())[len(args) :]
        for parameter in keyword_or_default_parameters:
            args.append(kwargs.get(parameter.name, parameter.default))
        return args

    def dec(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            if enable and satisfies_conditions(method, args, kwargs):
                # Create Test Data Directory
                path = os.path.join("tests/test_data/Bellkor/", model, test, method.__name__)
                if not os.path.exists(path):
                    os.makedirs(path)

                # Pickle Inputs
                input_file = os.path.join(path)
                with open(input_file, "wb") as f:
                    all_args = all_as_args(method, args, kwargs)
                    pickle.dump(all_args, f, protocol=None, fix_imports=True)

                # Get Result
                result = method(*args, **kwargs)

                # Pickle Results
                result_file = os.path.join(path, f"result_{method.__name__}.pkl")
                with open(result_file, "wb") as f:
                    pickle.dump(result, f, protocol=None, fix_imports=True)
            else:
                result = method(*args, **kwargs)

            return result

        return wrapper

    return dec


def timeit(method):
    def timed(*args, **kw):
        logger = logging.getLogger("Bellkor.Utils.Decorators.timeit")

        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        logger.info(f"Method: {method.__name__} - {te - ts} seconds")
        return result

    return timed


def timeit_debug(method):
    def timed(*args, **kw):
        logger = logging.getLogger("Bellkor.Utils.Decorators.timeit_debug")

        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        logger.debug(f"Method: {method.__name__} - {te - ts} seconds")
        return result

    return timed
