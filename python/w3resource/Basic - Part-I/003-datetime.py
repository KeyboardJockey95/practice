######################################################################################################################################################
#
# File: exercise-003-datetime.py
#
# Author: Mike Eldredge
#
# Origination Date: 5 May 2022
#
# Description: Write a Python program to display the current date and time.
#
# Sample Output
#
#   Current date and time :
#   2014-07-05 14:34:14
#
######################################################################################################################################################

import datetime

now = datetime.datetime.now();
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
