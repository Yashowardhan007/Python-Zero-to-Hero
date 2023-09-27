""" 
Many objects in Python are "iterable",meaning we can iterate over every element in the object.
Such as every element in a list or every character in a string.
We can use for loops to execute a block of code for every iteration.
"""

mylist = [1,2,3,4,5,6,7,8,9,10]

for number in mylist:
    print(number) #prints 1-10
print("")
for number in mylist:
    print('Hello') #prints hello 10 times

#check if number is odd or even from the list

for number in mylist:
    if (number%2 == 0):
        print('Number is Even')
    else:
        print('Number is Odd')

#Sum of All the  Numbers in the List

result = 0
for number in mylist:
    result = result + number
print('Sum Total of Numbers is: ', result)

#Iterating Through a String
for letter in 'Hello World':
    print(letter)

#Iterating Through a Tuple
print('Iterating Through a Tuple')
t = (11,22,33,44,55,66,77,88,99,100)
for item in t:
    print(item)

#Iterating through a List of Tuples

mylist1 = [(1,2),(3,4),(5,6),(7,8)]
print('Length of the List is: ',len(mylist1))

for item in mylist1:
    print(item)

""" 
Output of the Above
Length of the List is:  4
(1, 2)
(3, 4)
(5, 6)
(7, 8)
"""
#Tuple Unpacking

for(a,b) in mylist1:
    print(a)
    print(b)
""" 
1
2
3
4
5
6
7
8
"""

mylist2 = [(1,2,3,),(4,5,6),(10,20,30)]
for (x,y,z) in mylist2:
    print(x)
    print(y)
    print(z)
""" 
1
2
3
4
5
6
7
8
1
2
3
4
5
6
10
20
30
"""
#Iterating Through Dictionaries
print('Iterating Through Dictionaries')
d = {'k1':1,'k2':2,'k3':3}
#Default iteration gives us keys only
for item in d:
    print(item)

#To Iterate through value, use dictionary_name.values() function
print('Printing Values in the Dictionary')
for item in d.values():
    print(item)
""" 
Output of the Above
Printing Values in the Dictionary
1
2
3
"""
#To Print Key and Values use dictionary_name.items() function
print('Printing Keys and Values in the Dictionary')
for item in d.items():
    print(item)
""" 
Output of the Above
Printing Keys and Values in the Dictionary
('k1', 1)
('k2', 2)
('k3', 3)
"""

#Another Way to iterate is as Follows

for key,value in d.items():
    print('Keys: ',key)
    print('Values: ',value)
