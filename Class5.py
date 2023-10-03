# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:15:36 2023

@author: wongcyn6
"""

temp = 22
temp = 24
temperature = 30
specific_temp = 28.8
text = 'burger'
number = 52
pi_value = 3.1415




fahrenheit_temp = float(input("Input a temperature in Fahrenheit: "))
converted_temp = round((fahrenheit_temp - 32) * (5/9), 2)
print(str(fahrenheit_temp) + " in Centigrade is " + str(converted_temp))


number = int(input("Enter a lucky number: "))
if number % 5 == 0:
    print('The number ' + str(number) + ' is divisible by 5!')
else:
    print('The number ' + str(number) + ' is NOT divisible by 5!')
    