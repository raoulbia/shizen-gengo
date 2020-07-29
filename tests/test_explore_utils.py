#!/usr/bin/env python3
import shizen_gengo.explore.explore_utils as utils
import pandas as pd


def get_df():
    df = pd.read_csv("../local-data/raw/bs_sample.csv", index_col=0)
    return df


def test_search():
    dfcol = r'resolve_close_notes'
    res = utils.search(get_df(), dfcol, tok=r'ä')
    print('\n{}'.format(res.head()))
    print(len(res))


#TODO
def test_search_window():
    pass
#     col2search = 'resolve_close_notes'
#     res = utils.search_window(df_col, r'@')
#     print('\n{}'.format(res.head()))


def test_check_missing_values():
    df = get_df()
    print('\n{}'.format(utils.check_missing_values(df)))