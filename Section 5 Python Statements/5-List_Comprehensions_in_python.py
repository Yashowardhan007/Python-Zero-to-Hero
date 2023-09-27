""" 
List Comprehensions are a unique way of quickly creating a list with Python.
If you find yourself using a for loop along with .append() to create a list,
List Comprehensions are a good alternative!
To do this, let's go to a Jupyter Notebook!
"""
#Traditional Method to convert String to a List

mystring = "Hello"
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist) #['H', 'e', 'l', 'l', 'o']

#More Convinient Method

mylist1 = [letter for letter in mystring]
print(mylist1) #['H', 'e', 'l', 'l', 'o']

mylist2 = [x for x in 'YashowardhanDole']
print(mylist2) #['Y', 'a', 's', 'h', 'o', 'w', 'a', 'r', 'd', 'h', 'a', 'n', 'D', 'o', 'l', 'e']

mylist3 = [num for num in range(0,10)]
print(mylist3) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Lets we want to Square up each number
mylist4 = [num*num for num in range(0,10)]
print(mylist4) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#If we want to add if statement in the list comprehension

mylist5 = [x for x in range(0,6) if(x%2==0)]
print(mylist5) #[0, 2, 4]

#To convert Celisius to Farenheit

celcius = [0,10,20,30,40]
print('Celcius: ')
print(celcius)
farenheit = [(9/5)*temp+32 for temp in celcius]
print('Farenheit:')
print(farenheit) 
""" 
Celcius: 
[0, 10, 20, 30, 40]
Farenheit:
[32.0, 50.0, 68.0, 86.0, 104.0]
"""

#List Comprehensions using IF and Else
#Even Odd Example

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)  #[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

#Nested For Loops

mylist6 = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist6.append(x*y)
print(mylist6) #[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

#Shorter Code For above

mylist6 = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist6) #[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]