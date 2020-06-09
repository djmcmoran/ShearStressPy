# Generate script for Shear Stress
import math as m  ## Import math module
M = float(input('Enter M (mass of object - weight per unit volume) in numeric value(grams) '))  ## Issue prompt statement for mass

# define variables where possible
tau = 6.283185  ## Tau(T), also expressed as 2pi
g = 9.8  ## Gravity constant, units expressed as ms^-2
## range function used to generate alpha(angle) for given range (to 45 degrees, based on mechanics of devince in lab)
alpha = list(range(1,46,1))
y = len(alpha)
ShearStress = [0]*y

## Attempt at for loop for equation
i = 0
for x in alpha:
    ShearStress[i] = abs((M * g *(m.sin(x))/ tau))
    i = i + 1

## Print outputs
print(ShearStress, 'Pa')
