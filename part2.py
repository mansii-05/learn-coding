#EVERY THING WE TAKE INPUT FROM USER IS CONSIDERED AS STRING

#arithmetic_operations exercise
num1 = input("Enter first number:")
num2 = input("Enter second number:")

# sum
sum = int(num1) + int(num2)
print("sum: ",sum)

# difference
difference = int(num1) - int(num2)
print("difference: ",difference)

# product
product = int(num1) * int(num2)
print("product: ",product)

# quotient
quotient = int(num1) / int(num2)
print("quotient: ",quotient)

# -------------------------------------------------------------------------------------

#type casting: done by programmer
age = input("enter your age:")
new_age = int(age) + 5 #type casting from string to integer
new_age1 = float(age) + 1 #type casting from string to float
print(new_age , new_age1)

#type conversion : done by python compiler
a = 1 + (2.8899) 
print(a) #3.8899



