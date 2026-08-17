
# List : It is mutable. It is a collection of items of similar or different datatypes written within []

marks = [90, 56, 45, 99, 89]
print(type(marks)) #list

# add an item 
marks.append(67) #adds at end, [90, 56, 45, 99, 89, 67]
print(marks)

marks.insert(2, 12) #adds at specified index, [90, 56, 12, 45, 99, 89, 67]
print(marks)

# find length of list len()
print(len(marks)) #7

#access elements
print(marks[3]) #45
print(marks[-1]) #67

# slicing 
print(marks[2:5]) #[12, 45, 99]
print(marks[-3:])  #[99, 89, 67]

# traverse through list
for a in marks:
    print(a)

# check if an item is present in list
print(121 in marks) #False

# delete an item
marks.remove(12)
print(marks) #[90, 56, 45, 99, 89, 67]

# clear the list
marks.clear()
print(marks) #[]