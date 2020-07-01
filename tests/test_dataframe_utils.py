#!/usr/bin/env python3

import io
import preprocess_dataframe.dataframe_utils as utils
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 130)
pd.set_option('display.max_colwidth', 130)
# print('\n{}'.format())


def get_df(name='bs'):
    if name == 'bat':
        return pd.read_csv("../local-data/raw/bat_sample2_original_headers.csv", encoding = "ISO-8859-1")
    return pd.read_csv("../local-data/raw/bs_sample.csv", index_col=0)


def test_rename_column():
    df = get_df()
    before = r'resolve_close_notes'
    after = r'rcn'
    print('\n{}'.format(df.columns))
    df.columns = utils.rename_column(df.columns, before, after)
    print('\n{}'.format(df.columns))


def test_standardise_column_headers():
    df = get_df(name='bat')
    print('\n{}'.format(df.columns))
    df.columns = utils.standardise_column_headers(df.columns)
    print('\n{}'.format(df.columns))


def test_standardise_column_headers_custom():
    df = get_df(name='bat')
    print('\n{}'.format(df.columns))
    df.columns = utils.standardise_column_headers(df.columns, before='_-_', after='_')
    print('\n{}'.format(df.columns))


def test_fill_missing():
    df = get_df(name='bat')
    df_col = r'Customer Site Name'
    print(df[df_col].head(6))
    df[df_col] = utils.fill_missing(df[df_col])
    print(df[df_col].head(6))