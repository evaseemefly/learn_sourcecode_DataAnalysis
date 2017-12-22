import re
import os

files_list=[]
ignorefiles_list=[]
# 注意此处\D是非数字！
re_match=[r'^WL\d{4}.\d{5}$',r'^WS\d{4}.\d{5}$',r'^WV\d{4}.\d{5}$']
filename='WL1234.12345'
is_ok=re.match(r"^WL\d{4}.\d{5}$",filename)
def getmatchingFiles(path):
    # 当前路径下的目录
    year='2017'
    month='11'    
    start='01'
    end='30'
    '''
    在mac下：
    path：/Users/liusihan/Documents/GitHub/learn_sourcecode_DataAnalysis/codes_bymyself/data/sanya/perclock/
    source_dir：
    'perclock'
    '''
    source_dir=os.listdir(path)
    if year in source_dir:
        year_dir=os.path.join(path,'2017')
        month_dir=os.listdir(year_dir)        
        if month in month_dir:
            targetpath=os.path.join(year_dir,month)
            '''
            targetpath目录是到月的目录
            
            '''
            for root, dirs, files in os.walk(targetpath): 
                if len(dirs)==0: 
                    for temp_file in files:
                        ''' 
                        注意追加时不是所有的文件名都要追加

                        '''
                        str_file=temp_file.upper()
                        res_match_type = re.match('[a-zA-Z]{2}',str_file)
                        # 使用group匹配正则的匹配值
                        res_match_type=res_match_type.group()
                        print(res_match_type)
                        is_matching=False
                        # 有符合正则条件的放入忽略集合中
                        for temp_match in re_match:
                            res_match=re.match(temp_match,str_file)
                            if res_match!=None:
                                is_matching=True
                                ignorefiles_list.append(os.path.join(root, temp_file))
                                print("****%s已追加至忽略集合中"%os.path.join(root, temp_file))
                                break;
                        # 不匹配的才放入文件集合中
                        if is_matching==False:   
                            files_list.append(os.path.join(root, temp_file))
                            print("%s已追加"%os.path.join(root, temp_file))
                print("-----------")
                
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

# path=r'E:\03协同开发\99学习\05数据分析\网课源码\learn_sourcecode_DataAnalysis\codes_bymyself\data\sanya\perclock'

path=r'/Users/liusihan/Documents/GitHub/learn_sourcecode_DataAnalysis/codes_bymyself/data/sanya/perclock/'
getmatchingFiles(path)