#! python3
# -*- coding: utf-8 -*-
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

"""
Created on Mon Jul 31 22:43:29 2017

Script gets the text from the clipboard, add a star and space to the beginning
of each line, and then paste this new text to the clipboard.
Task from Automate the Boring Stuff with Python (AtBSwP)
https://automatetheboringstuff.com/chapter6/

@author: david.antonini
"""

import pyperclip

text = pyperclip.paste()

# This is code from Automate. 
# Separate lines and add stars.
#lines = text.split('\n')
#for i in range(len(lines)):    # loop through all indexes in the "lines" list
#    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
#text = '\n'.join(lines)


# This was my first attempt, with str.replace().
# It would be RAM heavy, reading the whole text into RAM, whereas splitting the
# text into a list of lines allows processing line by line.
#text = "* "+text  # adds leading bullet * to first line
#text = text.replace('\n', '\n* ')  # Adds bullet point to start of each line

# My final method, using str.splitlines()
text = "* "+text  # adds leading bullet * to first line
lines = text.splitlines(True)   # Splits the text into a list of lines.
                                # (True) to leave the linebreaks in the list.
text = '* '.join(lines)

pyperclip.copy(text)

print(text)
