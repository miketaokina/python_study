'''
Task 4: Wind-Chill Temperature

Exercise 2.9 in the book by Liang is about calculating the _perceived temperature_, that is calculating in the wind and what it does to the temperature when you are out in the cold. In the exercise, Liang uses the Fahrenheit degrees as he is American, but here in Sweden we usually use Celsius, so use the following formula to calculate the wind-chill, where T is the temperature in Celsius and V is wind speed in kilometres per hour:

$$ T_{wc} = 13.12 + 0.6215T - 11.37V^{0.16} + 0.3965T V^{0.16} $$

In reality, the wind-chill is only calculated for degrees below 10 degrees Celsius and above 4.8 km/s but in this exercise, you do not need to check the values entered. See below for an example execution:

Enter the air temperature in Celsius:  -8
Enter the wind speed in kilometres per hour:  12

The wind-chill temperature is: -13.49°C
'''

# Code Start

