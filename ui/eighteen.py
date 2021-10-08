import numpy as np
import h5py
import os

f = h5py.File('eighteen.h5','r')

#print(f['data'].shape)
#print(type(f['data'][0,0,0,0,0]))
d = f['data'][0,...,0]
#print(d[0])
#data = np.random.rand(100,110,120)

#d = (data>0.5)*1

#d = np.array([[[0,0],[0,0],[0,0]],[[0,0],[0,1],[0,0]]])

#print(np.where(d==1))

print(d.shape)

maxR=15

#out = np.zeros(d.shape) #初始化输出
out = np.ones(d.shape)*maxR #初始化输出

print(out.shape)

for i1 in range(d.shape[0]):
    print(i1)
    for j1 in range(d.shape[1]):
        print(str(d.shape) +' 进度: ' +  str(i1) + ' ' + str(j1))
        for k1 in range(d.shape[2]):
            if d[i1,j1,k1] == 0:
                out[i1,j1,k1] = 0 #当前位置为0时，输出0
            elif d[i1,j1,k1] == 2:
                out[i1,j1,k1] = 1 #当前位置为2时，输出1
            else: #当前位置为1时，输出距0的距离
                tmp = np.zeros(d.shape) # 用于记录已计算过的点
                tmp_distance = np.ones(d.shape)*100000000000000   #记录距离
                #for m in range(1,(int)((d.shape[0]**2+d.shape[1]**2+d.shape[2]**2)**0.5)):    #m为球半径
                for m in range(1,(int)(maxR)):    #m为球半径
                    for i2 in range(i1-m,i1+m+1):
                        if i2>=0 and i2<d.shape[0]:
                            for j2 in range(j1-m,j1+m+1):
                                if j2>=0 and j2<d.shape[1]:
                                    for k2 in range(k1-m,k1+m+1):
                                        if k2>=0 and k2<d.shape[2]:
                                            if tmp[i2,j2,k2] == 0 and d[i2,j2,k2] == 0 and (i2-i1)**2+(j2-j1)**2+(k2-k1)**2<=m**2:
                                                tmp_distance[i2,j2,k2] = ((i2-i1)**2+(j2-j1)**2+(k2-k1)**2)**0.5
                                                #print(tmp_distance[i2,j2,k2])
                                                tmp[i2,j2,k2] = 1
                    min_dis = np.min(tmp_distance)
                    #print(min_dis)
                    if min_dis<100000000000000:
                        #print(np.where(tmp_distance==min_dis))
                        #print(min_dis)
                        out[i1,j1,k1] = min_dis + 1
                        break
#输出整数，四舍五入
if not os.path.exists('1.h5'):
    with h5py.File('1.h5',mode='w') as file:
        file['data'] = np.around(out).astype(np.uint8).reshape(f['data'].shape)
        
#输出小数

if not os.path.exists('2.h5'):
    with h5py.File('2.h5',mode='w') as file:
        file['data'] = out.reshape(f['data'].shape)
