from pandas import DataFrame

def filter_by_index(dataframe: DataFrame, min_index: float, max_index: float) -> DataFrame:
    return dataframe[(dataframe.index >= min_index) & (dataframe.index <= max_index)]
