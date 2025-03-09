# exceptions have 4 important words => try, except, else, finally

"""
try => something that might cause an exception

except => block of code we would like to execute when we have an exception

else => define some code to execute if there are no exceptions

finally => do this no matter what happens
"""

# file not found
try:
    file = open("a_file.txt")
    print("File found")
except:
    print("File not found")
    file = open("a_file.txt", "w")
    print("File created instead")
else:
    print("File found")
finally:
    print("Doing finally actions")
