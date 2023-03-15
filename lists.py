# define a list of names
from os import name
from tkinter.font import names


names = ["rajkumar","rohan","Satish","Nitish"]
print(names [0])

names.append("Manoj")

names.sort()
print(names)



# Python program to demonstrate   
# Creation of List   
     
# Creating a List  
List = []  
print(List)  
     
# Creating a list of strings
List = ['GeeksForGeeks', 'Geeks'] 
print(List)  
     
# Creating a Multi-Dimensional List  
List = [['Geeks', 'For'], ['Geeks']]  
print(List)

# Adding Elements to a list: Using append(),insert() and extend()

# python program to demonstrate
# Addition of elements in a list

# creating a list 
list = []

# using append()
list.append(1)
list.append(2)
print(list)

#using insert()
list.insert(3,12,15)
list.insert(0,'Rajkumar')
print(list)

#using extend()
list.extend([ 8, 'raja ji','always'])
print(list)




## Accessing Elements from the list:--
#Use the index operator [ ] to access an item in a list.
#  In Python, negative sequence indexes represent positions 
# from the end of the array. Instead of having to compute the 
# offset as in List[len(List)-3],

#  it is enough to just write List[-3]

# Python program to demonstrate   
# accessing of element from list  
     
 
List = [1, 2, 3, 4, 5, 6]  
     
# accessing a element

print(List[0])   
print(List[2])  
   
# Negative indexing
# print the last element of list  
print(List[-1])
# print the third last element of list   
print(List[-3])



