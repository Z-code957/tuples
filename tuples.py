"""tuple1 = (1,2,3,"a","book")
print(tuple1)
#length or size
print(len(tuple1))
#indexing
print(tuple1[4])
#slicing
print(tuple1[1:4])
#changing a list = mutable
#list = mutable
#tuple = immutable
list1 = [1,2,3,4]
list1[2]="9"
print(list1)
#tuple1[4]="pen"
print(tuple1)
tuple2 = (1,1,3,3,4,4,4)
print(tuple2.count(4))"""
"""Tuple Operations
Outline:
Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers
 3. Create a new tuple by adding 9 to the previous tuple 
 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple"""
tuple1 = (1,2,3,"name","H")
tuple2 = (2,6,4,8)
#tuple3 = tuple2+9
print(tuple1[2:4])
"""2.Flip Flop
Outline:
Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome,
 then it is the same after being reversed."""
t = (1,2,3,3,2)
if t==t[::-1]:
    print("The given tuple is a flip flop")
else:
    print("The given tuple is not a flip flop")
"""Weather Prediction
Outline:
Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0).
 If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1.
   On the basis of the value of rainy and sunny, predict the weather."""
weather = (1,0,0,0,1,1,0,1)
sunny = 0
rainy = 0
for i in range(0,7):
    if weather [i]==1:
        rainy+=1
    else:
        sunny+=1
if (sunny>rainy):
    print("IT IS SUNNY :) total sunny days are ",sunny)
elif (rainy>sunny):
    print("IT IS rainy :) total rainy days are" ,rainy)
else:
    print("The weather is balanced between sunny and rainy.")
