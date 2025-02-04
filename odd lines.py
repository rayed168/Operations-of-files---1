file1 = open("file.txt", "r")
file2 = open("fileupdated.txt", "w")
count = 0 
for line in file1.readlines():
    count += 1 
    if count%2 != 0:
        print(line)
        file2.write(line)
file2.close()
file1.close()

file_read = open("fileupdated.txt", "r")
print('Reading file')
print(file_read.read)
file_read.close() 