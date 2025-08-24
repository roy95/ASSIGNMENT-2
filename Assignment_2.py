# a=float(input("Enter the first_Number: "))
# b=float(input("Enter the Second_Number: "))
# z=float
# c=input("Enter the Operator(+, _, *, /): ")
# if c=="+":
#     z=a+b
#     print("Your sum value is", z)
# elif c=="-":
#     z=a-b
#     print("Your substract value is", z)
# elif c=="*":
#     z=a*b
#     print("Your Multiplication value is", z)
# elif c=="/":
#     z=a/b
#     print("Your devide value is", z)
# else :
#     print("enter a Valid no or operator")

# a=int(input("How Difference you want to print: "))
# b=int(input("How much you want to print: "))
# n=list(range(0,b+1,a))
# for i in n:
#     print(i*7)

# x=['Apple','Book', 7.0, 90000]
# for i in x:
#     print(i)

# for i in range(0,11):
#     print("*")
# counter = 0
# while counter <= 5 :
#     print('a'*counter)
#     counter += 1



what=input("what you want to perform: \n 1.even odd: \n 2.sum of integer: ")
what=int(what)
if what==1:
# Check if a Number is Even or Odd
    a=int(input("Enter a Number: "))
    if a%2==0 :
        print("The Number You Enter", a ,"is a Even Number.")
    else:
        print("The Number You Enter", a ,"is a odd Number.")

elif what==2:
# Sum of Integers from 1 to user input Using a Loop
    b=int(input("Enter the range you want to add: "))
    sum=0
    for i in range(0,b+1):
        sum=sum+i
    print("The Sum value of 1 to", b ,"is: ", sum)
else:
    print("Enter a valid Selection")
