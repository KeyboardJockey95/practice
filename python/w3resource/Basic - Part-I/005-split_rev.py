######################################################################################################################################################
#
# File: 005-split_rev.py
#
# Author: Mike Eldredge
#
# Origination Date: 5 Apr 2022
#
# Description: Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#
# Sample Output
#   Enter your first and last name: Mike Eldredge
#
#   Eldredge, Mike
#
######################################################################################################################################################

names = input("Enter your first and last name: ")

first, last = str.split(names)

print()
print(last, ", ", first, sep="")
