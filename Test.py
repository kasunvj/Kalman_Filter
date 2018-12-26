import numpy as np
import csv
import math

#position gyro sensor
#Tis lines will genarate a CSV file containing sensor data
Z = []
mu ,sigma = 0, 1;

def noice_less_gyro(t_plus):
    return 4*t_plus

file = open ("Position_Gyro_Readings.csv","w")
for i in range (0,100):
    z = noice_less_gyro(i) + np.random.normal(mu, sigma,size = None)
    Z.append(z)
    file.write(str(z))
    file.write("\n")

file.close()

#State of the KF will be [Position; Velocity] position =pos(k) velocity=vel(k)
#[pos(k+1)   =  | 1   T | [pos(k)   +  |T^2/2| acc(k)
# vel(k+1)]     | 0   1 |  vel(k)]     |T    |
T = 1
A = np.array([(1,T),(0, 1)])
B = np.array([(np.square(T)/2),(T)])
Xk = np.array([(0),(0)])
ACC = 0

#X(K+1)
def Xkplus1(x, acc):
    return np.dot(A,x)+np.dot(B,acc)


L = []
a= np.array([(2),(3)])
b= np.array([(24),(33)])
L.append(a)
L.append(a)
L.append(b)
L.append(b)

M = []
a= np.array([(0,0),(0,0)])
b= np.array([(1,2),(3,5)])
M.append(a)
M.append(b)
M.append(a)
M.append(b)

#testing outputs
Chal = L
print(Chal)
print(Chal[2])
print(np.shape(Chal))
print(np.shape(Chal[2]))

Chal = M
print(Chal)
print(Chal[1])
print(np.shape(Chal))
print(np.shape(Chal[2]))

print(np.sqrt(b))



