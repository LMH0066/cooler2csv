import importlib.util
import pathlib

import pandas as pd


def go(filepath: pathlib.Path, dataframe: pd.DataFrame):
    spec = importlib.util.spec_from_file_location('custom_func', filepath)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo.process(dataframe)
