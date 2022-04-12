######################################################################################################################################################
#
# File: 009-deref_tuple.py
#
# Author: Mike Eldredge
#
# Origination Date: 12 Apr 2022
#
# Description: Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#   exam_st_date = (11, 12, 2014)
#
# Sample Input
#
# Sample Output
#
#   The examination will start from: 11/12/2014
#
######################################################################################################################################################

exam_st_date = (11, 12, 2014)

outStrings = ("The examination will start from: ", "/", "/")

for i in range(len(exam_st_date)):
    print(outStrings[i], exam_st_date[i], sep="", end="")
