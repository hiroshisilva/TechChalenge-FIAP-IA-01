import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    if 'Unnamed: 32' in df.columns:
        df.drop(columns=['Unnamed: 32'], axis=1, inplace=True)
    encoder = OrdinalEncoder(categories=[['M', 'B']])
    df['diagnosis'] = encoder.fit_transform(df[['diagnosis']])
    return df


def analysis_data(df):
  pd.set_option('display.max_columns', None)
  df.head()

def verify_data_nulls(df):
  df.shape()


