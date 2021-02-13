import pandas as pd
from scipy.interpolate import interp1d
import math

import numpy as np


S=pd.read_csv(r"C:\Users\Alexander Asriyan\Desktop\MCE\MakeaFriend\balldata\ball_data1.csv")


xyz=S.to_numpy()


x = []
y = []
z = []

j=len(xyz)

arr1 = []


for i in range(0,j-1):  
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

for i in range(0,j-1):
    x1.append(math.sqrt(y[i]**2+(x[i]+b/k)**2))
    y1.append(z[i])
    
#print(x1)
#creates the 2D coordinate arrray in OXY(with wave) coordinate system

F2=interp1d(y1, x1, kind='quadratic')
F2ar=interp1d(x1, y1, kind='quadratic')

#finds the trajectory function in the OXY(with wave) coordinate system

def wave_to_XYZ(x):
    return (k*x*math.sqrt(1+k**2)-b*(k**2+1))/(k*(1+k**2))

#conversion function for x from wave system to OXYZ
    

x1ar = np.linspace(x1[0], x1[j-2], num=j-1)
x2ar = np.linspace(x1[0], x1[j-2], num=15)



x1list=x1ar.tolist()

x2list=x2ar.tolist()

#creates an evenly spaced x1 and x2 arrays(lists) in the OXY wave system
#x2 is needed for finding the quadratic function in the obvious form

d=-(x1ar[j//2]-x1ar[j//2 + 1])

#finds the differenth between two neighboring numbers of x1ar array

x1list.append(x1list[j-2]+d)

#adds the "n+1" member, whose ordinate is going to be "predicted"

x11=x2list[4]
y11=F2ar(x11)
x2=x2list[8]
y2=F2ar(x2)
x3=x2list[12]
y3=F2ar(x3)

A=(y2*(x11-x3)+y11*(x3-x2)+y3*(x2-x11))/((x2-x11)*(x3**2+x11*x2-x3*(x2+x11)))
B=(y2-y11)/(x2-x11)-A*(x2+x11)
C=y11-A*x11**2-B*x11

#finds the quadratic function in the obvious form

y01=A*x1list[j-1]**2+B*x1list[j-1]+C
x01=x1list[j-1]

#calcuates the ordinate for the "n+1" member, i.e. finds the next ball position's (x,y) in the OXY(with wave coordinate system)

x0=wave_to_XYZ(x01)

y0=-(k*x0+b)

z0=y01

#converts the "n+1" coordinates to the OXYZ system

print("x = " , x0)
print("y = " , y0)
print("z = " , z0)

#prints the "n+1" point's coordinates in the OXYZ system




