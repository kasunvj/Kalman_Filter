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
def Get_X_at_K_plus_1(x, acc):
    return np.add(np.dot(A,x),np.dot(B,acc))
#Xk1= Get_X_at_K_plus_1(Xk,ACC)

#matrix_initialization
Xk1_est = np.array([(0),(0)])

#State Extapolation
Xk1_est_cal = np.dot(A,Xk1_est)



#testing outputs
Chal = Xk1_est_cal
print(Chal)
print(np.shape(Chal))
print(np.shape(Chal))




