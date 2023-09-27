#Create a File with .txt extension
myfile = open('12-myfile.txt')
#myfile = open('Yash.txt') //#FileNotFoundError: [Errno 2] No such file or directory: 'Yash.txt'

#read method
print(myfile.read())

#when we read again, it prints nothing,cause the cursor is at the end of the line in the file
print(myfile.read())
"""
output of the above 
Hello this is a Text file
this is a second line
this is a third line
"""
#We set the cursor to the start
myfile.seek(0)

print(myfile.read())
"""
output of the above 
Hello this is a Text file
this is a second line
this is a third line
"""

#to get the individual lines in form of list
myfile.seek(0) #reset the cursor to the start
mylist = myfile.readlines()
print(mylist) #['Hello this is a Text file\n', 'this is a second line\n', 'this is a third line']

#close this file
myfile.close()

with open('12-myfile.txt') as mynewfile:
    contents = mynewfile.read()
print('contents: \n',contents)
""" 
output of the above
contents:
Hello this is a Text file
this is a second line
this is a third line
"""
print('*****')
with open('12-myfile.txt',mode='r') as myfile:
    contents1 = myfile.read()
print(contents1)

print('*****')
with open('12-myfile1.txt',mode='r') as myfile1:
    print(myfile1.read())  
""" 
Output of the Above
First Line
Second Line
Third Line
"""

print('****')
with open('12-myfile1.txt',mode = 'a') as f:
    f.write('Fourth Line')

print('Writing to Fourth Line')
with open('12-myfile1.txt',mode='r') as myfile1:
    print(myfile1.read())  