import matplotlib.pyplot as plt
import numpy as np
 
x=[1,2,3,4,5,6]
y=[5,3,67,1,23,2]
 
 
# 进行多项式拟合（这里选取3次多项式拟合）
# z = np.polyfit(x, y, 1) # 用1次多项式拟合
# z = np.polyfit(x, y, 2) # 用2次多项式拟合
z = np.polyfit(x, y, 3) # 用3次多项式拟合
 
 
# 获取拟合后的多项式
p = np.poly1d(z)
print(p)  # 在屏幕上打印拟合多项式
 
def print_polynomial(poly:np.poly1d):
    cnt=list(poly).__len__()
    for co in list(poly):
        cnt-=1
        if cnt>0:
            print("%.12f*x^%d+"%(co,cnt),end="")
        else:
            print("%.12f"%(co),end="")
            

print_polynomial(p)
    
# 计算拟合后的y值
yvals=p(x)
 
 
 
# 计算拟合多项式的极值点。
peak = np.polyder(p, 1)
print(peak.r)
 
 
# 画图对比分析
plot1 = plt.plot(x, y, '*', label='original values', color='dimgray')
plot2 = plt.plot(x, yvals, '#000000', label='fitting values', linewidth=2)
 
plt.xlabel('time points')
plt.ylabel('values')
plt.legend(loc="best")  # 指定legend的位置,读者可以自己help它的用法
plt.title('fitting diagram')
plt.show()
 
 