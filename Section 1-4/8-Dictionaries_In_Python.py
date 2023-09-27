""" 
Complete Python 3 Bootcamp

•Dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence,
dictionaries use a key-value pairing instead.
This key-value pair allows users to quickly grab objects without needing to know an index location.



• Dictionaries use curly braces and colons to signify the keys and their associated values

{'keyl':'value1','key2':'value2'}

• So when to choose a list and when to choose a dictionary?

• Dictionaries: Objects retrieved by key name.

Unordered and can not be sorted.

• Lists: Objects retrieved by location.
 
Ordered Sequence can be indexed or sliced.

"""
mydict = {'k1':'v1','k2':'v2','k3':'v3'}
print(mydict) #{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

#To Extract the Value, we pass the key
print(mydict['k1']) #v1

d3 = {'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
print(d3['k2']) #[0, 1, 2]
print(d3['k3']) #{'insidekey': 100}
print(d3['k3']['insidekey']) #100

d4 = {'key1':['a','b','c']}
mylist = d4['key1']
print('mylist: ',mylist) #mylist:  ['a', 'b', 'c']
letter = mylist[2]
print('letter: ',letter.upper()) #letter:  C

#Alternative to Above thing is
print('To Grab a Index of Value:',d4['key1'][2])

d5 = {'k1':100,'k2':200,'k3':300}
print(d5)
d5['k4'] = 400
print(d5)

#To Exctract the Key From Dictionaries  use dictionary_name.keys()
print(d5.keys()) #dict_keys(['k1', 'k2', 'k3', 'k4'])

#To Exctract the value From Dictionaries use dictionary_name.values()
print(d5.values()) #dict_values([100, 200, 300, 400])

#To Extract the Both Keys and Values at the Same Time use dictionary_name.items()
print(d5.items()) #dict_items([('k1', 100), ('k2', 200), ('k3', 300), ('k4', 400)])



