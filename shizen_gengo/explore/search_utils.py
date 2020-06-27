#!/usr/bin/env python3

def search(df, dataframe_col, tok = ''):
    """
    This functions converts the dataframe column to a list for faster searching.

    :param df:
    :param dataframe_col:
    :param tok:
    :return:
    """
    df = df[df.index.notnull()]
    listed = df[dataframe_col].to_list()
    df['search_flag'] = [tok in str(i) for i in listed]
    return df[df.search_flag==True][dataframe_col].to_frame()


# def search_window(dataframe_col, token = ''):
#     if dataframe_col.ndim == 1:
#         raise Exception ("not a dataframe")
#     print(len(dataframe_col))
#     dataframe_col.replace("", np.nan, inplace=True)
#     dataframe_col = dataframe_col.dropna()
#     print(len(dataframe_col))
#     pat = r'(?P<before>(?:\w+\W+){,8})(?i)' + token + r'\W+(?P<after>(?:\w+\W+){,8})'
#     res = dataframe_col.str.extract(pat, expand=False)
#     res = res.dropna()
#     # print(len(new))
#     return res.sample(min(10, len(res)))