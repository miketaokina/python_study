'''
Task 6: Sorting Three Numbers

Let a program ask the user for three integers and sort them in descending order. In this exercise you are not allowed to use lists or similar to solve the task, just variables and selection. This is the same as exercise 3.8 in the book.

Enter number 1: 5
Enter number 2: 9
Enter number 3: 3
The integers in descending order are: 9, 5, 3
'''

# Code Start:

number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))
number3 = int(input('Enter number 3: '))

if number1 > number2 and number2 > number3:
    print(f'The integers in descending order are: {number1}, {number2}, {number3}')
elif number1 > number3 and number3 > number2:
    print(f'The integers in descending order are: {number1}, {number3}, {number2}')
elif number2 > number3 and number3 > number1:
    print(f'The integers in descending order are: {number2}, {number3}, {number1}')
elif number2 > number3 and number1 > number3:
    print(f'The integers in descending order are: {number2}, {number1}, {number3}')
elif number3 > number2 and number2 > number1:
    print(f'The integers in descending order are: {number3}, {number2}, {number1}')
elif number3 > number2 and number1 > number2:
    print(f'The integers in descending order are: {number3}, {number1}, {number2}')
else: 
    print(f'You have entered equal numbers, please enter different numbers.')
