file = open("file.txt", "r")
print(file.read())
file.close()

file = open("file.txt", "r")
print("Read in parts")
print(file.read(5))
file.close()

file = open("file.txt", "a")
file.write("\nThis is a new line")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()