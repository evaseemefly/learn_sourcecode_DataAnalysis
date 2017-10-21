
# coding: utf-8

# # Pandas简单数据分析

# ## 1. 创建Series
import pandas as pd

countries = ['中国', '美国', '澳大利亚']
# 使用series后会自动加上index
countries_s = pd.Series(countries)
print(type(countries_s))
print(countries_s)


# In[4]:


numbers = [4, 5, 6]
print(pd.Series(numbers))


# In[9]:

# 若将上面转成字典
# name是key value是value
country_dicts = {'CH': '中国',
                'US': '美国',
                'AU': '澳大利亚'}
country_dict_s = pd.Series(country_dicts)
print(country_dict_s)
print(country_dict_s.index)


# 2. 处理缺失数据
countries = ['中国', '美国', '澳大利亚', None]
print(pd.Series(countries))

numbers = [4, 5, 6, None]
print(pd.Series(numbers))


# ## 3. Series 索引
country_dicts = {'CH': '中国',
                'US': '美国',
                'AU': '澳大利亚'}

country_dict_s = pd.Series(country_dicts)
print(country_dict_s)

# iloc进行索引（整型索引位置-index）
# iloc必须传整型
print('iloc:', country_dict_s.iloc[1])
# 使用索引名称 name
print('loc:', country_dict_s.loc['US'])
print('[]:', country_dict_s['US'])

# 0与2位置
# 使用两个[]代表里面的[]是列表
print('iloc:\n', country_dict_s.iloc[[0, 2]])
print()
print('loc:\n', country_dict_s.loc[['US', 'AU']])


# ## 4.  向量化操作

# In[20]:


import numpy as np

s = pd.Series(np.random.randint(0, 1000, 10000))
print(s.head())
print(len(s))


# In[21]:


get_ipython().run_cell_magic('timeit', '-n 100', 'total = 0\nfor item in s:\n    total += item')


# In[22]:


get_ipython().run_cell_magic('timeit', '-n 100', 'total = np.sum(s)')


# In[33]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0, 1000, 10000))\nfor label, value in s.iteritems():\n    s.loc[label] = value + 2')


# In[34]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0, 1000, 10000))\ns += 2')

