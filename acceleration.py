import numpy as np
#Declare initial variables and constants
v0 = np.array([7,-5,0])
v1 = np.array([7.2, -5.4, 0])
timestep = 0.06 #time between v0 and v1
mass = 0.110 #kg
g = np.array([0, 9.8, 0]) #Gravitational field strength at earth surface
deltav = (v1-v0)
a = deltav/timestep
print('The acceleration of the mass is ', a, 'm/s/s')

#Rate of change of momentum calculation
dp = a*mass
print('The rate of change of momentum is ', dp, 'kg m/s/s')

#Net force calculation
Fnet = dp
print('The net force on the mass is ', Fnet, "N")