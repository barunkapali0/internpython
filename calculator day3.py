print("Basic calculator.")
print("Choose the operation u want to perform.")
print("1.Addition.(+)")
print("2.subtraction.(-)")
print("3.Multiplication.(*)")
print("4.Division.(/)")
print("5.Power.(**)")
a=int(input("Enter first num:"))
op=int(input("choose a number from above operations:"))
b=(int(input("Enter second num:")))
if op==1:
    m=a+b
    print(m)
elif op==2:
    m=a-b
    print(m)    
elif op==3:
    m=a*b
    print(m)
elif op==4:
    m=a/b
    print(m)  
elif op==5:
    m=a**b
    print(m)   
else:
    print("invalid number.Choose the right operator.")       