
# coding: utf-8

# # 透视表

# In[4]:

import pandas as pd
import numpy as np

cars_df = pd.read_csv('cars.csv')
cars_df.head()


# In[6]:

# 我们想要比较不同年份的不同厂商的车，在电池方面的不同
cars_df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)


# In[8]:

# 我们想要比较不同年份的不同厂商的车，在电池方面的不同
# 可以使用多个聚合函数
cars_df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean, np.min])


# In[9]:

# 我们想要比较不同年份的不同厂商的车，在电池方面的不同
# 可以使用多个聚合函数
cars_df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean, np.min], margins=True)


# In[ ]:



