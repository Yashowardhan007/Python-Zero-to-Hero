""" 
Complete Python 3 Bootcamp

• Lists are ordered sequences that can hold a variety of object types.

  They use [] brackets and commas to separate objects in the list.

。 [1,2,3,4,5]

• Lists support indexing and slicing. Lists can be nested and also 
have a variety of useful methods that can be called off of them.


"""
my_list = ['One','Two','Three']
print(my_list[1]) #Two
print(my_list[1:]) #['Two', 'Three']

my_list1 = ['Four','Five']
print(my_list+my_list1) #['One', 'Two', 'Three', 'Four', 'Five']

#Changing elements directly

my_list[0] = "1"
print(my_list[0]) #1

#Append  Method: Adding Method to the end of the List
newlist = my_list + my_list1;
print(newlist) #['1', 'Two', 'Three', 'Four', 'Five']
newlist.append('Six')
print(newlist) #['1', 'Two', 'Three', 'Four', 'Five', 'Six']

#pop removes the last element

pop_item = newlist.pop()
print(pop_item) #Six
print(newlist) #['1', 'Two', 'Three', 'Four', 'Five']

#pop element with index position to remove specific element
pop_item = newlist.pop(0);
print(pop_item) #1
print(newlist) #['Two', 'Three', 'Four', 'Five']


 

