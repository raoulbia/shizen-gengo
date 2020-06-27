#!/usr/bin/env python3

import io
import preprocess_dataframe.dataframe_utils as utils
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 130)
pd.set_option('display.max_colwidth', 130)
# print('\n{}'.format())


def get_df():
    df = pd.read_csv("../local-data/raw/bs_sample.csv", index_col=0)
    return df

def test_rename_col():
    df = get_df()
    before = r'resolve_close_notes'
    after = r'rcn'
    print('\n{}'.format(df.columns))
    df.columns = utils.rename_col(df.columns, before, after)
    print('\n{}'.format(df.columns))


# def test_fill_missing():
#     df = get_df()
#     column = r'subcategory'
#     print('\n{}'.format(len(df.isna().sum())))
#     df.columns = utils.fill_missing(df, column)
#     print('\n{}'.format(len(df.isna().sum())))