# indentation is used to define the scope of if/elif/else statements

age = int(input("Enter your age:"))

if(age>=21):
    print("you are eligible to drive")
    print("Age is 21 or above")

elif(age >=18):
    print("you are eligible to vote, but not to drive")

else: 
    print("You are not eligible to vote or drive")

print("End of code")