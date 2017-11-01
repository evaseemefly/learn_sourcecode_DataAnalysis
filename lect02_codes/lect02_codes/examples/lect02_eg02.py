
# coding: utf-8

# # 数据合并及分组

# ## 1. 数据合并

# In[1]:

import pandas as pd

staff_df = pd.DataFrame([{'姓名': '张三', '部门': '研发部'},
                        {'姓名': '李四', '部门': '财务部'},
                        {'姓名': '赵六', '部门': '市场部'}])


student_df = pd.DataFrame([{'姓名': '张三', '专业': '计算机'},
                        {'姓名': '李四', '专业': '会计'},
                        {'姓名': '王五', '专业': '市场营销'}])

print(staff_df)
print()
print(student_df)


# In[7]:

pd.merge(staff_df, student_df, how='outer', on='姓名')
# 或者
# staff_df.merge(student_df, how='outer', on='姓名')


# In[10]:

pd.merge(staff_df, student_df, how='inner', on='姓名')
# 或者
# staff_df.merge(student_df, how='inner', on='姓名')


# In[13]:

pd.merge(staff_df, student_df, how='left', on='姓名')
# 或者
# staff_df.merge(student_df, how='left', on='姓名')


# In[20]:

pd.merge(staff_df, student_df, how='right', on='姓名')
# 或者
# staff_df.merge(student_df, how='right', on='姓名')


# In[21]:

# 也可以按索引进行合并
staff_df.set_index('姓名', inplace=True)
student_df.set_index('姓名', inplace=True)
print(staff_df)
print(student_df)


# In[23]:

pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
# 或者
# staff_df.merge(student_df, how='left', left_index=True, right_index=True)


# In[24]:

# 当数据中的列名不同时，使用left_on，right_on
staff_df.reset_index(inplace=True)
student_df.reset_index(inplace=True)
print(staff_df)
print(student_df)


# In[26]:

staff_df.rename(columns={'姓名': '员工姓名'}, inplace=True)
student_df.rename(columns={'姓名': '学生姓名'}, inplace=True)
print(staff_df)
print(student_df)


# In[28]:

pd.merge(staff_df, student_df, how='left', left_on='员工姓名', right_on='学生姓名')


# In[37]:

# 如果两个数据中包含有相同的列名（不是要合并的列）时，merge会自动加后缀作为区别
staff_df['地址'] = ['天津', '北京', '上海']
student_df['地址'] = ['天津', '上海', '广州']
print(staff_df)
print(student_df)


# In[38]:

pd.merge(staff_df, student_df, how='left', left_on='员工姓名', right_on='学生姓名')


# In[39]:

# 也可指定后缀名称
pd.merge(staff_df, student_df, how='left', left_on='员工姓名', right_on='学生姓名', suffixes=('(公司)', '(家乡)'))


# In[41]:

# 也可以指定多列进行合并，找出同一个人的工作地址和家乡地址相同的记录
pd.merge(staff_df, student_df, how='inner', left_on=['员工姓名', '地址'], right_on=['学生姓名', '地址'])


# In[45]:

# apply使用
# 获取姓
staff_df['员工姓名'].apply(lambda x: x[0])


# In[46]:

# 获取名
staff_df['员工姓名'].apply(lambda x: x[1:])


# In[47]:

# 结果合并
staff_df.loc[:, '姓'] = staff_df['员工姓名'].apply(lambda x: x[0])
staff_df.loc[:, '名'] = staff_df['员工姓名'].apply(lambda x: x[1:])
print(staff_df)


# ## 2. 数据分组

# In[21]:

report_data = pd.read_csv('./2015.csv')
report_data.head()


# In[8]:

#groupby()
grouped = report_data.groupby('Region')
print(type(grouped))


# In[9]:

grouped['Happiness Score'].mean()


# In[10]:

grouped.size()


# In[12]:

# 迭代groupby对象
for group, frame in grouped:
    mean_score = frame['Happiness Score'].mean()
    max_score = frame['Happiness Score'].max()
    min_score = frame['Happiness Score'].min()
    print('{}地区的平均幸福指数：{}，最高幸福指数：{}，最低幸福指数{}'.format(group, mean_score, max_score, min_score))


# In[32]:

# 自定义函数进行分组
# 按照幸福指数排名进行划分，1-10, 10-20, >20
# 如果自定义函数，操作针对的是index
report_data2 = report_data.set_index('Happiness Rank')

def get_rank_group(rank):
    rank_group = ''
    if rank <= 10:
        rank_group = '0 -- 10'
    elif rank <= 20:
        rank_group = '10 -- 20'
    else:
        rank_group = '> 20'
    return rank_group

grouped = report_data2.groupby(get_rank_group)
for group, frame in grouped:
    print('{}分组的数据个数：{}'.format(group, len(frame)))


# In[35]:

# 实际项目中，通常可以先人为构造出一个分组列，然后再进行groupby

# 按照score的整数部分进行分组
# 按照幸福指数排名进行划分，1-10, 10-20, >20
# 如果自定义函数，操作针对的是index
report_data['score group'] = report_data['Happiness Score'].apply(lambda score: int(score))

grouped = report_data.groupby('score group')
for group, frame in grouped:
    print('幸福指数整数部分为{}的分组数据个数：{}'.format(group, len(frame)))


# In[41]:

import numpy as np

grouped.agg({'Happiness Score': np.mean, 'Happiness Rank': np.max})


# In[44]:

grouped['Happiness Score'].agg([np.mean, np.max, np.min, np.std])


# In[ ]:



