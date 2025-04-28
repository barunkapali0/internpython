print("voting eligiblity test.")
a=input("Enter your name:")
b=int(input("Enter your age:"))
if b>100:
    print("Invalid age.")
elif b>=18:
    print(f"{a},You are eligible to vote.Lets start.")  
else:
    print(f"{a},You are not eligible to vote.")    