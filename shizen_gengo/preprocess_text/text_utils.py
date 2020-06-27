#!/usr/bin/env python3

import string
import unicodedata
import nltk
from nltk import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english")) # set() speeds up stopword removal
punct_dict = dict((ord(punct), None) for punct in string.punctuation)

wnl = nltk.WordNetLemmatizer()
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')


def remove_nl_cr(dataframe_col):
    """
    remove new line and/or carriage return from dataframe column.

    Linux uses :code:`\\n` for a new-line, Windows `\\r\\n` and old Macs `\\r`

    :param dataframe_col:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception ("not a dataframe column")
    return dataframe_col.replace({'(\r\n|\r|\n)': ' '}, regex=True)


def remove_digits(dataframe_col):
    """
    remove digits

    :param dataframe_col:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'[0-9]+', '')


def remove_non_char(dataframe_col):
    """
    remove non-alphabetic tokens :code:`[#<>=.,;:$&*|?\'\"\-()%]`
    :param dataframe_col:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'[#<>=.,;:$&*|?\'\"\-()%]', ' ')


def custom_replace(dataframe_col, change_from='', change_to=''):
    """
    replace token

    :param dataframe_col:
    :param change_from:
    :param change_to:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(change_from, change_to, regex=True)


def remove_url(dataframe_col):
    """
    remove hyperlink
    :param dataframe_col:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'http\S+', '')


def remove_email(dataframe_col):
    """
    remove email address

    :param dataframe_col:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'\S*@\S*\s?', '')


def remove_consecutive_spaces(dataframe_col):
    """
    remove consecutive white spaces

    :param dataframe_col:
    :return:
    """
    if dataframe_col.ndim > 1:
        raise Exception("not a dataframe column")
    return dataframe_col.str.replace(r'\s+', ' ', regex=True)


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


def remove_accented_chars(text):
    """
    remove accented characters

    :param text:
    :return:
    """
    new_text = (unicodedata.normalize('NFKD', str(text))
                .encode('ascii', 'ignore')
                .decode('utf-8', 'ignore'))
    return new_text


def remove_punctuation(text):
    """
    remove punctuation

    :param text:
    :return:
    """
    sent = text.translate(punct_dict)
    return sent

### OLD ###

# def get_stanford_stopwords():
#     url = 'https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/data/edu/' \
#           'stanford/nlp/patterns/surface/stopwords.txt'
#     response = requests.get(url)
#     stopwords = response.text
#     # print(stopwords[:20])
#     return stopwords

# def nltk_tag_to_wordnet_tag(nltk_tag):
#     if nltk_tag.startswith('J'):
#         return wordnet.ADJ
#     elif nltk_tag.startswith('V'):
#         return wordnet.VERB
#     elif nltk_tag.startswith('N'):
#         return wordnet.NOUN
#     elif nltk_tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return None
#
# def lemmatize_sentence(sentence):
#
#     # tokenize the sentence and find the POS tag for each token
#     nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
#
#     # tuple of (token, wordnet_tag)
#     wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged) # IS A map object
#     # print(list(wordnet_tagged))
#
#     lemmatized_sentence = []
#     for word, tag in list(wordnet_tagged):
#         # print(word, tag, wnl.lemmatize(word, tag))
#         try:
#             lemmatized_sentence.append(wnl.lemmatize(word, tag))
#         except:
#             lemmatized_sentence.append(word)
#     # print(lemmatized_sentence)
#     return " ".join(lemmatized_sentence)
#
# def sent_tokenize(raw):
#     # converts to list of sentences
#     sents = nltk.sent_tokenize(raw)
#     return sents
#
# def pre_process(raw):
#     corpus = []
#     sents = sent_tokenize(raw)
#     for sent in sents:
#         # lower case and remove special characters\\whitespaces
#         sent = re.sub(r'[^0-9a-zA-Z\s]', '', sent, re.I | re.A)
#         sent = sent.lower()
#         sent = sent.strip()
#
#         text = lemmatize_sentence(sent)
#         text = remove_stopwords(text)
#     #     text = remove_punctuation_sentence(text)
#         corpus.append(text)
#         # print(text)
#     return corpus