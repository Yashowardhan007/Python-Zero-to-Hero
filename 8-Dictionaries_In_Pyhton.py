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