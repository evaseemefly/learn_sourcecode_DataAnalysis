
# coding: utf-8

# ## 本示例用来尝试根据指定的时间范围获取该时间范围及指定海洋站对应的路径

#%%
print("123")

#%%
import os
path=r'/Users/liusihan/Documents/GitHub/learn_sourcecode_DataAnalysis/codes_bymyself/data'
# 判断指定路径是否存在
if os.path.isdir(path):    
    for root, dirs, files in os.walk(path): 
        print("-----------")
        print("root:%s"%root)
        print("dirs:%s"%dirs)
        print("files:%s"%files)
#%%

# In[3]:

#%%
os.listdir(path)


# In[14]:


import re
import os

files=[]
def getmatchingFiles(path):
    # 当前路径下的目录
    year='2017'
    month='11'    
    start='01'
    end='30'
    source_dir=os.listdir(path)
    if year in source_dir:
        year_dir=os.path.join(path,'2017')
        month_dir=os.listdir(year_dir)        
        if month in month_dir:
            targetpath=os.path.join(year_dir,month)
            for root, dirs, files in os.walk(targetpath): 
                print("-----------")
                print("root:%s"%root)
                print("dirs:%s"%dirs)
                print("files:%s"%files)
                
#     for temp in source_dir:
#          # 找到指定年份
#         # 判断是否为年份
#         # 四位数字
#         res=re.match(r"\d{4}",source_dir)
        
#     print(source_dir)
#     if len(source_dir)==1:    
       
#         for year in res:
            
#         if res!=None:
#             # 若是四位数字再
#             print("匹配")
#         print(res)

path=r'E:\03协同开发\99学习\05数据分析\网课源码\learn_sourcecode_DataAnalysis\codes_bymyself\data\sanya\perclock'
getmatchingFiles(path)

