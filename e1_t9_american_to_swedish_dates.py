'''
Task 9: American to Swedish Dates

In the USA dates are usually written on the form MM/DD/YY (where MM is a two-digit representation of the month while DD is for the day 
and YY for the year). The usual way to display a date in Swedish is in the format YY/MM/DD. Write a program that takes an American date 
as input and displays the equivalent Swedish date. You do not need to handle any errors in the input other than that the length has to 
be eight. See an example execution below:

Enter a date in American format:  08/21/75
Swedish date is: 75/08/21
'''

# Code Starts:

american_date = input('Enter a date in American format: ')

if len(american_date) != 8:
    print('Error: Input length must be 8.')
else:
    #  MM / DD / YY
    #  01 2 34 5 67

    mm = american_date[0:2]
    dd = american_date[3:5]
    yy = american_date[6:8]

    swedish_date = yy + '/' + mm + '/' + dd
    print(f'Swedish date is: {swedish_date}')