import numpy as np
import pandas
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr
from pprint import pprint

index = ['datetime', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']
df_dust = pandas.read_csv('./data/dust.csv', index_col='datetime')
df_traffic = pandas.read_csv('./data/traffic.csv', index_col='datetime')

df_SO2 = pandas.DataFrame(df_dust['SO2'], columns=['SO2'])
'''
#pprint(df_SO2)
np.savetxt('./result.csv', cosine_similarity(df_traffic, df_SO2), delimiter=',')
'''
corr, p_value = pearsonr(df_traffic, df_SO2)
pprint(corr)
