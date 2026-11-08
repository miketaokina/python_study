'''Task 5: Getting Random

Write a program that generates a random integer between -100 and 100. The number should be displayed and it should be identified as positive or negative as well as even or odd. If it is zero, just print that it is zero. See below for an example execution:

The number is 7
The number is odd and positive
'''

# Code Start:

import random

the_number = random.randint(-100, 100)
print(f'The number is {the_number}')

if the_number > 0 and the_number % 2 == 0:
    print(f'The number is even and positive')
elif the_number > 0 and the_number % 2 != 0:
    print(f'The number is odd and positive')
elif the_number < 0 and the_number % 2 == 0:
    print(f'The number is even and negative')
elif the_number < 0 and the_number % 2 != 0:
    print(f'The number is odd and negative')
else: 
    print(f'The number is zero')

