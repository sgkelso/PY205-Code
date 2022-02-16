import math
#declare initial variables and constants
fgrav = 686 #N
angle = 36 #degrees
theta = (angle*math.pi)/180 #convert degrees to radians

#calculate vector decomp
fty = fgrav*math.sin(theta)
fnet = fgrav/(math.cos(theta))
ftx = fnet*math.sin(theta)
print("Tension in x direction is ", ftx, 'N')
print('Tension in y direction is ', fty, 'N')
print('Net force in rope 2 is ', fnet, 'N')

