######################################################################################################################################################
#
# File: 006-cslist.py
#
# Author: Mike Eldredge
#
# Origination Date: 5 Apr 2022
#
# Description: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those
#   numbers.
#
# Sample Output
#
#   Sample data : 3, 5, 7, 23
#
#   List : ['3', ' 5', ' 7', ' 23']
#   Tuple : ('3', ' 5', ' 7', ' 23')
#
######################################################################################################################################################

dataString = "3, 5, 7, 23"
print("Sample data: ", dataString)

stringList = dataString.split(", ")

print("List : ", stringList)
print("Tuple : ", tuple(stringList))
