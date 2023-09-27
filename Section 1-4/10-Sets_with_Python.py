""" 
Sets are unordered collections of unique elements.

Meaning there can only be one representative of the same object.

Let's see some examples!
"""

myset  = set()
print(myset)
myset.add(1) #{1}
print(myset)
myset.add(2)
myset.add(3)
print(myset) #{1, 2, 3}
myset.add(3)
print(myset) #{1, 2, 3}, notice 3 is not added again

mylist = [1,1,2,2,3,3,4,4,5,5,6]
print(set(mylist)) #{1, 2, 3, 4, 5, 6}

