# arithmetic operators: + , - , * , / , % , ** (power) , // (floor division, gives int value) 

print(5 + 2)  # 7 
print(5 - 2)  # 3
print(5 * 2)  # 10
print(5 / 2)  # 2.5
print(5 // 2) # 2
print(5 ** 2) # 25

# assignment operators: = , += , -= , *= , /= , %= , **= , //=
x = 5

x+= 2 # it means x = x + 2,similarly other operators can be used
print(x) #7

# operator precedence: () , ** , * , / , // , % , + , -

y = 5 + 2 * 3 / 2 - 1 % 2
print(y) # 7

# comparison operators : == , !=, >= , <= , > , <
print( 5 == 2) #False

# Logical operators : and , or, not : checks the condition on stt and returns boolean value

print(5 > 2 and 2 < 1)  #False
print(5 > 2 or 2 < 1)  #True
print(not(1>2)) #True