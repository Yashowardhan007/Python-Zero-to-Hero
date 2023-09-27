#range function

#range with ending index position
for num in range(10):
    print(num, end = " ") #0 1 2 3 4 5 6 7 8 9 (does not include 10)

#range with startand  index position
print(" ")
for num in range(3,10):
    print(num,end = " ") #3 4 5 6 7 8 9 (start =3 and does not include end=10)

#range with start, end and step size
print(" ")
for num in range(0,10,2):
    print(num, end = " ") #0 2 4 6 8
print(" ")
mylist = list(range(0,10,2))
print(mylist, end = " ") #[0, 2, 4, 6, 8]
print(" ")
print(list(range(0,20,3)), end = " ") #[0, 3, 6, 9, 12, 15, 18]

#Enumerate

#Lets say we need to to keep the track of index of the string
print(" ")
indexcount = 0
for i in 'abcdefg':
    print('At Index {i} the letter is {l}'.format(i=indexcount,l=i))
    indexcount = indexcount+1
""" 
Output of the Above
At Index 0 the letter is a
At Index 1 the letter is b
At Index 2 the letter is c
At Index 3 the letter is d
At Index 4 the letter is e
At Index 5 the letter is f
At Index 6 the letter is g
"""
print(" ")
#Another Way to Approach  the Above Example
print("Another Way to Approach  the Above Example")
count = 0
for i in 'abcdegf':
    print(i,':',count)
    count = count+1

#Enumerate Function: Does index Count For Us Automatically
print("Enumerate function")
word = "abcd"

for item in enumerate(word):
    print(item)
""" 
Output:
Enumerate function
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
"""

#Zip function is used to bind to list
print('Zip Function')
mylist3 = [1,2,3,4]
mylist4 = ['a','b','c','d']
mylist5 = [100,200,300,400]
for item in zip(mylist3,mylist4,mylist5):
    print(item)
""" 
Output
Zip Function
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)
(4, 'd', 400)
"""

#in keyword can be used if object is in the list
a = 'x' in [1,2,3] #checks if x is in list [1,2,3]
print(a) #False
b = 'a' in ['a','b','c'] #check if a is in the list ['a','b','c']
print(b) #True


#in keyword to check if letter is in a string
c = 'a' in "Yashowardhan"
print(c) #True

#in keyword to check if key is present in dictionary

d = 'key1' in {'key1':100,'key2':200}
print(d) #True

#Min and Max
print('Min and Max')
ml = [10,20,30,3000,5000]
print('Min Number is: ',min(ml))
print('Max Number is: ',max(ml))
""" 
Output:
Min and Max
Min Number is:  10
Max Number is:  5000

"""
#random library
from random import shuffle
shuffle(ml)
print(ml) #[30, 10, 3000, 5000, 20]