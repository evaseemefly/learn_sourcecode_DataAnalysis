import random
import numpy as np
# 实现随机漫步的方式一
position=0
walk=[position]
steps=1000
for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)

# 实现随机漫步的方式二
nsteps=1000
draws=np.random.randint(0,2,size=nsteps)
steps=np.where(draws>0,1,-1)
# 求所有元素的累计和
# 数组当前值于之前值相加的和，组成一个新的数组
walk=steps.cumsum()
print(walk)
