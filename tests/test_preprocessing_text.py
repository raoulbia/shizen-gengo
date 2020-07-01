#!/usr/bin/env python3

import io
import preprocess_text.text_utils as utils
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 130)
pd.set_option('display.max_colwidth', 130)
# print('\n{}'.format())

def get_df():
    df = pd.read_csv("../local-data/raw/bs_sample.csv", index_col=0)
    return df


# def get_some_text(record=None):
#     df = pd.read_csv("../local-data/raw/bs_sample.csv", index_col=0)
#
#     # select dataframe column with text
#     df_col = df.resolve_close_notes.dropna()
#     if record:
#         return df_col.loc[record]
#     return df_col.sample(10)
#
# def test_get_some_text():
#     print('\n{}'.format(get_some_text()))


def test_remove_nl_cr():
    examples = ['INC3356469', 'INC4423232']  # nl, cr, consec. spaces
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_nl_cr(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


#TODO
def test_remove_repeating_letters():
    df = get_df().sample(5)


def test_remove_consecutive_spaces():
    examples = ['INC3356469', 'INC4423232']  # nl, cr, consec. spaces
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_consecutive_spaces(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_digits():
    examples = ['INC3560034', 'INC4889742']  # digits
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_digits(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_non_char():
    examples = ['INC3073892', 'INC3288398', 'INC5402381']  # parentheses, >, <. #
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_non_char(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_custom_replace():
    examples = ['INC5402381']  # parentheses, >, <. #
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.custom_replace(df[dfcol], '#', '$')
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_url():
    examples = ['INC5295070']  # parentheses, >, <. #
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_url(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_email():
    examples = ['INC3166609', 'INC2929187', 'INC4925154']
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    # dfcol = get_some_text(examples)
    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_email(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_accented_chars():
    examples = ['INC3098065']
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    print('\nbefore:\n{}'.format(df[dfcol].head()))
    df['cleaned'] = utils.remove_accented_chars(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_punctuation():
    examples = ['INC3098065']
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    print('\nbefore:\n{}'.format(df[dfcol].head()))
    df['cleaned'] = df[dfcol].apply(lambda x : utils.remove_punctuation(x))
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_stopwords():
    df = get_df().sample(5)
    dfcol = r'resolve_close_notes'
    print('\nbefore:\n{}'.format(df[dfcol].head()))
    df['cleaned'] = df[dfcol].apply(lambda x : utils.remove_stopwords(x))
    print('\nafter:\n{}'.format(df['cleaned'].head()))


#TODO
def test_all():
    df = get_df().sample(5)


