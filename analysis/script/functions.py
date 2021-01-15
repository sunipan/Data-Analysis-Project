import pandas as pd

def load_and_process(directory):
    
    df1 = (pd.read_csv(directory, sep = ',\s', na_values = ['?'], engine = 'python')
          .drop(['Final Weight', 'Education-Num','Capital Gain', 'Capital Loss', 'Relationship'], axis = 1)
          .dropna()
          )
    return df1