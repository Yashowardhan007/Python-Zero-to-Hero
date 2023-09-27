""" 
Tuples in Python
Tuples are very similar to lists.However they have one key difference-immutability.

Once an element is inside a tuple, it can not be reassigned.

Tuples use parenthesis: (1,2,3)


"""

#tuple
t = (1,2,3)
print('type of t: ',type(t)) #type of t:  <class 'tuple'>
mylist = [1,2,3]
print('type of mylist: ',type(mylist)) #type of mylist:  <class 'list'>

t1 = ('One',2)
print(t1[0]) #One
print(t1[1]) #2
print('********')

#count method: counts the number of occurences of the passed argument
t2 = ('a','a','b','c','d','e','e')
print(t2.count('a')) #2
print(t2.count('b')) #1
print(t2.count('c')) #1
print(t2.count('d')) #1
print(t2.count('e')) #2

#index method: returns the index of the specified element
print('Index of b:',t2.index('b')) #Index of b: 2
 
print('Index of a:',t2.index('a')) #Index of a: 0, returns the first occurence of a


