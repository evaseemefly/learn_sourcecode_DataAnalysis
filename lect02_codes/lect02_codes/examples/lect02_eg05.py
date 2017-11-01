
# coding: utf-8

# # 使用Python进行假设检验

# In[1]:

import pandas as pd


# In[4]:

grades_df = pd.read_csv('grades.csv')
grades_df.head()


# In[7]:

grades_df.info()


# In[8]:

early_submission = grades_df[grades_df['assignment1_submission'] <= '2015-12-31']
late_submission = grades_df[grades_df['assignment1_submission'] > '2015-12-31']


# In[9]:

early_submission.mean()


# In[10]:

late_submission.mean()


# [scipy.stats.ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

# In[15]:

from scipy import stats
# 使用t检验来比较两个总体是否有显著差异，即：早提交作业的学生与晚提交作业的学生成绩是否有显著差异
# 零假设：早提交的学生总体和晚提交的学生总体没有显著差异
# 备择假设：两个总体有显著差异
# 构造一个与此相关的统计量，如果该统计量非常的大（即已经超过了一定的临界值），即p-value>alpha
# 则可以认为这种差异并不仅仅是由抽样误差带来的，因此我们可以拒绝原假设，认为两个总体有显著差异。


# In[11]:

stats.ttest_ind(early_submission['assignment1_grade'], late_submission['assignment1_grade'])
# pvalue=0.16，表示两个总体在assignment1上的成绩没有显著差异的概率是0.16>0.05，小概率事件没有发生，不能拒绝原假设


# In[12]:

stats.ttest_ind(early_submission['assignment2_grade'], late_submission['assignment2_grade'])


# In[19]:

stats.ttest_ind(early_submission['assignment6_grade'], late_submission['assignment6_grade'])


# In[ ]:




# In[ ]:



