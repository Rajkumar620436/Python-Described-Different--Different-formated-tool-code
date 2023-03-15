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




# Python program to demonstrate   
# Removal of elements in a List  
     
# Creating a List  
List = [1, 2, 3, 4, 5, 6,   
        7, 8, 9, 10, 11, 12]
 
# using Remove() method  
List.remove(10)  
List.remove(11)
print(List)  
   
# using pop()
List.pop()
print(List)  