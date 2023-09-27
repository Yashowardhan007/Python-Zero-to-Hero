""" 
Two Methods For Formatting Strings
.format() method
f-strings(formatted string literals)

"""
#Example of Format

print('This is a String {}'.format('INSERTED')) #This is a String INSERTED

#Exmaple 2 of Format
 
print('Hello {1} {2} {0}'.format('Dole','Yashowardhan','Anand')) #Hello Yashowardhan Anand Dole

#Exmaple 3 of Format

print('Hello {d} {y} {a}'.format(d='Dole',y='Yashowardhan',a='Anand')) #Hello Dole Yashowardhan Anand

#Example of Float Formatting
""" 
Float formatting follows "{value:width.precision f}
width is the number of white spaces
"""

result = 100/777
print(result) #0.1287001287001287

print("The result is {r:1.3f}".format(r=result)) #The result is 0.129

#Example of F-String or Formatting String Literal


name = "Jose"
print(f'Hello, his name is {name}')
