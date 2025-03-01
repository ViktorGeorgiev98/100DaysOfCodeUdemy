# read file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write file, but will replace everything
# mode = w means writable
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# write file but add to already existing content
# mode = a means write, but add not overwrite
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# with mode = w, if file does not exist, we will create a file
# with open("my_file2.txt", mode="w") as file:
#     file.write("New text.")


#  read and write file from a specific directory
# with open("./test/test1/test2/test.txt", mode="w") as file:
#     file.write("Hello")
#
# with open("./test/test1/test2/test.txt") as file:
#     content = file.read()
#     print(content)