# strings can be created using singl as well as double quotes. But, use single quotes for single characters and double quotes for strings.
# strings are immutable.

#----------------------- string methods -----------------------------

name = "John Don"

# find : returnsa index poition of first occurrence of substring. If not found, returns -1

print(name.find("n doe")) # -1
print(name.find("n")) #3

# replace : replaces a substring with another
print(name.replace("Don", "Smith")) # John Smith
print(name.replace("hn", "nny")) # Jonny Don

#upper() : to uppercase
print(name.upper()) #JOHN DON

#lower() : to lowercase
print(name.lower()) #john don

# check presence : returns boolean value
print("john" in name) #False

# startswith() : returns boolean value
print(name.startswith("J")) #True

# endswith() : returns boolean value, checks with the string ends with given substring or not
print(name.endswith("Don")) #True
print(name.endswith("n")) #True


# -------------------exercise -----------------------------
# 1. Take price of three products as input and calculate the bill and find average

price1 = float(input("Enter price of product 1:"))
price2 = float(input("Enter price of product 2:"))
price3 = float(input("Enter price of product 3:"))

# find bill
bill  = price1 + price2 + price3
print("Total bill= ", bill)

# calculate average
avg = bill/3
print("Average price= ", avg)

# 2. Take a string as input and check if it starts with s or S or not
text = input("Enter a String: ")
temp = text.lower()
print("if the string starts with s or S: ", temp.startswith("s"))