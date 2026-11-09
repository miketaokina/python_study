'''
Task 8: Processing Strings

Let a program ask for a string and then print some information about it. The information needed to be displayed is the length of the string, 
the first and last letter, the number of spaces in it and if contains the string "Python". Solve the task without using iteration (that is 
in the next assignment). See an example execution below:

Enter a string:  The programming language Python is named after Monty Python
Length: 59
First and last letter: T, n
Number of spaces: 8
Does it contain "Python"? Yes

'''

# Code Starts:

user_string = input('Enter a string: ')

length = len(user_string)
first_letter = user_string[0]
last_letter = user_string[-1]
number_of_spaces = user_string.count(' ')
if 'Python' in user_string:
    contains_python = 'Yes'
else:
    contains_python = 'No'

print(f'Enter a string: {user_string} \nLength: {length} \nFirst and last letter: {first_letter, last_letter} \nNumber of spaces: {number_of_spaces} \nDoes it contain "Python"? {contains_python}')

'''
print('Length:', length)
print('First and last letter:', first_letter + '', '' + last_letter)
print('Number of spaces:', space_count)
print('Does it contain "Python"?:', contains_python)
'''