import numpy as np
import csv
import math

#position gyro sensor
#Tis lines will genarate a CSV file containing sensor data
Z = []
T = 1
mean_process ,sigma_process = 0, 2;
mean_sensor,sigma_sensor = 0, 1;

def noice_less_gyro(t_plus):
    return 4*t_plus

file = open ("Position_Gyro_Readings.csv","w")
for i in range (0,100):
    z = noice_less_gyro(i) + np.random.normal(mean_sensor, sigma_sensor,size = None)
    Z.append(z)
    file.write(str(z))
    file.write("\n")

file.close()

#State of the KF will be [Position; Velocity] position =pos(k) velocity=vel(k)
#[pos(k+1)   =  | 1   T | [pos(k)   +  |T^2/2| acc(k)
# vel(k+1)]     | 0   1 |  vel(k)]     |T    |
#From State Space model of Process
A = np.array([[1,T],[0, 1]])
B = np.array([[np.square(T)/2],[T]])
#From State Space model of Sensor
H = np.array([[1,0]])

Xk = np.array([[0],[0]])
ACC = 1

#X(K+1)
def Xkplus1(x, acc):
    return np.dot(A,x)+np.dot(B,acc)

#Variance Calculation
#Process
Var_W = np.dot(np.square(sigma_process),np.square(B))
#Sensor
Var_V = np.dot(np.square(sigma_sensor),np.square(1))

#Covarians Calculation
def Covariance(var):
    return np.sqrt(np.dot(var,np.transpose(var)))

Q = Covariance(Var_W)
R = Covariance(Var_V)


#Variable Initialization
X_hat = np.array([[0],[0]])
P = np.array([[0],[0]])

#State Exploitation
X_hat_working = np.dot(A,X_hat)

#Covariance Calculation
Error = X_hat - Xkplus1(X_hat,0) #------------------------------- Check this is right
P = np.dot(Error,np.transpose(Error))
P_working = np.dot(A, np.dot(P,np.transpose(A))) + Q

#Kalman Gain
K_bar =np.dot(H,np.dot(P_working,np.transpose(H))) + R
K = np.dot(np.transpose(P_working), np.transpose(H))/K_bar



Chal =K
print(Chal)
#print(Chal[2])
print(np.shape(Chal))
#print(np.shape(Chal[2]))