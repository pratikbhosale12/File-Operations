#Write a python program to read a file and write the contents to another file and
# push the file onto github

output = open("file-2_output.txt",'w')

with open("file-1_input.txt",'r') as input:
    output.write(input.read())

print("Successfully Copied Contents")
output.close()
