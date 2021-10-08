import numpy as np
import pandas as pd


class BasicFunctions:

    def __init__(self, df):
        self.df = df

    def apply_func_col(self, col, func):
        return func(self.df[col])

    def drop_col(self, list_columns):
        return self.df.drop(columns=list_columns, axis=1)

    def drop_na_row(self, list_columns=None):
        return self.df.dropna(subset=list_columns, axis=0)

    def drop_na_col(self, list_columns=None):
        return self.df.dropna(subset=list_columns, axis=1)

    def fill_na_col(self, values):
        return self.df.fillna(values)

    def describe_df(self):
        return self.df.describe()

    def group_op(self, col_group, col, op):
        partial = self.df.groupby(col_group).agg({col: op})
        return partial.rename({col: 'new_col'}, axis=1).reset_index()

    def select_col(self, list_col):
        return self.df[list_col]

    def filter_col(self, str_filter):
        return self.df.query(str_filter)

    def rename_col(self, dic_new_col):
        return self.df.rename(dic_new_col, axis=1)

    def new_col(self, name_col, func, cols):
        list_args = [self.df[col] for col in cols]
        self.df[name_col] = np.vectorize(func)(*list_args)
        return self.df

    def multi_group(self, col_group, agg_dict):
        return self.df.groupby(col_group).agg(agg_dict)

    def df_set_index(self, new_index):
        return self.df.set_index(new_index)

    def reset_index(self):
        return self.df.reset_index()

    def pivot(self, index_col, value_col, func):
        return pd.pivot_table(self.df, index=index_col, values=value_col, aggfunc=func)
