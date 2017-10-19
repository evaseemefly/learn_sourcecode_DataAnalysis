
# coding: utf-8

# # 科学计算库NumPy

# In[1]:


import numpy as np


# ## 1. 创建Array

# In[4]:


my_list = [1, 2, 3]
x = np.array(my_list)

print('列表：', my_list)
print('Array: ', x)


# In[6]:


m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)
print('shape: ', m.shape)


# In[7]:


n = np.arange(0, 30, 2)
print(n)


# In[9]:


n = n.reshape(3, 5)
print('reshape后: ')
print(n)


# In[15]:


print('ones:\n', np.ones((3, 2)))
print('zeros:\n', np.zeros((3, 2)))
print('eye:\n', np.eye(3))
print('diag:\n', np.diag(my_list))


# In[17]:


print('*操作：\n', np.array([1, 2, 3] * 3))
print('repeat：\n', np.repeat([1, 2, 3], 3))


# In[25]:


p1 = np.ones((3, 3))
p2 = np.arange(9).reshape(3, 3)
print('纵向叠加: \n', np.vstack((p1, p2)))
print('横向叠加: \n', np.hstack((p1, p2)))


# ## 2. Array操作

# In[26]:


print('p1: \n', p1)
print('p2: \n', p2)

print('p1 + p2 = \n', p1 + p2)
print('p1 * p2 = \n', p1 * p2)
print('p2^2 = \n', p2 ** 2)
print('p1.p2 = \n', p1.dot(p2))


# In[29]:


p3 = np.arange(6).reshape(2, 3)
print('p3形状: ', p3.shape)
print(p3)
p4 = p3.T
print('转置后p3形状: ', p4.shape)
print(p4)


# In[30]:


print('p3数据类型:', p3.dtype)
print(p3)

p5 = p3.astype('float')
print('p5数据类型:', p5.dtype)
print(p5)


# In[34]:


a = np.array([-4, -2, 1, 3, 5])
print('sum: ', a.sum())
print('min: ', a.min())
print('max: ', a.max())
print('mean: ', a.mean())
print('std: ', a.std())
print('argmax: ', a.argmax())
print('argmin: ', a.argmin())


# ## 3. 索引与切片

# In[39]:


# 一维array
s = np.arange(13) ** 2
print('s: ', s)
print('s[0]: ', s[0])
print('s[4]: ', s[4])
print('s[0:3]: ', s[0:3])
print('s[[0, 2, 4]]: ', s[[0, 2, 4]])


# In[43]:


# 二维array
r = np.arange(36).reshape((6, 6))
print('r: \n', r)
print('r[2, 2]: \n', r[2, 2])
print('r[3, 3:6]: \n', r[3, 3:6])


# In[46]:


# 过滤
print(r[r > 30])

# 将大于30的数赋值为30
r[r > 30] = 30
print(r)


# In[48]:


# copy()操作
r2 = r[:3, :3]
print(r2)


# In[49]:


# 将r2内容设置为0
# 注意会将原始的值也同时进行修改
# 可以使用copy
r2[:] = 0
# 查看r的内容
print(r)


# In[50]:


r3 = r.copy()
r3[:] = 0
print(r)


# ## 4. 遍历 Array

# In[51]:


t = np.random.randint(0, 10, (4, 3))
print(t)


# In[53]:


for row in t:
    print(row)


# In[54]:


# 使用enumerate()
for i, row in enumerate(t):
    print('row {} is {}'.format(i, row))


# In[55]:


t2 = t ** 2
print(t2)


# In[56]:


# 使用zip对两个array进行遍历计算
for i, j in zip(t, t2):
    print('{} + {} = {}'.format(i, j, i + j))

