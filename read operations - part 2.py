file_read = open("file.txt", "r")
print("Reading file")
print(file_read.read())
file_read.close()

file_write = open("file.txt", "w")
file_write.write("\nFile in write mode")
file_write.close()

file_read = open("file.txt", "r")
print("Reading file")
print(file_read.read())
file_read.close()

file_append = open("file.txt", "a")
file_append.write("\nFile in append mode")
file_append.close()

file_read = open("file.txt", "r")
print("Reading file")
print(file_read.read())
file_read.close()