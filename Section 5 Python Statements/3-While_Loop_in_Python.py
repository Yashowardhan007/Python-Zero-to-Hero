
x = 0;
while (x<5):
    print(f'The Current Value of X is {x}')
    x = x+1
else:
    print('Final Value of X is: ',x)

""" 
Output of the Above
The Current Value of X is 0
The Current Value of X is 1
The Current Value of X is 2
The Current Value of X is 3
Final Value of X is:  5
"""

""" 
break, continue, pass
We can use break, continue, and pass statements in our loops to add additional functionality for various cases.
The three statements are defined by:
break: Breaks out of the current closest enclosing loop. 
continue: Goes to the top of the closest enclosing loop. 
pass: Does nothing at all.

"""
#pass
x = [1,2,3,4]
for i in x:
    pass

#continue
str = "Yash"
for x in str:
    if x == 'a':
        continue #continue skips the current iteration and goes to nexr one
    print(x) #Prints y,s,h


#break
print('break statement')
str1 = "Yashowardhan"
for x in str1:
    if x == 'h':
        break #Breaks the current closest enclosing loop
    print(x) #print y a s