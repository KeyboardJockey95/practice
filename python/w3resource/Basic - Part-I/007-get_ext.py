######################################################################################################################################################
#
# File: 000-get_ext.py
#
# Author: Mike Eldredge
#
# Origination Date: 7 Apr 2022
#
# Description: Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
#
# Sample Input
#   abc.java
#
# Sample Output
#   java
#
######################################################################################################################################################

print("filename: ", end="")
extension = input().split(".")[-1]
print("extension: ", extension)