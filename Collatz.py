#! python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:28:00 2017

@author: david.antonini

Takes input from user and runs Collatz sequnce, printing each step
"""


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number*3 + 1


number = 0
while number == 0:
    try:
        number = int(input('Please enter a number: '))
        if number == 0:
            print('Number must be an integer not equal to zero.')
        else:
            while True:
                number = collatz(number)
                print(number)
                if abs(number) == 1 or number == -5 or number == -17:
                    break
    except ValueError:
        print('Number must be an integer.')
