
# coding: utf-8

# # Pandas进阶及技巧

# ## 1. 创建Pandas

# In[77]:

import pandas as pd

country1 = pd.Series({'Name': '中国',
                    'Language': 'Chinese',
                    'Area': '9.597M km2',
                     'Happiness Rank': 79})

country2 = pd.Series({'Name': '美国',
                    'Language': 'English (US)',
                    'Area': '9.834M km2',
                     'Happiness Rank': 14})

country3 = pd.Series({'Name': '澳大利亚',
                    'Language': 'English (AU)',
                    'Area': '7.692M km2',
                     'Happiness Rank': 9})

df = pd.DataFrame([country1, country2, country3], index=['CH', 'US', 'AU'])


# In[78]:

# 注意在jupyter中使用print和不使用print的区别
print(df)
df


# In[79]:

# 添加数据
# 如果个数小于要求的个数，会自动进行“广播”操作
# 如果大于要求的个数，会报错
df['Location'] = '地球'
print(df)

df['Region'] = ['亚洲', '北美洲', '大洋洲']
print(df)
df


# ## 2. Pandas索引

# In[80]:

# 行索引
print('loc:')
print(df.loc['CH'])
print(type(df.loc['CH']))

print('iloc:')
print(df.iloc[1])


# In[81]:

# 列索引
print(df['Area'])
print(type(df['Area']))


# In[82]:

# 获取不连续的列数据
print(df[['Name', 'Area']])


# In[83]:

# 混合索引
# 注意写法上的区别
print('先取出列，再取行：')
print(df['Area']['CH'])
print(df['Area'].loc['CH'])
print(df['Area'].iloc[0])

print('先取出行，再取列：')
print(df.loc['CH']['Area'])
print(df.iloc[0]['Area'])


# In[84]:

# 转换行和列
print(df.T)


# ## 3. 删除数据

# In[85]:

print(df.drop(['CH']))
# 注意drop操作只是将修改后的数据copy一份，而不会对原始数据进行修改
print(df)


# In[86]:

print(df.drop(['CH'], inplace=True))
# 如果使用了inplace=True，会在原始数据上进行修改，同时不会返回一个copy
print(df)


# In[87]:

#  如果需要删除列，需要指定axis=1
print(df.drop(['Area'], axis=1))
print(df)


# In[88]:

# 也可直接使用del关键字
del df['Name']
print(df)


# ## 4. DataFrame的操作与加载

# In[74]:

# 注意从DataFrame中取出的数据进行操作后，会对原始数据产生影响
ranks = df['Happiness Rank']
ranks += 2
print(ranks)
print(df)


# In[75]:

# 注意从DataFrame中取出的数据进行操作后，会对原始数据产生影响
# 安全的操作是使用copy()
ranks = df['Happiness Rank'].copy()
ranks += 2
print(ranks)
print(df)


# In[124]:

# 加载csv文件数据
reprot_2015_df = pd.read_csv('./2015.csv')
print('2015年数据预览：')
#print(reprot_2015_df.head())
reprot_2015_df.head()


# In[94]:

print(reprot_2015_df.info())


# In[98]:

# 使用index_col指定索引列
# 使用usecols指定需要读取的列
reprot_2016_df = pd.read_csv('./2016.csv', 
                             index_col='Country',
                             usecols=['Country', 'Happiness Rank', 'Happiness Score', 'Region'])
# 数据预览
reprot_2016_df.head()


# In[100]:

print('列名(column)：', reprot_2016_df.columns)
print('行名(index)：', reprot_2016_df.index)


# In[104]:

# 注意index是不可变的
reprot_2016_df.index[0] = '丹麦'


# In[120]:

# 重置index
# 注意inplace加与不加的区别
reprot_2016_df.reset_index().head()


# In[118]:

# 重命名列名
reprot_2016_df.rename(columns={'Region': '地区', 'Hapiness Rank': '排名', 'Hapiness Score': '幸福指数'})
reprot_2016_df.head()


# In[106]:

# 重命名列名，注意inplace的使用
reprot_2016_df.rename(columns={'Region': '地区', 'Happiness Rank': '排名', 'Happiness Score': '幸福指数'},
                     inplace=True)
reprot_2016_df.head()


# ## 5. Boolean Mask

# In[111]:

# 过滤 Western Europe 地区的国家
only_western_europe = reprot_2016_df['地区'] == 'Western Europe'
only_western_europe


# In[112]:

# 过滤 Western Europe 地区的国家
# 并且排名在10之外
only_western_europe_10 = (reprot_2016_df['地区'] == 'Western Europe') & (reprot_2016_df['排名'] > 10)
only_western_europe_10


# In[114]:

# 叠加 boolean mask 得到最终结果
reprot_2016_df[only_western_europe_10]


# In[115]:

# 熟练以后可以写在一行中
reprot_2016_df[(reprot_2016_df['地区'] == 'Western Europe') & (reprot_2016_df['排名'] > 10)]


# ## 6. 层级索引

# In[121]:

reprot_2015_df.head()


# In[147]:

# 设置层级索引
report_2015_df2 = reprot_2015_df.set_index(['Region', 'Country'])
report_2015_df2.head(20)


# In[133]:

# level0 索引
report_2015_df2.loc['Western Europe']


# In[134]:

# 两层索引
report_2015_df2.loc['Western Europe', 'Switzerland']


# In[148]:

# 交换分层顺序
report_2015_df2.swaplevel()


# In[150]:

# 排序分层
report_2015_df2.sort_index(level=0)


# ## 7. 数据清洗

# In[157]:

log_data = pd.read_csv('log.csv')
log_data


# In[158]:

log_data.set_index(['time', 'user'], inplace=True)
log_data.sort_index(inplace=True)
log_data


# In[159]:

log_data.fillna(0)


# In[160]:

log_data.dropna()


# In[161]:

log_data.ffill()


# In[162]:

log_data.bfill()


# In[ ]:



