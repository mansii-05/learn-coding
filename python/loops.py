# range() , returns a sequence of numbers starting with 0 by default
range(6) # 0, 1, 2, 3, 4, 5 

range(5, 10) #5, 6, 7, 8, 9

# range(start, stop, step) # start : starting number, stop : ending number, step : increment/decrement value
range(1, 10, 2) #1, 3, 5, 7, 9

# --------------------------LOOPS----------------------------------------------------

# 1. WHILE loop

# initialise counter variable
# while condition:
    #code to be executed
    #increment/decrement the value of variable used in condition
i = 1
while(i<= 5):
    print(i* " *")
    i+=1

print("Inverted triangle")
j = 5
while(j>=1):
    print(j* " *")
    j-=1

# 2. FOR loop

# for variable in range(start, stop, step):
    #code to be executed

# way 1
num = range (1, 20, 2)
#Q. print odd numbers between 1 to 20
for i in num: #i is temporary variable here
    print(i)

# way 2
# Q. table of 57
for i in range(1,11):
    print (57*i)

# continue(skip aniteration) and break(exit the loop) stt

# Q. print all multiples of 3 but skip 15 between 1 to 50
for i in range(3, 50, 3):
    if(i==15):
        continue
    print(i)

#Q. take range of 1 to 1000, and find the first nuber divisible by 2 and 13
for i in range(1, 1000):
    if(i%2==0 and i%13==0):
        print("Num is:", i)
        break