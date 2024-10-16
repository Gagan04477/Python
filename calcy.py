a=float(input("Enter the number:"))
b=float(input("Enter the number:"))
operator=input("Enter the operator(+,-,*,?):")
if operator=="+":
    result=float(a)+float(b)
elif operator=="-":
    result=float(a)-float(b)
elif operator=="*":
    result=float(a)*float(b)
elif operator=="/":
    result=float(a)/float(b)
elif operator==" ":
    print("Invalid")
print("Result",result)

   