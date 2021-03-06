"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open('./src/foo.txt', 'r')
readF = f.read()

print(readF)

f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE 
w = open("./src/bar.txt", "w")

w.write("Write three lines of arbitrary content.\n")
w.write("Then close the file.\n")
w.write("Open and inspect it to make sure the file contains expected results.\n")

with open("./src/bar.txt") as r:
  read_data = r.read()
  print(read_data)
  
print(r.closed)