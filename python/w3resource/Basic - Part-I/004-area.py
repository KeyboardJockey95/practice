######################################################################################################################################################
#
# File: exercise-000-area.py
#
# Author: Mike Eldredge
#
# Origination Date: 5 Apr 2022
#
# Description: Write a Python program which accepts the radius of a circle from the user and compute the area.
#
# Sample Output
#
#   r = 1.1
#   Area = 3.8013271108436504
#
######################################################################################################################################################

import math

# prompt for and read in the radius
radius = float(input("r = "))

# apply πr² (pi r squared)
print("Area =", math.pi * radius**2)
