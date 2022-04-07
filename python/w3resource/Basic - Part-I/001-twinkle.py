######################################################################################################################################################
#
# File: exercise-001-twinkle.py
#
# Author: Mike Eldredge
#
# Origination Date: 31 Mar 2022
#
# Description: Write a Python program to print the Twinkle, twinkle poem in a specific format (see the output).
#
# Sample String
#   "Twinkle, twinkle, little star, How i wonder what you are! Up above the world so high, Like a
#   diamond in the sky. Twinkle, twindle, little star, How I wonder what you are"
#
# Sample Output - where '|' represents the left edge of the screen:
#   
#  |Twinkle, twinkle, little star,
#  |    How I wonder what you are!
#  |        Up above the world so high,
#  |        Like a diamond in the sky.
#  |Twinkle, twinkle, little star,
#  |    How I wonder what you are!
#
######################################################################################################################################################

# Declare the string using line continuation char '\'
celestial_poem = \
"Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, \
Like a diamond in the sky. Twinkle, twindle, little star, How I wonder what you are"

tabspaces = "    "

# Cherry-pick the needed substrings and print them in the required format

# Show the offsets
#0         1         2         3         4         5         6         7         8         9        10        11        12        13        14        15        16
#0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
#Twinkle, twinkle, little star, How i wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twindle, little star, How I wonder what you are

# mark beginning
print("\nsimple straightforward algorithm")
print("=====================================\n")

# print the first line
print(celestial_poem[:30])

# print the second line after a tab. The 'print' statement can take a variable-length list of tab-separated parameters.  The sep='' supresses print's putting a default space
# between the printed parameters.
print(tabspaces, celestial_poem[31:57], sep='');

# and continue
print(tabspaces, tabspaces, celestial_poem[58:85])
print(tabspaces, tabspaces, celestial_poem[86:112])

# cheat and just do the first two lines over.
print(celestial_poem[:30])
print(tabspaces, celestial_poem[31:57], sep='');

# now try a different algorithm

# mark middle
print("\nparametric looping algorithm")
print("=====================================\n")

#define the number of tabs, beginning offset, and ending offset for each section of the poem
linespecs = [[0, 0, 30], [1, 31, 57], [2, 58, 85], [2, 86, 112], [0, 0, 30], [1, 31, 57]]

for linespec in linespecs:
    # print out the tabs
    for i in range(linespec[0]): print(tabspaces, sep='', end='')

    # print the subsection of the poem
    print(celestial_poem[linespec[1]:linespec[2]])
    
# mark end
print("\n=====================================")
