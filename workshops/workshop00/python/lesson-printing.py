#!/usr/bin/env python
'''
  File Name: lesson-printing.py
  Author: Lawrence (Drew) Whisenant
  Date Created: 01 July 2018
  Date Last Modified: 01 July 2018
  Python Version: 3.7
'''

# Topics:
# 0. Running Python
# 1. Comments
# 2. Printing and Strings

# 0. Running Python
# You can launch the Python interpreter from the command line by typing
#   python3
# You can run a Python file (ending in .py) from the command line (in the correct directory) by typing
#   python3 file.py

# 1. Comments
# In programming, a comment is anything in a code file that is not meant to be executed.
# They allow you to make notes about code or to write code without running it.
# In Python, you can comment out a line by starting the line with a pound symbol (#)

# For lesson files, delete the # symbol to run a line, and add it back next time you run the file.

# 2. Printing
# When learning to program, one of the first things you need to know
#   is how to print information to the screen.
# This is one way you have to get information about what your program 
#   as it runs.

# In Python, this done with a function called "print".
# A function is some code that you can run by knowing what it's called
#   without knowing (possibly) what it does or how it does it.

# Print takes some information and writes it to the screen.

# This line prints a number on a new line on the screen
# In this line, 538 is an argument to the function
# print(538)

# You can call print with no arguments.
# This line prints a blank, new line on the screen
# print()

# This line prints a number with a decimal in it on the screen.
# print(3.14159)

# You can also print a series of things.
# By default, Python will print all items with a space in between.
# print(1, 2, 3)

# You can change what's in the middle by specifying the sep argument.
# This line uses decimals instead of spaces.
# print(1, 2, 3, sep='.')

# This line uses colons instead of spaces.
# print(1, 2, 3, sep=':')

# In programming, we generally refer to text data as a string.
# The sep argument to print is a string.
# A string is usually written as 'string' or "string".

# This line prints my name.
# print('Drew')

# This line also prints my name.
# print("Drew")

# This line prints a string with quotes.
# print('A quote looks like this:"')

# This line prints an apostrophe.
# print("An apostrophe looks like this:'")

# We generally call ' a single quote and " a double quote.

# This line separates with the word "and".
# Notice the space on either side of the word "and".
# print(1, 2, 3, sep=' and ')

# You can also use whitespace letters using special characters.
#   A space is a space: ' '
#   Nothing is the empty string: ''
#   A tab is the special character: '\t'
#   A new line is the special character: '\n'
# The backslash is a signal to say "I don't really want the next letter, I want a special character."

# This line prints each item with new lines between them.
# print(1, 2, 3, sep='\n')

# Finally, you can print without printing a new line by default.
# This can be set using the end argument.

# These lines print the numbers 1 and 2 right beside one another.
# Notice that only the second line creates a new line.
# print(1, end='')
# print(2)

# These lines print the numbers 1 and 2 with a space between.
# Notice that only the second line creates a new line.
# print(1, end=' ')
# print(2)

# You can use sep and end together.
# Write down what you think the lines will print before running them.
# print("The", "Arab High School", "Robotics Team", "The Dragon Slayers", sep='\t', end='\n')
# print("Are the best!")
