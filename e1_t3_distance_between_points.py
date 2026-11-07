'''
Task 3: Distance Between Points

Write a program that asks the user for coordinates for two points in a two-dimensional coordinate system (x1, y1) and (x2, y2). The program 
should then calculate and print the distance between the two points. The distance between two points in a two-dimensional coordinate system 
can be calculated using the following:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$
'''

# https://github.com/miketaokina/python_study/blob/main/e1_t3_distance_between_points.md

'''
See below for an example execution of the program:

Enter the x-coordinate of the first point (x1):  3
Enter the y-coordinate of the first point (y1):  5
Enter the x-coordinate of the second point (x2):  7
Enter the y-coordinate of the second point (y2):  9

The distance between the points (3.0, 5.0) and (7.0, 9.0) is 5.66
'''

# Code Start

x1 = float(input('Enter the x-coordinate of the first point (x1): '))
y1 = float(input('Enter the y-coordinate of the first point (y1): '))
x2 = float(input('Enter the x-coordinate of the second point (x2): '))
y2 = float(input('Enter the y-coordinate of the second point (y2): '))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print()
print('The distance between the points (', x1, ', ', y1, ') and (', x2, ', ', y2, ') is ', round(distance, 2))
print(f'The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}')
