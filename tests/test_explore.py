#!/usr/bin/env python3

import explore.search_utils as utils
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)
pd.set_option('display.max_colwidth', 150)


def get_df():
    df = pd.read_csv("../local-data/raw/bs_sample.csv", index_col=0)
    return df

def test_search():
    dfcol = r'resolve_close_notes'
    res = utils.search(get_df(), dfcol, tok = r'ä')
    print('\n{}'.format(res.head()))
    print(len(res))
# def test_search_window():
#     col2search = 'resolve_close_notes'
#     res = utils.search_window(df_col, r'@')
#     print('\n{}'.format(res.head()))
