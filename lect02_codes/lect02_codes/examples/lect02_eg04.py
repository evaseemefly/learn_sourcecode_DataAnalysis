
# coding: utf-8

# # 常用的统计分布

# In[1]:

import pandas as pd
import numpy as np


# ## 1. 二项分布
# [numpy.random.binomial](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.binomial.html)<br/|>
# 从二项分布中采样

# In[10]:

# 1次试验中，成功的次数
np.random.binomial(1, 0.5)


# In[16]:

# 1000次试验中，成功的次数
print('1000次试验中，成功的次数: ', np.random.binomial(1000, 0.5))

# 1000次试验中，成功的概率
print('1000次试验中，成功的次数: ', np.random.binomial(1000, 0.5) / 1000)


# In[17]:

# 10000次试验中，成功的次数
print('10000次试验中，成功的次数: ', np.random.binomial(10000, 0.5))

# 10000次试验中，成功的概率
print('10000次试验中，成功的次数: ', np.random.binomial(10000, 0.5) / 10000)


# In[19]:

# 模拟100000次试验中，连续两次都是1的次数
n_events = 100000
events = np.random.binomial(1, 0.5, n_events)

two_in_a_row = 0
for i in range(1, n_events - 1):
    if events[i] == 1 and events[i - 1] == 1:
        two_in_a_row += 1
print('{}次投掷硬币，连续两次都是正面的次数{}'.format(n_events, two_in_a_row))


# ## 2. 正态分布
# (numpy.random.normal)[https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html]<br>
# 从正态分布中采样

# In[20]:

np.random.normal(loc=0.75)


# In[27]:

samples = np.random.normal(loc=0.75, size=1000)

print('期望：', np.mean(samples))
print('标准差：', np.std(samples))


# In[ ]:



