import pandas as Edd
# Reading the csv to the  code
df=Edd.read_csv('candle_clean_data.csv')
df.head()
df.tail()
df1=df.reset_index()['close']
df1


import matplotlib.pyplot as plt
import numpy as np
# Ndoplotter in mat by 
# visual with .ipynb
plt.plot(df1)
