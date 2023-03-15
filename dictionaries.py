houses = {"rajkumar":"RAJ KUMAR SINGHANIYA","sapana":"synthaliya"}

houses["sapana"] = "manoj pandit"
print(houses["rajkumar"])


# Creating an empty Dictionary  
Dict = {}
print(Dict)  
 
# with Integer Keys  
Dict = {1: 'raju', 2: 'For', 3: 'this is websited of the road mapping'}
print(Dict)  
 
# with Mixed keys  
Dict = {'Name': 'group of collection', 1: [1, 2, 3, 4]}
print(Dict) 



# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For',  
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
   
print(Dict)  


#Adding element to Dictionary:
# one value at a time can be added to a Dictinary by defining 
# value along with the key e.g:- Dict[key] = 'value'.

# creating an empty Dictionary 
Dict = {}

# Adding elements one at a time 
Dict[0] = 'Singhaniya group of company'
Dict[2] = 'For'
Dict[3] = 1
print(Dict) 
 
   
# Updating existing Key's Value 
Dict[2] = 'Welcome to my world'
print(Dict) 


# Python program to demonstrate    
# accessing an element from a Dictionary   
     
# Creating a Dictionary   
Dict = {1: 'singhaniya', 'name': 'For', 3: 'Geeks'}  
     
# accessing a element using key
print(Dict['name'])  
   
# accessing a element using get()
print(Dict.get(3)) 

# Removing Elements from Dictionary: 
# Using pop(),and popitem():

# Initial Dictionary  
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',  
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
       }  
     
# using pop()  
Dict.pop(5) 
print(Dict)  
 
# using popitem()  
Dict.popitem() 
print(Dict)  

# dictionary with integer keys:

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
  
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

print("Empty Dictionary: ") 
Dict = {}
print(Dict)

Dict = dict({1: 'raja ji', 3: 'for', 4: 'singhaniya'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# creating a Dictionary with dict() method
Dict = dict([(1, 'rajkuar'), (2,'for')])
print("\nDictionary with each item as a pair: ")
print(Dict)

#Adding elements to a Dictionary

Dict = {}
print("Empty Dictionary as a elements: ")
print(Dict)
  
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

