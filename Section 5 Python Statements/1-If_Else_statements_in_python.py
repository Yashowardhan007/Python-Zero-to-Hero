""" 
Let's begin to learn about control flow
We often only want certain code to execut when a particular condition has been met.
For example, if my dog is hungry (some condition), then I will feed the dog (some action).

Control Flow syntax makes use of colons and indentation (whitespace).
This indentation system is crucial to Python and is what sets it apart from other programming languages.


"""
#IF
if (3>2):
    print('Its True') #Its True

#IF ELSE
hungry = True
if hungry:
    print('Feed Me') #Feed Me
else:
    print('Dont Feed Me')


#IF ELIF and ELSE
loc = "Bank"

if(loc == 'Autoshop'):
    print("I am at the Auto Shop")
elif (loc == 'Bank'):
    print('Iam at the Bank')
else:
    print('Iam at Home')#Iam at Home