#!/usr/bin/env python3

def search(df, dataframe_col = '', tok = ''):
    """
    Search dataframe column and return rows that contain the specified token.

    :param df: dataframe
    :param dataframe_col: string
    :param tok: string
    :return: dataframe
    """
    df = df[df.index.notnull()]
    # Convert the dataframe column to a list for faster searching.
    listed = df[dataframe_col].to_list()
    df['search_flag'] = [tok in str(i) for i in listed]
    return df[df.search_flag==True].drop('search_flag', axis = 1)


if __name__ == "__main__":
    pass