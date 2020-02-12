"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

numberOfArguments = len(sys.argv)

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " )

for i in sys.argv:
  print(i)

# Print out the OS platform you're using:
import platform

print("Platform System: " + platform.system())
print("Platform Release: " + platform.release())

# Print out the version of Python you're using:
print("Python Version: " + sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("The current process ID: " + str(os.getpid()))

# Print the current working directory (cwd):
print("The current working directory: " + str(os.getcwd()))

# Print out your machine's login name
print("The current working directory: " + str(os.getlogin()))
