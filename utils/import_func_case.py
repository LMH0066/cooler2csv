import pandas as pd


def process(dataframe: pd.DataFrame):
    dataframe = dataframe[['chrom1', 'chrom2', 'start1', 'end1', 'start2', 'end2', 'count']]
    dataframe['chrom1'] = dataframe['chrom1'].str[3:]
    dataframe['chrom2'] = dataframe['chrom2'].str[3:]
    dataframe.rename(columns={'chrom1':'chr1', 'chrom2':'chr2'}, inplace=True)
    return dataframe