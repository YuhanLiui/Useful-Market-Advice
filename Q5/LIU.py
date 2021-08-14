import sklearn
import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('C:/Users/UniqueTropic/Experiment/DataSet/customer_data_large.csv')
data.drop('Unnamed: 0',axis=1,inplace=True)
data.drop('0', axis=1, inplace=True)
data.drop('1', axis=1, inplace=True)
data.columns = ['SHOP_DATE', 'SHOP_WEEKDAY', 'SHOP_HOUR', 'QUANTITY',
                'SPEND', 'PRODUCT_CODE', 'PRODUCT_CODE10', 'PRODUCT_CODE20', 'PRODUCT_CODE30', 'PRODUCT_CODE40', 'CUSTOMER_CODE', 'CUST_PRICE_SENSITIVITY', 'CUST_LIFESTAGE', 'BASKET_ID', 'BASKET_SIZE', 'BASKET_PRICE_SENSITIVITY', 'BASKET_TYPE', 'BASKET_DOMINANT_MISSION', 'STORE_CODE', 'STORE_FORMAT', 'STORE_REGION']
data = data.dropna()
df = pd.DataFrame(data,columns = data.columns)

df1 = df[['BASKET_ID','PRODUCT_CODE']]
df1.reset_index(inplace = True )
gb = df1.groupby('BASKET_ID')
result = gb['PRODUCT_CODE'].unique()
df2 = result.to_frame()
df2.to_excel('C:/Users/UniqueTropic/Experiment/DataSet/1.xls')