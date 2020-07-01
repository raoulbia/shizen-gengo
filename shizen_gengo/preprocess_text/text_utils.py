#!/usr/bin/env python3

import string
import unicodedata
import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english")) # set() speeds up stopword removal
punct_dict = dict((ord(punct), None) for punct in string.punctuation)

wnl = nltk.WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')


def remove_nl_cr(dataframe_col):
    """
    Remove new line and/or carriage return from dataframe column.

    Linux uses :code:`\\n` for a new-line, Windows `\\r\\n` and old Macs `\\r`

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception ("not a dataframe column")
    return dataframe_col.replace({'(\r\n|\r|\n)': ' '}, regex=True)


def remove_digits(dataframe_col):
    """
    Remove digits.

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'[0-9]+', '')


def remove_non_char(dataframe_col):
    """
    Remove non-alphabetic tokens:

     :code:`[#<>=.,;:$&*|?\'\"\-()%]`

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'[#<>=.,;:$&*|?\'\"\-()%]', ' ')


def custom_replace(dataframe_col, change_from='', change_to=''):
    """
    Replace tokens.

    :param dataframe_col: a single dataframe column
    :param change_from: string
    :param change_to: string
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(change_from, change_to, regex=True)


def remove_url(dataframe_col):
    """
    Remove hyperlink / url.

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'http\S+', '')


def remove_email(dataframe_col):
    """
    Remove email address.

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'\S*@\S*\s?', '')


def remove_consecutive_spaces(dataframe_col):
    """
    Remove consecutive white spaces.

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'\s+', ' ', regex=True)


def remove_repeating_letters(dataframe_col):
    """
    Remove repeating letters with a minimum threshold of 2.

    The threshold prevents repeated letters in names e.g. Aaron to be preserved.

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    min_threshold_rep = 2
    return dataframe_col.str.replace(r'(\w)\1{%d,}'%(min_threshold_rep-1), r'\1')


def remove_accented_chars(dataframe_col):
    """
    Remove accented characters.

    :param dataframe_col: a single dataframe column
    :return: a single dataframe column
    """
    # Convert the dataframe column to a list for faster searching.
    listed = dataframe_col.to_list()
    return [(unicodedata.normalize('NFKD', str(text))
                .encode('ascii', 'ignore')
                .decode('utf-8', 'ignore')) for text in listed]
    # return new_text


def remove_punctuation(text):
    """
    Remove punctuation.

    :param text:
    :return:
    """
    sent = text.translate(punct_dict)
    return sent


def remove_stopwords(text):
    """
    remove stopwords
    :param text:
    :return:
    """
    tokens = tokenizer.tokenize(str(text))
    filtered_words = [w for w in tokens
#                       if len(w) > 2
                      if not w in stopwords]
    filtered_words = [wnl.lemmatize(w) for w in filtered_words]
    return " ".join(filtered_words)


if __name__ == "__main__":
    pass