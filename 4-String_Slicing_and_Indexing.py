""" 
Indexing and Slicing

"""
mystring = "Hello World"
print(mystring) #Hello World

#To Grab A Single Character From String
#Lets say we want to grab the 6th character in the string

print(mystring[6]) #W

#We can grab the string from reverse also
print(mystring[-1]) #d
print(mystring[-2]) #l
print(mystring[-3]) #r
print(mystring[-4]) #o

#Slicing

mystring1 = "abcdefghi"

#grabs everything after 2nd position
print(mystring1[2:]) #o/p:cdefghi.  

#grabs everything before 3rd postion
print(mystring1[:3]) #abc

#lets grab another subsection of the string lets say 'def'
print(mystring1[3:6]) #def

#lets understand step size
""" 
By Default step size is 1, which means string  is scanned 1 character
after the other.
if set step size = 2. lets say.. then we string will scan characters which are 2 letter
ahead from the current character
"""
#Example of Step

mystring3 = "abcdefghijk"
print(mystring3[::2]) #acegik

#to reverse a String 
print(mystring3[::-1]) #kjihgfedcba
