#python is case sensitive
print("Hello, World!") 

#variables: no need to declare variables before using them
name  = "John" #tring type
age = 25 #integer type
price = 1234.76 #float type
isStudent = False #boolean type
print(name, age)

#check type of variable
print(type(name)) 
print(type(age))
print(type(isStudent))
print(type(price))

#Take input from user: use input() 
user = input("ENTER YOUR NAME:")
print("Hello, " +user) #concatenation of string

#exercise : Take name, age and height as input and display a paragraph using input values

naam = input("Enter name:")
your_age = input("Enter your age:")
height = input("Enter height in meters:")

print("Hello, my name is " + naam + ". aI am " + your_age + " years old. My height is " + height + " m.")