file1 = open("input.txt",'r')
file2 = open("output.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()
cont  = 0
for i in range(len(file1_lines)):
    if file1_lines[i] != file2_lines[i]:
        cont = cont + 1
        print("Line " + str(i+1) + " doesn't match.")
        print("------------------------")
        print("File1: " + file1_lines[i])
        print("File2: " + file2_lines[i])

file1.close()
file2.close()
