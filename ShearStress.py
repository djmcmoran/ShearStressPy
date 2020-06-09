# Generate script for Shear Stress
import math as m  ## Import math module
M = float(raw_input('Enter M (mass of object - weight per unit volume) in numeric value(grams) '))  ## Issue prompt statement for mass
alpha = float(raw_input('Enter angle(alpha) in numeric value to two decimal places '))  ## Issue prompt for angle

# define variables where possible
tau = 6.283185  ## Tau(T), also expressed as 2pi
g = 9.8  ## Gravity constant, units expressed as ms^-2
# sin alpha (sin of angle of the slope) is a value derived upon inspection or known for insertion into the equation

## Run equation with values from prompts
shear_stress = (M * g * (m.sin(alpha))/ tau)
print(float(M), 'mass', (g), 'gravity', (m.sin(alpha)), 'angle', (tau), 'tau')
print(int(shear_stress), 'Pa')
