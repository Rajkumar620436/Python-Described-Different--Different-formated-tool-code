# python program to demonstrate
# creation of set

# creating an empty tuple
from typing import Tuple


Tuple1 = ()
print (Tuple1)

#creating a tuple of strings
print(('Rajkumar','for a learning more again you again'))

# Creating a Tuple of list integer values 
print(tuple([1, 2, 4, 5, 6, 7, 8, 9, 10]))
 
# Creating a nested Tuple
Tuple1 = (0, 1, 2, 3,15,655, 5516, )  
Tuple2 = ('python', 'rajtutorials')  
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)


print( "ACCESSING Element of a tuple-")
# Python program to  
# demonstrate accessing tuple 
   
tuple1 = tuple([1, 2, 3, 4, 5]) 
   
# Accessing element using indexing
print(tuple1[0]) 
   
# Accessing element using Negative
# Indexing
print(tuple1[-1])




# Python program to  
# demonstrate accessing tuple 
   
tuple1 = tuple([1, 2, 3, 4, 5]) 
   
# Accessing element using indexing
print(tuple1[0]) 
   
# Accessing element using Negative
# Indexing
print(tuple1[-1])

# Deleting/ updating elements of tuple:
# Python program to  
# demonstrate updation / deletion 
# from a tuple 
   
tuple1 = tuple([1, 2, 3, 4, 5])
   
# Updating an element
tuple1[0] = -1
   
# Deleting an element
del tuple1[2] 