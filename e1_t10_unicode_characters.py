'''
Task 10: Unicode Characters

The Unicode character set has several different categories, for example, runes, arrows and geometrical symbols and in this exercise we want you to print five random characters from the runes category. Runes are located between 0x16A0 and 0x16FF. See an example of what the output can be below:

Random characters from the Runes category:
ᛊ ᚷ ᛢ ᛀ ᛠ
'''

# Code Starts:

import random

for i in range(5):
    code_point = random.randint(0x16A0, 0x16FF)

    rune_char = chr(code_point)
    
    print(rune_char, end=" ")

print()