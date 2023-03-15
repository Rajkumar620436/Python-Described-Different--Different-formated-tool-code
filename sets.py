# Create an empty set
s = set()

#add element to set 
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)
s.add(6)
s.add(7)
s.add(10)
s.add(64)
s.add(45)
s.add(3)
s.add(11)
print(s)

s. remove(10)
print(s)

print(f"the set has {len(s)} elements.")



# Python program to demonstrate   
# Creation of Set in Python  

# creating a set 
set1 = set()

#creating a set of string
set1 = set("GeeksForGeeks") 
print(set1)  
   
# Creating a Set of List  
set1 = set(["Geeks", "For", "Geeks"])
print(set1)  

## ADDING ELEMENTS:USING add()and update()

set1 = set()
     
# Adding to the Set using add() 
set1.add(8)
set1.add((6, 7))
print(set1)  
   
# Additio to the Set using Update()   
set1.update([10, 11])
print(set1) 



#Accessing a set:
# One can loop through the set items using a for 
# loop as set items cannot be accessed by referring to an index

# Creating a set  
set1 = set(["Geeks", "For", "Geeks"])  
 
# Accessing using for loop
for i in set1:  
    print(i, end =" ")


# REMOVING ELEMENTS FROM A SET:
# Using remove(),discard(),pop()and claer()

set1 = set([1, 2, 3,3 ,4, 5, 5, 6, 7,
             8, 9, 10, 11, 12, 13, 14])

# using Remove() method  
set1.remove(5)  
set1.remove(6)
print(set1)  
 
# using Discard() method  
set1.discard(8)  
set1.discard(9)
print(set1)  
 
# Set using the pop() method  
set1.pop()
print(set1)  
 
# Set using clear() method  
set1.clear()
print(set1)     


