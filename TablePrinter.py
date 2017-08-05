#! TablePrinter.py
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 23:47:34 2017

Write a function named printTable() that takes a list of lists of strings and
displays it in a well-organized table with each column right-justified. Assume
that all the inner lists will contain the same number of strings. For example,
the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

https://automatetheboringstuff.com/chapter6/

@author: david.antonini
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    # set column widths
    colWidths = [0]*len(table)
    for col in range(len(table)):
        colWidths[col] = len(max(table[col], key=len))
        # len for length instead of last in alpha ordering

# print table
    for rownum in range(len(max(tableData, key=len))):
        row = ''
        for col in range(len(table)):
            row += table[col][rownum].rjust(colWidths[col])+' '
        print(row)


printTable(tableData)
