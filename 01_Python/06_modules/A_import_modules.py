# Importing an implicit module

import math
num = int(input("Enter any number = "))
sq_root = math.sqrt(num)
print(sq_root)

# Importing a specific function from a module

from math import cbrt
cb_root = cbrt(num)
print(cb_root)

# Importing an explicit module

import B_calculator_functions
print(B_calculator_functions.add(10,5))
