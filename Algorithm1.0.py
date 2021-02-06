import pandas as pd
from scipy.interpolate import interp1d
import math


S=pd.read_csv(r"C:\Users\Alexander Asriyan\Desktop\MCE\MakeaFriend\balldata\ball_data.csv")


xyz=S.to_numpy()


x = []
y = []
z = []

j=len(xyz)

arr1 = []

for i in range(0,j):  
    arr1=xyz[i]
    x.append(float(arr1[0]))
    z.append(float(arr1[1]))
    y.append(float(arr1[2]))

F1=interp1d(x, y, kind = 'linear')

k=(F1(x[4])-F1(x[5]))/(x[4]-x[5])

b=F1(x[5])-k*x[5]

x1=[]
y1=[]

for i in range(0,j):
    x1.append(math.sqrt(y[i]**2+(x[i]+b/k)**2))
    y1.append(z[i])
    

F2=interp1d(y1, x1, kind='quadratic')

x10=F2(0)

x0=(k*x10*math.sqrt(1+k**2)-b*(k**2+1))/(k*(1+k**2))
y0=F1(x0)

print(x0)
print(y0)



