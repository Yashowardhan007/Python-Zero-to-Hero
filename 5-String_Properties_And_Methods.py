""" 
 Immutability meanns we cannot change the String
 
"""
name = "Sam"
print(name) #Sam
lastletters = name[1:] #Stores am in lastletters
name = 'P' + lastletters 
print(name) #Pam

#Upper and Lower Methods in Python
letter = 'z'
print(letter*10)

x = "Hello World"
print(x)
x = x.upper()
print(x)
x= x.lower()
print(x)

#split method will split the String into list based on white space or letter passed in
x = x.split()
print(x) #['hello', 'world']

#Another Example of Split Function is
y = "Hii This is A String"
y =  y.split('i')
print(y) #['H', '', ' Th', 's ', 's A Str', 'ng']

