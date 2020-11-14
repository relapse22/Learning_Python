my_file = open('test.txt')

# (seek) Will go to the line in the Text File
my_file.seek(0)
print(my_file.read())
my_file.seek(0)

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)

print() # empty print just to give a line space in the code
print(my_file.readlines())

# close the file so it can be used somewere else it he programme
my_file.close()