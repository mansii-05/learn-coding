# collection of unique items is called a set. It is created using {}
# It doesn't stores(doesn't considers even if we write them in set) duplicate values.

ages = {34, "Ansi", 45, 78, 78, 98, 56}

print(len(ages)) #6 , not 7

for a in ages:
    print(a)
print(ages)

# ===================DICTIONARY============================

# {key => value}, it is a collection of key-value pairs with unique key, but duplicate values can be there.

my_dict = {"name": "Bob", "age": 21, "isStudent": True}

# modifying values
my_dict["course"] = "Python" #add new value
my_dict["age"] = 24 #update old value
del my_dict["isStudent"] #delete a value

# accessing values
for a in my_dict:
    print(a, my_dict[a])