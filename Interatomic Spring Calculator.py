import math #import math

#declare initial variables
mass = 44.0 #Mass hung from wire in kg
dlength = (0.002639) #Wire stretch (delta length) in m
density = 8900.0 #kg/m^3 (usually given in problem statement (1g/cm^3 = 1000kg/m^3))
length = 3.0 #length of the metal wire in m
g = 9.8 #Gravitational field strength on Earth
#r = radius of wire if circular cross section
#code to calculate molar mass
mmol = 59 #mass in kg per mole of metal
navo = 6.02e23 #Avogadro's # in atoms/mole
matom = mmol/navo #kg/atom

#10.3E formatting is scientific notation to 3 decimal places
print('The mass of one atom is ', format(matom, "10.3E"), ' kg') 

#ONLY USE AND UNCOMMENT FOR SQUARE CROSS SECTION 
#Acs = (0.11/100)**2 #Square cross-section length in m when given side length in cm

#ONLY USE AND UNCOMMENT FOR CIRCULAR CROSS SECTION
#Acs = math.pi*(r**2)

#USE FOR RECTANGULAR CROSS SECTION
side1 = 0.0015 #side 1 length in m
side2 = 0.0027 #side 2 length in m
Acs = side1*side2 #Cross-sectional area in m^2

#calculate distance between atoms
Vatom = matom/density
datom = (Vatom) ** (1/3)
print('Distance between atoms is ', format(datom, "10.3E"), ' m')

#calculate amounts of series and parallel spring chains
series = length/datom
print('Number of serial springs is ',format(series, "10.3E"))

parallel = Acs/((datom)**2)
print('Number of parallel springs is ',format(parallel, "10.3E"))

#calculate interatomic spring force
Kwire = (mass*g)/dlength
Katom = (Kwire*series)/parallel
print('Interatomic spring force is ', format(Katom, "0.2f"), 'N/m')

#Calculations for speed of sound through the wire
vsound = math.sqrt(Katom/matom) * datom #use sqrt function imported from math
print('Speed of sound through the material is ',format(vsound, "10.3E"), 'm/s')

#Calculations for Young's Modulus
stress = (mass*g)/Acs
strain = dlength/length
ymod = stress/strain
print('Youngs Modulus for this wire is ', format(ymod, "10.3E"), ' N/m^2')