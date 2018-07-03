#!/usr/bin/env python
'''
  File Name: lesson-variables.py
  Author: Lawrence (Drew) Whisenant
  Date Created: 03 July 2018
  Date Last Modified: 03 July 2018
  Python Version: 3.7
'''

# Topics
# 1. Variables
# 2. Types and Casting
# 3. Operations (Math and Logic)

# 1. Variables
# Now that you can print to the screen, you'll be able to see what 
#  the computer is doing with your program as it runs.

# For print, you supplied some data into the function immediately.
# But what if you want to put some data in your program to be used later?

# This is where variables come in.
# In math, a variable is an unknown or something whose value can change.
# In programming, a variable is a piece of memory that can hold information.

# Consider: x = 3
# In math, we say, "The variable x is equal to the value 3," or "x is 3."
# In programming, this sentence reads, "The variable x gets the value 3," or "3 is stored in x."

# When programming in Python, = does not mean "equals," it means assignment.
# For that reason, it is called the assignment operator.
# Whenever you see it, think of it as "I am putting the right value into the memory on the left."

# You can use variables with print.
# You can uncomment both lines or just one, but notice what happens if the first line stays commented.
# x = 3
# print(x)

# Generally, you want to name your variables something more meaningful than x.
# Variables should start with a lowercase letter and have no spaces.
# If you have multiple words in the variable, they should all start with a capital letter (except the first).
# This is called camelCase.
# myBetterNamedVariable = 42

# The process of making a variable is declaration and giving it a value is called initialization.

# 2. Types and Casting
# Many programming languages have a concept of types for variables.
# For example, in x = 3, three is an integer (no decimal value), so its type is int.
# In x = 3.14, 3.14 is a floating point number (decimal value), so its type is float.
# In x = 'c', 'c' is a single character, so its type is chr.
# In x = "me", "me" is a string value, so its type is str.
# In x = True, True is a boolean value, so its type is bool.

# A boolean indicates 0 or 1, off or on, false or true, etc.
# In Python, the two boolean values are True and False.
# x = True
# print(x)
# y = False
# print(y)

# Python is a dynamically typed language, which means, essentially, that programs
#  will rely on context to figure out the type of a variable.

# For example, consider these lines
# x = 1.0
# x = 1
# x = "1.0"
# You can run all three lines, and x can take all three values, even though all three have different types.

# You can also try to change one type to another.
# We call this process casting.

# Suppose you have an integer.
# x = 3
# print(x)

# But you want to make sure the computer reads it as a decimal.
# So you tell it to!
# y = float(x)
# print(y)

# You can do the same thing if you want to ignore the decimal part of a float.
# Notice that it chops off the decimal (no rounding).
# x = 3.77
# print(x)
# y = int(x)
# print(y)

# You can easily cast to string with str
# x = 3
# y = str(3)

# But be careful casting from string.

# For example, this is ok
# x = "3.15"
# y = float(x)
# print(y)

# But this causes an error
# x = "Not a number"
# y = float(x)

# Another oddity is with converting booleans.
# x = "True"
# y = int(x)
# This will fail.

# This won't, so be mindful when casting.
# x = "True"
# y = int(bool(x))

# 3. Operations (Math and Logic)
# Output (printing) is important to programming, because it allows you to "see" your program run.
# Data (variables) is important to programming, because is allows you to store information.
# The final piece is operations - using your data to do something (usually in the form of math).

# Let's start with the math operations.
# Addition
# Subtraction
# Multiplication
# Division
# Exponent
# Floor Division
# Modulus

# Now let's look at some logic.




