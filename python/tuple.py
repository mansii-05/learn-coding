# Tuple: It is immutable, non-primitive data-type. It is created using () or without (), but we prefer using parenthesis.

score = (12, "Mansi", 34, 45, 67)
print(type(score)) #tuple

# check frequency of a value
print(score.count(34)) #1

#get index of a value
print(score.index(45))
# print(score.index(14)) #ValueError: tuple.index(x): x not in tuple

# access a value
print(score[4]) # 67
print(score[2:5])  #(34, 45, 67)