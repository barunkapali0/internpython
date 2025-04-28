#grade checker.
print("Grade checker")
a=float(input("Enter your GPA:"))
if a>4.0:
    print("invalid GPA!")
elif a>=3.65:
    print("your grade is A+")
elif a>=3.25:
    print("your garde is A")    
elif a>=2.85:
    print("your garde is B+")  
elif a>=2.45:
    print("your garde is B")  
elif a>=2.05:
    print("your garde is C+")      
elif a>=1.65:
    print("your garde is C")      
elif 1.60>a:
    print("you failed.")    
      