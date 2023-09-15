import pandas as pd
import numpy as np
from IPython.display import display

def get_df_summary(df:pd.DataFrame):
    print('The first 5 rows of dataset is shown below')
    display(df.head())
    print('-'*50)
    print(f'The shape of dataset is: {df.shape[0]} rows x {df.shape[1]} columns')
    print('-'*50)
    print('df column information')
    print(df.info())
    print('-'*50)
    print('Number of missing values in the dataset: ',df.isnull().sum().sum())
    if df.isnull().sum().sum() >0:
        print(df.isnull().sum())

    print('-'*50)
    print('statistical summary')
    display(round(df.describe(),2))
    
    print('-'*50)
    
    obj_cols = [str(col) for col in df.columns if df[col].dtype=='object']
    if len(obj_cols)>0:
        print('Following shows the distinct values of text labels in each columns:')
        for col in [str(col) for col in df.columns if df[col].dtype=='object']:
            print(f'distinct values of {col}: ',set(df[col]))
    else:
        print('There is no text value column.')
