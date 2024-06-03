from data_import import *

PATH = 'students.csv'

def test_csv_tokenize():
    tokens = csv_to_tokens(PATH)
    return tokens

def test_token_to_dict(tokens):
    df_dict = test_csv_tokenize()
    return df_dict

def test_csv_to_df():
    dataframe = csv_to_dataframe(PATH)
    return dataframe





if __name__ == '__main__':
    tokens = test_csv_tokenize()
    
    data_dict = test_token_to_dict(tokens)

    dataframe = test_csv_to_df()
