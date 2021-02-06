import pandas as pd
from scipy.interpolate import interp1d
import math


S=pd.read_csv(r"C:\Users\Alexander Asriyan\Desktop\MCE\MakeaFriend\balldata\ball_data.csv")

#reads the csv file

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
    
#creates the coordinate array

F1=interp1d(x, y, kind = 'linear')

#trajectory projection linear function in the OXY plane

k=(F1(x[4])-F1(x[5]))/(x[4]-x[5])

b=F1(x[5])-k*x[5]

# gives k and b values for y=kx+b F1 function
x1=[]
y1=[]

for i in range(0,j):
    x1.append(math.sqrt(y[i]**2+(x[i]+b/k)**2))
    y1.append(z[i])
    
#creates the 2D coordinate arrray in OXY(with wave) coordinate system
F2=interp1d(y1, x1, kind='quadratic')

#finds the trajectory function in the OXY(with wave) coordinate system

x10=F2(0)

#finds the enpoint in the OXY(with wave) coordinte system

x0=(k*x10*math.sqrt(1+k**2)-b*(k**2+1))/(k*(1+k**2))
y0=F1(x0)

#converts the endpoint coordinates to the OXYZ system (z = 0)

print("x = " , x0)
print("y = " , y0)
print("z = " , 0)



