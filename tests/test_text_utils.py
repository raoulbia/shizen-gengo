#!/usr/bin/env python3
import preprocess_text.text_utils as utils
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def get_df(name='bs'):

    if name == 'bat':
        return pd.read_csv("../local-data/raw/bat_sample2_original_headers.csv",
                           encoding = "ISO-8859-1", # to prevent unicode error
                           index_col=5)

    return pd.read_csv("../local-data/raw/bs_sample.csv",
                       index_col=0)


def test_remove_newline_chars():
    df = get_df()
    examples = ['INC3356469', 'INC4423232']
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'

    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_newline_chars(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_newline_chars2():
    df = get_df(name='bat')
    examples = ['CH3434657', 'CH4418347']
    df = df.loc[examples]
    dfcol = r'Description'

    print('\nbefore:\n{}'.format(df[dfcol]))
    df['cleaned'] = utils.remove_newline_chars(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_repeating_letters():
    df = get_df(name='bat')
    examples = df[df.index.isin(['CH3335178', 'CH4685020'])]
    print('\n{}'.format(examples['Customer Display Name']))
    examples['Customer Display Name'] = utils.remove_repeating_letters(examples['Customer Display Name'])
    print('\n{}'.format(examples['Customer Display Name']))


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
    df = get_df()
    examples = ['INC3098065']
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    print('\nbefore:\n{}'.format(df[dfcol].head()))
    df['cleaned'] = utils.remove_accented_chars(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))
    print(type(df['cleaned']))


def test_remove_punctuation():
    examples = ['INC3098065']
    df = get_df()
    df = df.loc[examples]
    dfcol = r'resolve_close_notes'
    print('\nbefore:\n{}'.format(df[dfcol].head()))
    df['cleaned'] = utils.remove_punctuation(df[dfcol])
    print('\nafter:\n{}'.format(df['cleaned']))


def test_remove_stopwords():
    df = get_df()
    examples = ['INC3356469', 'INC4423232']
    df = df.loc[examples] # speed up test
    dfcol = r'resolve_close_notes'
    print('\nbefore:\n{}'.format(df.loc[examples][dfcol]))
    df['cleaned'] = utils.remove_stopwords(df[dfcol])
    print('\nafter:\n{}'.format(df.loc[examples]['cleaned']))


#TODO
def test_all():
    df = get_df().sample(5)


